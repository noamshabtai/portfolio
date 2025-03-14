import pathlib
import sys

import parse_sweeps.parse_sweeps
import pytest

project_dir = pathlib.Path(__file__).parent
tests_dir = project_dir / "tests"


@pytest.fixture
def root_dir():
    return project_dir.parent


def create_fixture(fixture):
    yaml_path = tests_dir / "config" / f"{fixture}.yaml"

    @pytest.fixture(scope="session", params=parse_sweeps.parse_sweeps.parse_sweeps(yaml_path))
    def k(request):
        return request.param

    setattr(sys.modules[__name__], f"kwargs_{fixture}", k)


for fixture in ["normal_data_file", "make_yaml_safe"]:
    create_fixture(fixture)
