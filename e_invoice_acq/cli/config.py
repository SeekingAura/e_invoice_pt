import json
from pathlib import Path
from typing import (
    Any,
    TypedDict,
    cast,
)

ROOT_DIR: Path = Path.home() / ".e_invoice_acq"
CONFIG_DIR: Path = ROOT_DIR / "config"
CONFIG_FILE: Path = CONFIG_DIR / "config.json"
DEFAULT_OUTPUT_DIR: Path = ROOT_DIR / "output"


class configDict(TypedDict):
    output_dir: str


def load_config(config_path: Path = CONFIG_FILE) -> configDict:
    if not config_path.exists():
        return cast(
            configDict,
            dict(),
        )
    with open(config_path, "r") as file:
        return cast(
            configDict,
            json.load(file),
        )


def save_config(config: dict[str, Any]):
    if not CONFIG_DIR.exists():
        CONFIG_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )
    with open(CONFIG_FILE, "w") as file:
        json.dump(
            config,
            file,
            indent=4,
        )
