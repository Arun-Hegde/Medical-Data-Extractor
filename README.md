# 🩺 Medical Document Extractor

A modular Python-based application that extracts structured data from **medical PDFs** such as **prescriptions** and **patient records** using OCR and custom regex parsing. Users can upload a file through a clean Streamlit interface and download the results in **PDF or JSON** format.

---

## ✅ Features

- 🔍 Extracts key data from PDFs (name, address, medicines, etc.)
- 📤 Upload your own PDF files through UI
- 🧠 OCR-based text recognition (Tesseract)
- 📄 Download extracted data in **PDF** and **JSON** formats
- ⚡ Fast and responsive backend with FastAPI
- 🖥️ Beautiful interactive frontend built using Streamlit
- 📁 Includes test cases and sample PDF data

---

## 🚀 Tech Stack

| Component   | Technology       |
|-------------|------------------|
| Frontend    | Streamlit        |
| Backend     | FastAPI          |
| OCR Engine  | Tesseract        |
| Image Utils | OpenCV, NumPy    |
| Language    | Python 3.10+     |
| Testing     | Pytest           |

---

## 📂 Project Structure

Project-Medical-Data-Extraction/
├── backend/ 
│ ├── src/ 
│ │ ├── main.py # FastAPI app 
│ │ ├── extractor.py # Image → text → parse  
│ │ ├── parser_generic.py # Abstract parser class 
│ │ ├── prescription_parser.py # Prescription data parser 
│ │ ├── patient_details_parser.py# Patient details parser 
│ │ ├── util.py # Preprocessing (OpenCV) 
│ ├── test/ 
│ │ ├── test_prescription_parser.py 
│ │ └── test_patient_details_parser.py 
│ ├── uploads/ # Temp upload files (auto) 
│ └── resources/ 
│ ├── prescription/ # Sample PDFs 
│ └── patient_details/ 
├── frontend/ 
│ └── app.py # Streamlit app 
├── screenshots/ 
│ └── ui_screenshot.png # UI screenshot 
├── logo.png # (optional) app logo 
├── requirements.txt 
└── README.md 


## 🖼️ UI Preview

> Upload PDF ➜ Extract ➜ View ➜ Download PDF


## 🛠️ Setup Instructions

### 🔧 Step 1: Clone the repository

git clone https://github.com/your-username/medical-document-extractor.git
cd medical-document-extractor

📦 Step 2: Install Python dependencies
Make sure Python 3.10+ is installed. Then run:
pip install -r requirements.txt

🔤 Step 3: Install Tesseract & Poppler
Tesseract:
Download for Windows
Set path in code:
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
Poppler for Windows:
Download here
Set poppler_path in code:

POPPLER_PATH = r"C:\path\to\poppler\bin"
▶️ Run the Application
🖥️ Start FastAPI Backend

cd backend/src
uvicorn main:app --reload
🌐 Start Streamlit Frontend (new terminal)

cd frontend
streamlit run app.py
🧪 Testing (Optional)

cd backend/test
pytest
💾 Sample Files
You can test using the sample PDFs in:

backend/resources/prescription/

backend/resources/patient_details/

📤 Output
Extracted data shown in a clean card format in the frontend.

Data can be downloaded as:

extracted_data.json

extracted_data.pdf

🙋‍♂️ Author
Developed by Arun Hegde
Let’s connect on [Arun-Hegde]
