import pytesseract
from pytesseract import image_to_string
from pdf2image import convert_from_path
from PIL import Image
import re
import pandas as pd
from config.config import *
from config.artifact_config import *
import os
pytesseract.pytesseract.tesseract_cmd= r"C:\Program Files\Tesseract-OCR\tesseract.exe"


class to_excel():
    def __init__(self):
        self.to_excel_config = to_excel_config()
    def excel(self, path:to_excel_config.path):
        files = os.listdir(path)
        for index,file in enumerate(files):
            with open(os.path.join(path,file), "r") as file:
                text = file.read()

                file_content = text.replace("Assembly Constituency No and Name :","\nACNN").replace("Section No and Name", "\nSNON").replace('Age as on', "current_birth_time").replace("Fathers Name", "\nFathersN").replace("Husbands Name", "\nHusbandN").replace("House Number", "\nHouseN").replace("Others","\nOther").replace("Name", "\nName").replace("Age", "\nAge").replace("Gender", "\nGender").replace(":", "").replace("+", "").replace("Available", "\n").replace("Photo", "/n").replace("=","").replace("?", "")
                new_string = file_content.split("\n")

                Name=[]
                Father_Spouse_Name= []
                Age = []
                HouseN = []
                Gender = []
                ACNN = []
                Sonn = []
                Voter_ID = []
                frame = {}

                for i in range(len(new_string)):
                    
                    tokens= new_string[i]
                    if "Name" in tokens:
                        Name.append(tokens.replace("Name", ""))

                    if "FathersN" in tokens:
                        Father_Spouse_Name.append(tokens.replace("FathersN","")+" (Father)")

                    if "HusbandN" in tokens:
                        Father_Spouse_Name.append(tokens.replace("HusbandN", "")+" (Husband)")

                    if "Other" in tokens:
                        Father_Spouse_Name.append(tokens.replace("Other", "")+" (Others)")

                    if "Age" in tokens:
                        Age.append(tokens.replace("Age",""))

                    if "HouseN" in tokens:
                        HouseN.append(tokens.replace("HouseN", ""))

                    if "Gender" in tokens:
                        Gender.append(tokens.replace("Gender", ""))

                    if "ACNN" in tokens:
                        ACNN.append(tokens)
                    if "SNON" in tokens:
                        Sonn.append(tokens)

                if len(Name) == len(Age) == len(Father_Spouse_Name)==len(Gender)==len(HouseN) != 0:
                    frame = {"name": Name, "Father_spouse_name":Father_Spouse_Name,"HouseN":HouseN, "Age":Age, "Gender":Gender}
                    df = pd.DataFrame(frame)
                    if len(Sonn)!=0:
                        df["ward"] = Sonn[0]

                    
                    folder_path = to_excel_config.excel_folder_path
                    file_name = f"output{index}.csv"
                    full_path = os.path.join(folder_path, file_name)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    df.to_csv(full_path, index=False)
                    

            









                        
                        

