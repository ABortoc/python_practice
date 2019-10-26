import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_watermark(pdf_list):
    with open(pdf_list[0], "rb") as file_input:
        pdf = PyPDF2.PdfFileReader(file_input)
        num_pages = pdf.getNumPages()
        with open(pdf_list[1], "rb") as file_watermark:
            watermark = PyPDF2.PdfFileReader(file_watermark)
            watermark_page = watermark.getPage(0)
            page_counter = 0
            pdf_writer = PyPDF2.PdfFileWriter()
            for page in range(num_pages):
                page_to_watermark = pdf.getPage(page_counter)
                page_counter += 1
                page_to_watermark.mergePage(watermark_page)
                pdf_writer.addPage(page_to_watermark)
            with open(pdf_list[2], "wb") as file_output:
                pdf_writer.write(file_output)


pdf_watermark(inputs)
