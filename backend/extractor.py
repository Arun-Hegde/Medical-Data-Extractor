from pdf2image import convert_from_path
import pytesseract
from backend.src import util
from backend.src.prescription_parser import PrescriptionParser
from backend.src.Patient_Details_Parser import PatientDetailsParser

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
POPLER_PATH= r'C:\poppler-24.08.0\Library\bin'

def extract(file_path,file_format):
    pages = convert_from_path(file_path,poppler_path=POPLER_PATH)

    document_text = ''

    if len(pages) > 0:
        page = pages[0]
        processed_image=util.preprocessing_image(page)
        text = pytesseract.image_to_string(processed_image, lang='eng')
        document_text = '\n' + text

    if file_format == 'prescription':
        extracted_data = PrescriptionParser(document_text).parse()
    elif file_format == 'patient_details':
        extracted_data = PatientDetailsParser(document_text).parse()
    else:
        raise Exception(f"Invalid File Format '{file_format}'")

    return extracted_data

if __name__ == '__main__':
    data = extract(r'..\resources\prescription\pre_1.pdf','prescription')
    print(data)