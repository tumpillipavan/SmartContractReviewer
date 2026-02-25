import re

def sanitize_text(text: str) -> str:
    """
    Sanitizes raw extracted text from PDFs or user input:
    - Removes excessive whitespace
    - Removes non-printable characters
    - Normalizes line breaks
    - Removes suspected repeated page headers/footers (basic heuristic)
    """
    if not text:
        return ""

    text = re.sub(r'[^\x20-\x7E\n\t\r]', '', text)

    text = re.sub(r'\n{3,}', '\n\n', text)

    text = re.sub(r'[ \t]{2,}', ' ', text)

    lines = text.split("\n")
    cleaned_lines = []
    
    for line in lines:
        stripped = line.strip()
        
        if re.match(r'^(page\s*\d+|\d+)$', stripped, re.IGNORECASE):
            continue
        cleaned_lines.append(stripped)

    final_text = "\n".join(cleaned_lines)
    return final_text.strip()