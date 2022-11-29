"""Load configuration from .toml file."""
import tomllib
from pathlib import Path

# Read local `config.toml` file.
CONFIG_PATH = Path(__file__).parent / 'config.toml'

with CONFIG_PATH.open("rb") as fi:
    config = tomllib.load(fi)
