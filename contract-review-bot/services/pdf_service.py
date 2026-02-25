import fitz  
import logging
from io import BytesIO

logger = logging.getLogger(__name__)

def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """
    Extracts text from a provided PDF byte string using PyMuPDF (fitz).
    
    Args:
        pdf_bytes (bytes): The bytes content of the uploaded PDF file.
        
    Returns:
        str: The extracted full text of the document.
        
    Raises:
        ValueError: If PDF bytes are empty or invalid.
    """
    if not pdf_bytes:
        raise ValueError("Cannot extract text from empty file bytes.")
        
    full_text = ""
    try:
        
        pdf_document = fitz.open(stream=BytesIO(pdf_bytes), filetype="pdf")
        
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            text = page.get_text("text")
            full_text += text + "\n\n"
            
        pdf_document.close()
        
    except Exception as e:
        logger.error(f"Failed to read PDF file: {e}")
        raise ValueError(f"Failed to parse PDF document. It may be corrupt or encrypted. Details: {e}")
        
    return full_text.strip()