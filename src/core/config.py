import pathlib
import shutil

import tomllib

import core.logs as logger

CONFIG_PATH = pathlib.Path("~/.config/ncspot-rpc/config.toml").expanduser()
EXAMPLE_PATH = pathlib


class Basic:
    def __init__(self) -> None:
        self.logs = logger.Logger()
        self._ensure_config()
        config = self._load_config()

        self.DEBUG: bool = config.get("general", {}).get("DEBUG", False)
        self.LOGS_ADD_SONG: bool = config.get("general", {}).get("LOGS_ADD_SONG", True)
        self.RUNTIME_PATH: str = config.get("socket", {}).get(
            "RUNTIME_PATH", "/run/user/1000/ncspot"
        )
        self.API_CLIENT_ID: str = config.get("api", {}).get("DISCORD_CLIENT_ID", None)
        self.DISPLAY_CLIENT: bool = config.get("format", {}).get("DISPLAY_CLIENT", True)
        self.DISPLAY_PLAYER_ICON: bool = config.get("format", {}).get(
            "DISPLAY_PLAYER_ICON", True
        )
        self.DISPLAY_PROGRESS: bool = config.get("format", {}).get(
            "DISPLAY_PROGRESS", True
        )

    def _ensure_config(self):
        self.logs.debug(f"CONFIG_PATH resolves to: {CONFIG_PATH}")
        self.logs.debug(f"EXAMPLE_PATH resolves to: {EXAMPLE_PATH}")
        self.logs.debug(f"Config exists: {CONFIG_PATH.exists()}")

        if not CONFIG_PATH.exists():
            self.logs.debug("COPYING NOW!")

            CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(EXAMPLE_PATH, CONFIG_PATH)

            self.logs.warn("No default configuration found! ")
            self.logs.success(f"Created a new default config at {CONFIG_PATH}")

    def _load_config(self):
        self.logs.info(f"Attempting to load config from: {CONFIG_PATH}")

        with open(CONFIG_PATH, "rb") as f:
            data = tomllib.load(f)

        self.logs.success("Config successfully loaded.")
        return data
