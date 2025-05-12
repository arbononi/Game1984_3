# configs/config.py
from configparser import ConfigParser
from pathlib import Path

# Resolve caminho absoluto
config_path = Path(__file__).parent / "config.ini"

_config = ConfigParser()
_config.read(config_path, encoding="utf-8")

# Acesso seguro
terminal_cfg = _config["Terminal"]
lin_terminal = int(terminal_cfg["lin_terminal"])
col_terminal = int(terminal_cfg["col_terminal"])
lin_message = int(terminal_cfg["lin_message"])
col_message = int(terminal_cfg["col_message"])
size_message_lin = int(terminal_cfg["size_message_lin"])


# from pathlib import Path
# import configparser

# config_path = Path(__file__).parent / "config.ini"
# _config = configparser.ConfigParser()
# _config.read(config_path, encoding="utf-8")

# lin_terminal = int(_config["Terminal"]["lin_terminal"])
# col_terminal = int(_config["Terminal"]["col_terminal"])
# lin_message = int(_config["Terminal"]["lin_message"])
# col_message = int(_config["Terminal"]["col_message"])
# size_message_lin = int(_config["Terminal"]["size_message_lin"])