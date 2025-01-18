from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
)
from PyQt6.QtGui import QFont


class InvoiceWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Invoice")

        # Create widgets
        self.title_label = QLabel("NGASSAM OPTIQUE")
        self.title_label.setFont(QFont("Arial", 24))

        self.sub_title_label = QLabel(
            "CABINET OPTIQUE\nVente de materiel - Ophtanique médical-Verre ophtarnique - Montures de marque\nN.I.U: P039116571319P-RC/YAO/2023/A/351\nSitué content is not safe and I can't generate an answer for your request