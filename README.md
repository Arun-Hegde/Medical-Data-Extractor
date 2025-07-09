# 🩺 Medical Document Extractor

A Python-based tool that extracts structured information from medical PDF documents such as **Prescriptions** and **Patient Records** using OCR (Tesseract), OpenCV, and regex.

Built using:
- 🧠 **FastAPI** for backend API
- 💻 **Streamlit** for frontend interface
- 📄 **Tesseract-OCR** + **Poppler** for PDF image conversion and text extraction

---

## 📁 Project Structure

```
Project-Medical-Data-Extraction/
├── backend/
│   ├── src/
│   │   ├── main.py                   # FastAPI app
│   │   ├── extractor.py              # Image → text → parse
│   │   ├── parser_generic.py         # Abstract parser class
│   │   ├── prescription_parser.py    # Prescription parser
│   │   ├── patient_details_parser.py # Patient info parser
│   │   ├── util.py                   # Preprocessing functions
│   ├── test/
│   │   ├── test_prescription_parser.py
│   │   └── test_patient_details_parser.py
│   ├── uploads/                      # Temporary uploaded files
│   └── resources/
│       ├── prescription/             # Sample prescriptions
│       └── patient_details/          # Sample patient details
├── frontend/
│   └── app.py                        # Streamlit UI app
├── screenshots/
│   └── ui_screenshot.png             # UI preview
├── logo.png                          # Optional app logo
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run the Project

### 📥 Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/medical-document-extractor.git
cd medical-document-extractor
```

### 📦 Step 2: Install Python Dependencies

Make sure Python 3.10+ is installed. Then run:

```bash
pip install -r requirements.txt
```

### 🔤 Step 3: Install Tesseract & Poppler

#### ✅ Tesseract-OCR

- Download: https://github.com/tesseract-ocr/tesseract/wiki
- Set path in code (inside `extractor.py`):

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

#### ✅ Poppler for Windows

- Download: https://blog.alivate.com.au/poppler-windows/
- Set Poppler path in code:

```python
POPPLER_PATH = r"C:\path\to\poppler\bin"
```

---

## ▶️ Run the Application

### 🖥️ Start Backend (FastAPI)

```bash
cd backend/src
uvicorn main:app --reload
```

### 🌐 Start Frontend (Streamlit in new terminal)

```bash
cd frontend
streamlit run app.py
```

---

## 🧪 Testing (Optional)

To run tests for the parsers:

```bash
cd backend/test
pytest
```

---

## 💾 Sample Files

Use these sample PDFs for testing:

```
backend/resources/prescription/
backend/resources/patient_details/
```

---

## 📤 Output

- ✅ Data is shown in a clean, styled card format on the frontend
- 💾 Download options:
  - `extracted_data.json`
  - `extracted_data.pdf`

---


---

## 🙋‍♂️ Author

Developed by **Arun Hegde**  
📎 [GitHub Profile](https://github.com/Arun-Hegde)

Feel free to ⭐ the repo or connect on GitHub!

---