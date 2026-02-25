import streamlit as st

def render_hero_section():
    """
    Renders the Premium Hero Section with high-contrast gradient typography.
    """
    st.markdown("""
        <div style='text-align: center; padding: 1.5rem 0;'>
            <h1 class="hero-title">AI Contract Intelligence</h1>
            <p class="hero-subtitle">
                Upload an agreement to instantly extract terms, spot risks, and generate actionable summaries.
            </p>
        </div>
    """, unsafe_allow_html=True)

def render_input_area():
    """
    Renders the tabs for PDF Upload and Raw Text paste in a styled container.
    Returns:
        uploaded_file, text_input (both can be None or populated)
    """
    st.markdown('<h3 style="margin-top:0">🖋️ Input Document</h3>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["📄 Upload PDF", "✏️ Paste Text"])
    
    uploaded_file = None
    pasted_text = ""
    
    with tab1:
        uploaded_file = st.file_uploader("Upload your contract PDF", type=["pdf"])
        
    with tab2:
        pasted_text = st.text_area("Or copy and paste raw contract text here", height=200)
    
    return uploaded_file, pasted_text