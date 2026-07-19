"""Contratos de datos estables y exportables."""
from dataclasses import asdict, dataclass
from typing import Any
@dataclass(frozen=True, slots=True)
class Finding:
    category: str
    value: str
    source: str
    severity: str = "info"
    def to_dict(self) -> dict[str, Any]: return asdict(self)
