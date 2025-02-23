import os
from pdf2image import convert_from_path

class PDFConverter:
    @staticmethod
    def convert_pdf_to_png(pdf_files, output_folder, dpi=200):
        """
        将 PDF 文件的第一页转换为 PNG 图片并保存到指定文件夹。
        
        :param pdf_files: list, PDF 文件路径列表
        :param output_folder: str, 图片保存的目标文件夹
        :param dpi: int, 转换图片的分辨率
        :return: list, 转换成功的文件路径列表
        """
        converted_files = []
        for pdf_file in pdf_files:
            try:
                pages = convert_from_path(pdf_file, dpi=dpi, first_page=1, last_page=1)
                output_filename = os.path.join(
                    output_folder,
                    os.path.basename(pdf_file).replace('.pdf', '.png')
                )
                pages[0].save(output_filename, "PNG")
                converted_files.append(output_filename)
            except Exception as e:
                print(f"Error converting {pdf_file}: {e}")
        return converted_files
