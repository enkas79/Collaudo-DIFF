"""Launcher for SmartCollaudo PRO."""

from __future__ import annotations

import sys

from PyQt6.QtWidgets import QApplication

from smartcollaudo.config import logger
from smartcollaudo.gui.main_window import SmartCollaudoWindow
from smartcollaudo.version import APP_NAME, APP_VERSION


def main() -> int:
    """Entry point dell'applicazione desktop."""
    logger.info("Avvio %s v%s", APP_NAME, APP_VERSION)
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    window = SmartCollaudoWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
