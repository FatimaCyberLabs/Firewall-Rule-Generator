# Firewall-Rule-Generator

Herramienta de Blue Team de **FatimaCyberLabs**. Genera reglas auditables para iptables, nftables y Windows Firewall.

## Caracteristicas

- iptables
- nftables
- windows
- tcp
- udp
- icmp

## Arquitectura

src/config.py centraliza configuracion; models.py define contratos; service.py contiene los casos de uso; cli.py presenta la interfaz; main.py es el punto de entrada. La separacion permite sustituir adaptadores sin mezclar logica, E/S y CLI.

## Instalacion

Requiere Python 3.10+. Ejecute python -m pip install -e . y, para pruebas, python -m pip install -e ".[dev]".

## Uso

python -m src.main inspect input --output result.json

python -m src.main stats result.json

## Ejemplos

Consulte examples/ para una entrada de ejemplo y use --help para ver los argumentos disponibles.

## Tecnologias

Python 3, biblioteca estandar, argparse, logging, pathlib, dataclasses y pytest para pruebas.

## Casos de uso reales

Triage local, preparacion de evidencias, automatizacion de tareas SOC y exportacion de resultados compatibles con flujos JSON.

## Limitaciones

Los adaptadores que dependen del sistema operativo o de servicios remotos deben ejecutarse con permisos y conectividad apropiados. Valide siempre los resultados antes de aplicar una accion de respuesta.

## Roadmap

- Adaptadores de API opcionales.
- Integracion con el futuro ThreatIntel-Hub.
- Informes enriquecidos y politicas de retencion.

## Licencia

MIT Â© 2026 FatimaCyberLabs. Consulte [LICENSE](LICENSE).
