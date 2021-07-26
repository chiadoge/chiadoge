# std
import logging
import sys
from pathlib import Path
from typing import Optional
import yaml


class Config:
    def __init__(self, config_path: Path):
        if not config_path.is_file():
            raise ValueError(f"Invalid config.yaml path: {config_path}")

        with open(config_path, "r", encoding="UTF-8") as config_file:
            self._config = yaml.safe_load(config_file)

    def _get_child_config(self, key: str, required: bool = True) -> Optional[dict]:
        if key not in self._config.keys():
            if required:
                raise ValueError(f"Invalid config - cannot find {key} key")
            else:
                return None

        return self._config[key]

    def get_config(self):
        return self._config

    def get_crypto_config(self):
        return self._get_child_config("crypto")

    def get_monitor_server(self):
        return self._get_child_config("monitor").get("server")


def check_keys(required_keys, config) -> bool:
    for key in required_keys:
        if key not in config.keys():
            logging.error(f"Incompatible configuration. Missing {key} in {config}.")
            return False
    return True


def is_win_platform() -> bool:
    return sys.platform.startswith("win")
