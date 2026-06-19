# Import the actual heavy-lifting function from our components folder
from components.pdf_handler import extract_text_from_pdf

def process_core_pdf(uploaded_file) -> str:
    """Passes the uploaded file to the main component extractor."""
    return extract_text_from_pdf(uploaded_file)