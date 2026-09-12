"""Compatibilita' per import legacy della versione."""

from smartcollaudo.version import (
    APP_LOG_DIR_NAME,
    APP_NAME,
    APP_VERSION,
    CHANGELOG,
    read_app_version,
)

__all__ = ["APP_LOG_DIR_NAME", "APP_NAME", "APP_VERSION", "CHANGELOG", "read_app_version"]
