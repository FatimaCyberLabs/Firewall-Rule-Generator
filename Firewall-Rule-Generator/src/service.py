"""Casos de uso comunes: carga, normalizacion, estadisticas y exportacion."""
from __future__ import annotations
import json
import logging
import re
from collections import Counter
from pathlib import Path
from .models import Finding
LOGGER = logging.getLogger(__name__)

IP_RE = re.compile(r"^\d{1,3}(\.\d{1,3}){3}$")

class Service:
    """Base reutilizable para adaptadores especificos de cada herramienta."""
    def inspect(self, target: Path) -> list[Finding]:
        if not target.exists(): raise FileNotFoundError(target)
        findings: list[Finding] = []
        for raw in target.read_text(encoding="utf-8", errors="ignore").splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            parts = [p.strip() for p in line.split(",")]
            if len(parts) != 3:
                findings.append(Finding(category="invalid_rule_line", value=line, source=str(target), severity="low"))
                continue
            ip, port, action = parts
            if not IP_RE.match(ip) or action.lower() not in {"allow", "deny"}:
                findings.append(Finding(category="invalid_rule_line", value=line, source=str(target), severity="low"))
                continue
            target_flag = "ACCEPT" if action.lower() == "allow" else "DROP"
            rule = f"iptables -A INPUT -s {ip} -p tcp --dport {port} -j {target_flag}"
            findings.append(Finding(category="firewall_rule", value=rule, source=str(target), severity="info"))
        return findings
    @staticmethod
    def export(findings: list[Finding], destination: Path) -> None:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(json.dumps([item.to_dict() for item in findings], indent=2) + "\n", encoding="utf-8")
    @staticmethod
    def stats(findings: list[Finding]) -> dict[str, object]:
        return {"total": len(findings), "by_category": dict(Counter(item.category for item in findings)), "by_severity": dict(Counter(item.severity for item in findings))}
