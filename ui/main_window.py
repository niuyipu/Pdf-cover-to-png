from PyQt5.QtWidgets import QMainWindow, QPushButton, QFileDialog, QLabel, QVBoxLayout, QWidget, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self, pdf_converter):
        super().__init__()
        self.pdf_converter = pdf_converter  # 注入转换逻辑
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PDF to PNG Converter")
        self.setGeometry(300, 200, 400, 200)

        # Layout
        layout = QVBoxLayout()

        # Select PDF Files Button
        self.select_files_btn = QPushButton("Select PDF Files")
        self.select_files_btn.clicked.connect(self.select_files)
        layout.addWidget(self.select_files_btn)

        # Select Output Folder Button
        self.select_folder_btn = QPushButton("Select Output Folder")
        self.select_folder_btn.clicked.connect(self.select_folder)
        layout.addWidget(self.select_folder_btn)

        # Convert Button
        self.convert_btn = QPushButton("Convert to PNG")
        self.convert_btn.clicked.connect(self.convert_pdfs)
        layout.addWidget(self.convert_btn)

        # Status Label
        self.status_label = QLabel("Status: Waiting for input...")
        layout.addWidget(self.status_label)

        # Central Widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Variables to store selected files and folder
        self.pdf_files = []
        self.output_folder = ""

    def select_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select PDF Files", "", "PDF Files (*.pdf)")
        if files:
            self.pdf_files = files
            self.status_label.setText(f"Selected {len(files)} PDF files.")

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if folder:
            self.output_folder = folder
            self.status_label.setText(f"Selected output folder: {folder}")

    def convert_pdfs(self):
        if not self.pdf_files:
            QMessageBox.warning(self, "Warning", "No PDF files selected!")
            return
        if not self.output_folder:
            QMessageBox.warning(self, "Warning", "No output folder selected!")
            return

        converted_files = self.pdf_converter.convert_pdf_to_png(self.pdf_files, self.output_folder)
        QMessageBox.information(self, "Success", f"Converted {len(converted_files)} PDF files!")
        self.status_label.setText("Conversion completed.")
