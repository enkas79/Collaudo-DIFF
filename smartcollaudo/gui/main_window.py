"""Finestra principale dell'applicazione."""

from __future__ import annotations

from PyQt6.QtWidgets import QMainWindow, QMessageBox

from smartcollaudo.version import APP_NAME, APP_VERSION


class SmartCollaudoWindow(QMainWindow):
    """Finestra principale con la barra dei menu obbligatoria."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(APP_NAME)
        self.resize(1024, 768)
        self._build_menu_bar()

    def _build_menu_bar(self) -> None:
        help_menu = self.menuBar().addMenu("&Aiuto")

        about_action = help_menu.addAction("&Informazioni")
        about_action.triggered.connect(self._show_about)

        update_action = help_menu.addAction("&Controlla Aggiornamenti")
        update_action.triggered.connect(self._check_for_updates)

        guide_action = help_menu.addAction("&Guida")
        guide_action.triggered.connect(self._show_guide)

    def _show_about(self) -> None:
        QMessageBox.about(
            self,
            f"Informazioni su {APP_NAME}",
            f"{APP_NAME}\nVersione {APP_VERSION}\n\nAutore: enkas79",
        )

    def _check_for_updates(self) -> None:
        # TODO: eseguire la verifica in QThread verso GitHub Releases.
        QMessageBox.information(self, "Controlla Aggiornamenti", "Funzione di aggiornamento non ancora implementata.")

    def _show_guide(self) -> None:
        QMessageBox.information(self, "Guida", f"Guida all'uso di {APP_NAME} non ancora disponibile.")
