import sys
import random
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QGroupBox, QMessageBox
from PyQt5.QtCore import Qt, QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Erzurum Devlet Hastanesi - Hasta Takip Sistemi")
        self.setGeometry(100, 100, 1200, 700)
        self.setStyleSheet("background-color: #ffe6e6; font-family: Arial;")

        # Ana widget ve layout
        self.central_widget = QWidget()
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(15)

        # Başlık
        self.title_label = QLabel("Erzurum Devlet Hastanesi - Hasta Takip Sistemi", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 22px; font-weight: bold; color: #0044cc;")
        self.main_layout.addWidget(self.title_label)

        # Hasta Bilgileri
        self.patient_info_group = QGroupBox("Hasta Bilgileri", self)
        self.patient_info_group.setStyleSheet("font-size: 14px; color: #333; font-weight: bold;")
        self.patient_info_layout = QVBoxLayout()

        self.upper_row_layout = QHBoxLayout()

        self.name_box = QGroupBox("Hasta Adı")
        self.name_box.setStyleSheet("font-size: 14px; font-weight: bold; color: #333;")
        name_box_layout = QVBoxLayout()
        name_label = QLabel("Mehmetcan Alpsungur")
        name_label.setStyleSheet("font-size: 11px; color: #555;")
        name_box_layout.addWidget(name_label)
        self.name_box.setLayout(name_box_layout)

        self.details_box = QGroupBox("Bilgiler")
        self.details_box.setStyleSheet("font-size: 14px; font-weight: bold; color: #333;")
        details_box_layout = QVBoxLayout()
        details_label = QLabel("Yaş: 45   Cinsiyet: Erkek   Aciliyet: Orta")
        details_label.setStyleSheet("font-size: 11px; color: #555;")
        details_box_layout.addWidget(details_label)
        self.details_box.setLayout(details_box_layout)

        self.upper_row_layout.addWidget(self.name_box)
        self.upper_row_layout.addWidget(self.details_box)

        self.complaint_box = QGroupBox("Hasta Şikayeti")
        self.complaint_box.setStyleSheet("font-size: 14px; font-weight: bold; color: #333;")
        complaint_box_layout = QVBoxLayout()
        complaint_label = QLabel("Kalp Çarpıntısı")
        complaint_label.setStyleSheet("font-size: 11px; color: #555;")
        complaint_box_layout.addWidget(complaint_label)
        self.complaint_box.setLayout(complaint_box_layout)

        self.patient_info_layout.addLayout(self.upper_row_layout)
        self.patient_info_layout.addWidget(self.complaint_box)
        self.patient_info_group.setLayout(self.patient_info_layout)
        self.main_layout.addWidget(self.patient_info_group)

        # EKG Alanı
        self.ekg_group = QGroupBox("Hastanın EKG Değerleri", self)
        self.ekg_group.setStyleSheet("font-size: 14px; color: #333;")
        ekg_layout = QVBoxLayout()

        self.figure = Figure(figsize=(8, 4))
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_ylim(-70, 70)
        self.ax.set_facecolor("#f7f7f7")
        self.ax.set_title("EKG Durumu", fontsize=16, loc="center", color="green", pad=20)
        self.ax.set_xlabel("Veri Noktaları", fontsize=12)
        self.ax.set_ylabel("Gerilim (mV)", fontsize=12)
        self.figure.subplots_adjust(top=0.85, bottom=0.2)
        ekg_layout.addWidget(self.canvas)

        self.ekg_group.setLayout(ekg_layout)
        self.main_layout.addWidget(self.ekg_group)

        # Hasta Verileri
        self.data_group = QGroupBox("Hasta Verileri", self)
        self.data_group.setStyleSheet("font-size: 14px; color: #333;")
        data_layout = QHBoxLayout()

        self.temp_label = QLabel("Hastanın Sıcaklık Değerleri: 0°C", self)
        self.temp_label.setStyleSheet("font-size: 14px; color: #333;")
        data_layout.addWidget(self.temp_label)

        self.pulse_label = QLabel("Hastanın Nabız Değerleri: 0 bpm", self)
        self.pulse_label.setStyleSheet("font-size: 14px; color: #333;")
        data_layout.addWidget(self.pulse_label)

        self.data_group.setLayout(data_layout)
        self.main_layout.addWidget(self.data_group)

        # Ana widget'i ayarla
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.main_layout)

        # Zamanlayıcılar
        self.timer = QTimer()
        self.timer.setInterval(4000)  # 1 saniyede bir güncelleme
        self.timer.timeout.connect(self.update_values)
        self.timer.start()

        # Grafik Verileri
        self.x_data = np.linspace(0, 10, 100)
        self.y_data = np.zeros(100)
        self.line, = self.ax.plot(self.x_data, self.y_data, color='blue')

    def update_values(self):
        try:
            data_temp_pulse = pd.read_excel("sıcaklık_nabız.xlsx")
            data_ekg = pd.read_excel("megadeneme.xlsx")

            last_row_temp_pulse = data_temp_pulse.iloc[-1]
            last_row_ekg = data_ekg.iloc[-1]

            temperature = last_row_temp_pulse["Sıcaklık"]
            pulse = last_row_temp_pulse["Nabız"]

            self.temp_label.setText(f"Hastanın Sıcaklık Değerleri: {temperature}°C")
            self.pulse_label.setText(f"Hastanın Nabız Değerleri: {pulse} bpm")

            self.y_data = last_row_ekg.values
            self.line.set_ydata(self.y_data)
            self.ax.relim()
            self.ax.autoscale_view()
            self.canvas.draw()

        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Veriler güncellenirken bir hata oluştu: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
