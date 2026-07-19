"""Interfaz de linea de comandos."""
from __future__ import annotations
import argparse, json, logging
from pathlib import Path
from .service import Service
def run(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="FatimaCyberLabs security tool")
    parser.add_argument("--verbose", action="store_true")
    commands = parser.add_subparsers(dest="command", required=True)
    inspect = commands.add_parser("inspect", help="Inspecciona una entrada")
    inspect.add_argument("target", type=Path); inspect.add_argument("--output", type=Path, required=True)
    stats = commands.add_parser("stats", help="Muestra estadisticas")
    stats.add_argument("file", type=Path)
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)
    try:
        if args.command == "inspect":
            findings = Service().inspect(args.target); Service.export(findings, args.output); print(f"Exportados {len(findings)} hallazgos a {args.output}")
        else:
            records = json.loads(args.file.read_text(encoding="utf-8")); print(json.dumps(Service.stats([__import__("src.models", fromlist=["Finding"]).Finding(**r) for r in records]), indent=2))
        return 0
    except (OSError, ValueError) as exc:
        logging.error("%s", exc); return 2
