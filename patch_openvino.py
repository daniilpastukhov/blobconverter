import os
import subprocess
import sys
from pathlib import Path

versions = {
    "2021_4": Path("/opt/intel/openvino_2021"),
    "2021_3": Path("/opt/intel/openvino2021_3"),
    "2021_2": Path("/opt/intel/openvino2021_2"),
    "2021_1": Path("/opt/intel/openvino2021_1"),
    "2020_4": Path("/opt/intel/openvino2020_4"),
}

legacy = {
    "2020_3": Path("/opt/intel/openvino2020_3"),
    "2020_2": Path("/opt/intel/openvino2020_2"),
    "2020_1": Path("/opt/intel/openvino2020_1"),
    "2019_3": Path("/opt/intel/openvino2019_3"),
}

def abs_str(path: Path):
    return str(path.absolute())


def apply_patch(name: str, path: Path, interpreter):
    zoo_path = path / "deployment_tools" / "open_model_zoo"

    subprocess.check_call(["cp", "/opt/intel/models_gdrive.patch", abs_str(zoo_path)])
    subprocess.check_call(["git", "apply", "models_gdrive.patch"], cwd = abs_str(zoo_path))




if __name__ == "__main__":
    for env_name, base_path in versions.items():
        apply_patch(env_name, base_path, "python3.8")
    for env_name, base_path in legacy.items():
        apply_patch(env_name, base_path, "python3.7")
