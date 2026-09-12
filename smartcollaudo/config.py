"""Configurazione applicativa, logging e disponibilita' ActiveX/COM."""

from __future__ import annotations

import logging
import os
import platform
from pathlib import Path

from .version import APP_LOG_DIR_NAME, APP_NAME


def resolve_log_file() -> Path:
    """Restituisce un percorso log stabile, indipendente dalla cartella di avvio."""
    appdata_dir = os.getenv("APPDATA")
    log_dir = Path(appdata_dir) / APP_LOG_DIR_NAME if appdata_dir else Path.home() / f".{APP_LOG_DIR_NAME.lower()}"

    try:
        log_dir.mkdir(parents=True, exist_ok=True)
    except OSError:
        log_dir = Path.cwd()

    return log_dir / "SmartCollaudo.log"


LOG_FILE = resolve_log_file()

logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)
logger = logging.getLogger(APP_NAME)

try:
    import win32com.client as win32  # type: ignore

    try:
        import pythoncom  # type: ignore
    except ImportError:
        pythoncom = None

    PYWIN32_AVAILABLE = True
except ImportError:
    win32 = None
    pythoncom = None
    PYWIN32_AVAILABLE = False

WINDOWS_AVAILABLE = platform.system().lower() == "windows"
ACTIVEX_AVAILABLE = WINDOWS_AVAILABLE and PYWIN32_AVAILABLE
