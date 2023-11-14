import os , sys

class ingestion_config:
        file_path = '2023-EROLLGEN-S29-61-FinalRoll-Revision1-ENG-4-WI.pdf'

class process_config:
        artifact = "artifact/images"
        
        custom_config = r'--oem 1 --psm 12'
class to_excel_config:
        path = "artifact/images"
        excel_folder_path = "artifact/excels"
           
         

        