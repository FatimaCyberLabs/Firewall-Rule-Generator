"""Configuracion de aplicacion."""
from dataclasses import dataclass
from pathlib import Path
@dataclass(frozen=True, slots=True)
class Settings:
    output_dir: Path = Path("output")
    log_level: str = "INFO"
