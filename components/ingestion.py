import pytesseract
from pytesseract import image_to_string
from pdf2image import convert_from_path
from PIL import Image
import re
import pandas as pd
from config.config import *
pytesseract.pytesseract.tesseract_cmd= r"C:\Program Files\Tesseract-OCR\tesseract.exe"


class ingestion():
    def pdf_to_images(self,pdf_path:ingestion_config.file_path):
        '''
        The method will give the pdf file into images 
        use if it has multiple pages you will get multiple 
        image objects
        '''
        images = convert_from_path(pdf_path)
        return images
    
    
    
    
    

