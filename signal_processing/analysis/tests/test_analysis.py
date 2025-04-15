import argparse
import pathlib
import shutil

import analysis.instances.analysis
import data_handle.utils
import deepmerge
import numpy as np
import parse_sweeps.parse_sweeps


def prepare_data(**data_kwargs):
    k = dict(
        mean=0,
        std=1,
        channel_shape=data_kwargs["system"]["input_buffer"]["channel_shape"],
        nsamples=data_kwargs["simulation"]["nsamples"],
        dtype=np.dtype(data_kwargs["input"]["dtype"]),
        path=data_kwargs["input"]["path"],
    )
    data_handle.utils.normal_data_file(**k)


def test_analysis(kwargs, project_dir, tmp_path):
    cliargs = argparse.Namespace()
    cliargs.yaml_path = project_dir / kwargs["yaml_path"]
    activator_kwargs = parse_sweeps.parse_sweeps.parse_sweeps(cliargs.yaml_path)[0]
    activator_kwargs["output"]["dir"] = tmp_path / activator_kwargs["output"]["dir"]
    activator_kwargs["input"]["path"] = tmp_path / pathlib.Path(activator_kwargs["input"]["path"]).name
    prepare_data(**activator_kwargs)

    cliargs.output_dir = tmp_path / kwargs["output"]["dir"]
    cliargs.indices = kwargs["indices"]
    cliargs.parallel = True

    shutil.rmtree(cliargs.output_dir, ignore_errors=True)
    an = analysis.instances.analysis.Analysis(cliargs=cliargs)

    merger = deepmerge.Merger([(dict, ["merge"])], ["override"], ["override"])

    an.activator_kwargs_list = [
        merger.merge(
            activator_kwargs,
            {
                "output": {"dir": tmp_path / activator_kwargs["output"]["dir"]},
                "input": {"path": tmp_path / activator_kwargs["input"]["path"]},
            },
        )
        for activator_kwargs in an.activator_kwargs_list
    ]
    an.execute()

    assert len(an.results) == 3
    nexecutes = len(cliargs.indices)
    assert [len(an.results[key]) == nexecutes for key in an.results]

    assert cliargs.output_dir.is_dir()
    for i in cliargs.indices:
        output_dir = cliargs.output_dir / f"output{i}"
        assert output_dir.is_dir()
        assert (output_dir / "reflector1.bin").is_file()
        assert (output_dir / "reflector2.bin").is_file()
        assert (output_dir / "reflector1.png").is_file()
        assert (output_dir / "reflector2.png").is_file()
        assert (output_dir / "params.yaml").is_file()
