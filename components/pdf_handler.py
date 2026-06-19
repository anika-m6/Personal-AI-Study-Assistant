import PyPDF2

def extract_text_from_pdf(uploaded_file) -> str:
    """
    Takes an uploaded PDF file from Streamlit, loops through its pages, 
    and extracts all readable text characters into a single string.
    """
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        extracted_text = ""
        
        # Loop through every page sequentially
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                extracted_text += page_text + "\n"
                
        return extracted_text.strip()
    except Exception as e:
        return f"Error reading PDF: {str(e)}"