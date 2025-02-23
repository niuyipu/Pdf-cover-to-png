import sys
from PyQt5.QtWidgets import QApplication
from converter.pdf_converter import PDFConverter
from ui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)

    # 创建转换器实例
    pdf_converter = PDFConverter()

    # 创建主窗口
    main_window = MainWindow(pdf_converter)
    main_window.show()

    # 启动应用程序
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
