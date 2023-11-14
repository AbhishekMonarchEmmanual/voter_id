import pytesseract
from pytesseract import image_to_string
from pdf2image import convert_from_path
from PIL import Image
import re
import pandas as pd
from config.config import *
from config.artifact_config import process_artifact
import os
pytesseract.pytesseract.tesseract_cmd= r"C:\Program Files\Tesseract-OCR\tesseract.exe"


class process():
    def __init__(self):
        self.process_config = process_config()

    def create_doc_files(self, image_objects):
        os.makedirs(self.process_config.artifact, exist_ok=True)
        for i in range(len(image_objects)):
            text = image_to_string(image_objects[i], config=self.process_config.custom_config)
            with open(os.path.join(self.process_config.artifact, f"text{i}.txt"), "w") as file:
                file.write(text)
        




            

    



    

