import streamlit as st
import requests
import base64
import json
from xhtml2pdf import pisa
from io import BytesIO

# FastAPI backend endpoint
API_URL = "http://127.0.0.1:8000/extract_from_doc"

# Set page config and styling
st.set_page_config(page_title="🩺 Medical Document Extractor", layout="centered", page_icon="🧾")

# Inject custom CSS for colors and layout
st.markdown("""
    <style>
    .main {
        background-color: #f0f4f7;
        padding: 2rem;
        border-radius: 12px;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        padding: 0.6rem 1.2rem;
        border: none;
        border-radius: 8px;
        font-size: 1rem;
    }
    .stRadio > div {
        background-color: #000000;
        border-radius: 8px;
        padding: 0.5rem;
    }
    .stFileUploader {
        background-color: #000000;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #cccccc;
    }
    </style>
""", unsafe_allow_html=True)

# Optional: Add a logo
logo_path = "logo.png"  # place a logo image in the same folder
try:
    with open(logo_path, "rb") as image_file:
        encoded_logo = base64.b64encode(image_file.read()).decode()
        st.markdown(f'<img src="data:image/png;base64,{encoded_logo}" width="120">', unsafe_allow_html=True)
except:
    pass

st.title("🩺 Medical Document Extractor")

st.markdown("""
Upload a medical PDF file — such as a **Prescription** or **Patient Details** — and extract meaningful information instantly.
""")

# File upload
uploaded_file = st.file_uploader("📄 Choose a PDF file", type="pdf")

# Select file format
file_format = st.radio("📑 Select document type:", ("prescription", "patient_details"))

# Submit button
if st.button("📤 Extract Data"):
    if uploaded_file is not None:
        with st.spinner("🔍 Extracting data, please wait..."):
            try:
                # Prepare the request
                files = {'file': (uploaded_file.name, uploaded_file.getvalue(), 'application/pdf')}
                data = {'file_format': file_format}

                # Send request to FastAPI
                response = requests.post(API_URL, files=files, data=data)

                if response.status_code == 200:
                    result = response.json()
                    st.success("✅ Data Extracted Successfully")

                    with st.container():
                        for key, value in result.items():
                            st.markdown(f"""
                            <div style='background-color:#ffffff; padding:15px; margin-bottom:10px; border-radius:10px; box-shadow:0 2px 8px rgba(0,0,0,0.05);'>
                                <h5 style='margin-bottom:5px; color:#4CAF50;'>{key.replace('_', ' ').title()}</h5>
                                <p style='margin:0; font-size:16px; color:#333;'>{value}</p>
                            </div>
                            """, unsafe_allow_html=True)


                    def generate_html_from_result(data):
                        html = "<h2>Extracted Medical Data</h2><br><hr>"
                        for key, value in data.items():
                            clean_val = str(value).replace("\n", "<br>")
                            html += f"<p><strong>{key.replace('_', ' ').title()}:</strong><br>{clean_val}</p><br>"
                        return html


                    # Convert HTML to PDF
                    def convert_html_to_pdf(source_html):
                        pdf_file = BytesIO()
                        pisa_status = pisa.CreatePDF(source_html, dest=pdf_file)
                        if pisa_status.err:
                            return None
                        return pdf_file.getvalue()


                    pdf_html = generate_html_from_result(result)
                    pdf_bytes = convert_html_to_pdf(pdf_html)

                    if pdf_bytes:
                        b64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
                        pdf_download_link = f'<a href="data:application/pdf;base64,{b64_pdf}" download="extracted_data.pdf">📄 Download Extracted Data as PDF</a>'
                        st.markdown(pdf_download_link, unsafe_allow_html=True)
                    else:
                        st.error("❌ Failed to generate PDF.")

                else:
                    st.error(f"❌ Server Error: {response.status_code}")
                    st.text(response.text)

            except Exception as e:
                st.error(f"❌ Extraction failed: {str(e)}")
    else:
        st.warning("⚠️ Please upload a file first.")
