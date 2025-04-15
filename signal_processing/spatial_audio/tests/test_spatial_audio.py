import numpy as np
import quaternion
import spatial_audio.spatial_audio


def test_spatial_audio(kwargs, project_dir):
    kwargs["spatial_audio"]["hrtf"]["path"] = project_dir / kwargs["spatial_audio"]["hrtf"]["path"]
    kwargs["spatial_audio"]["initial_azimuth"] = kwargs["test"]["input"]["azimuths"]
    kwargs["spatial_audio"]["initial_elevation"] = kwargs["test"]["input"]["elevations"]
    sp = spatial_audio.spatial_audio.SpatialAudio(**kwargs["spatial_audio"])
    sp.tare_head_orientation(0, 0, 0)
    assert sp.global_orientation == quaternion.quaternion(1, 0, 0, 0)
    sp.set_head_orientation(0, 0, 0)
    assert sp.head_orientation == quaternion.quaternion(1, 0, 0, 0)

    assert np.allclose(sp.azimuth_CH, sp.initial_azimuth_CH)
    assert np.allclose(sp.elevation_CH, sp.initial_elevation_CH)

    el, az = sp.combine_head_orientation()
    assert np.allclose(el, sp.elevation_CH)
    assert np.allclose(np.mod(az, 360), np.mod(sp.azimuth_CH, 360))

    sp.set_head_orientation(**kwargs["test"]["orientation"])
    el, az = sp.combine_head_orientation()
    assert np.allclose(el, kwargs["test"]["expected"]["elevations"], atol=1)
    valid_idx = np.where(np.abs(np.abs(el) - 90) > 1)[0]
    az = az[valid_idx]
    expected_az = np.array(kwargs["test"]["expected"]["azimuths"])[valid_idx]
    delta = (az - expected_az + 180) % 360 - 180
    assert np.all(np.abs(delta) < 1)
