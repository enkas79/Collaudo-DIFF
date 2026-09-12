"""Metadati di versione, letti dinamicamente da version.txt."""

from __future__ import annotations

from pathlib import Path

APP_NAME = "SmartCollaudo PRO"
APP_LOG_DIR_NAME = "SmartCollaudo"

# Changelog placeholder: da popolare per versione con le note di rilascio.
CHANGELOG: dict[str, str] = {}

_VERSION_FILE = Path(__file__).resolve().parent.parent / "version.txt"


def read_app_version() -> str:
    """Legge la versione corrente da version.txt nella root del progetto."""
    try:
        return _VERSION_FILE.read_text(encoding="utf-8").strip()
    except OSError:
        return "0.0.0"


APP_VERSION = read_app_version()
