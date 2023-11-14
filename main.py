import pytesseract
from pytesseract import image_to_string
from pdf2image import convert_from_path
from PIL import Image
import re
import pandas as pd
from config import *
import os
from components.ingestion import *
from components.docus import *
from components.toexcel import *
pytesseract.pytesseract.tesseract_cmd= r"C:\Program Files\Tesseract-OCR\tesseract.exe"

ingestion_config = ingestion_config()

ingestion = ingestion()

images = ingestion.pdf_to_images(ingestion_config.file_path)

print(images[4])

process_config = process_config()
process = process()
docs = process.create_doc_files(image_objects=images)
print(docs)

to_excel_config = to_excel_config()
to_excel = to_excel()
to_excel.excel(path="artifact\images")
            

    



    

