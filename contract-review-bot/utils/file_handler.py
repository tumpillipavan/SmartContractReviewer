def get_uploaded_file_bytes(uploaded_file) -> bytes:
    """
    Safely reads bytes from a streamlit uploaded file object.
    
    Args:
        uploaded_file: The st.file_uploader return object.
        
    Returns:
        bytes: The files content bytes.
    """
    if uploaded_file is None:
        return b""
        
    file_bytes = uploaded_file.getvalue()
    return file_bytes