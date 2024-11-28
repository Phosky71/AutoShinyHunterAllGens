import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QVBoxLayout, QWidget, QLabel, \
    QHBoxLayout, QComboBox, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Emulator Launcher")
        self.setGeometry(100, 100, 400, 250)  # Tamaño de la ventana

        # Layout principal
        layout = QVBoxLayout()

        # Selector de generación (1 a 9)
        self.gen_label = QLabel("Seleccionar Generación:")
        self.gen_combo = QComboBox()
        for i in range(1, 10):
            self.gen_combo.addItem(f"Generación {i}")
        layout.addWidget(self.gen_label)
        layout.addWidget(self.gen_combo)

        # Layout para importar archivos
        import_layout = QVBoxLayout()

        # Selección de archivo SAV (Battery file)
        self.sav_label = QLabel("No se ha seleccionado archivo SAV")
        sav_button = QPushButton("Seleccionar archivo SAV")
        sav_button.clicked.connect(self.select_sav)
        import_layout.addWidget(self.sav_label)
        import_layout.addWidget(sav_button)

        # Selección de archivo ROM (Archivo GBA)
        self.rom_label = QLabel("No se ha seleccionado archivo ROM")
        rom_button = QPushButton("Seleccionar archivo ROM")
        rom_button.clicked.connect(self.select_rom)
        import_layout.addWidget(self.rom_label)
        import_layout.addWidget(rom_button)

        # Botón para ejecutar el emulador
        execute_button = QPushButton("Ejecutar Emulador")
        execute_button.clicked.connect(self.run_emulator)
        layout.addWidget(execute_button)

        # Agregar el layout de importación al layout principal
        layout.addLayout(import_layout)

        # Widget principal
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Variables para almacenar las rutas seleccionadas
        self.sav_path = None
        self.rom_path = None

    def select_sav(self):
        """Función para seleccionar el archivo SAV"""
        self.sav_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo SAV", "", "Archivos SAV (*.sav)")
        if self.sav_path:
            self.sav_label.setText(f"Archivo SAV seleccionado: {self.sav_path}")

    def select_rom(self):
        """Función para seleccionar el archivo ROM"""
        self.rom_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo ROM", "", "Archivos GBA (*.gba)")
        if self.rom_path:
            self.rom_label.setText(f"Archivo ROM seleccionado: {self.rom_path}")

    def run_emulator(self):
        """Función para ejecutar el emulador con los archivos seleccionados"""
        selected_gen = self.gen_combo.currentText()
        if selected_gen != "Generación 1":
            QMessageBox.critical(self, "Error", "La generación seleccionada no está disponible todavía.")
            return

        if self.sav_path and self.rom_path:
            # Aquí es donde ejecutarías el emulador con las rutas seleccionadas
            print(f"Ejecutando emulador con:\nROM: {self.rom_path}\nSAV: {self.sav_path}")
        else:
            QMessageBox.critical(self, "Error", "Por favor selecciona un archivo ROM y un archivo SAV.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())