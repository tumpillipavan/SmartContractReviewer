import streamlit as st
import logging

st.set_page_config(
    page_title="AI Contract Intelligence",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

from ui.styles import inject_global_styles
inject_global_styles()
st.markdown('<div class="branding-spotlight">INVISI EDGE</div>', unsafe_allow_html=True)

from ui.layout import render_sidebar
from ui.components import render_hero_section, render_input_area
from ui.report_display import display_analysis_report

from analysis.confidence_validator import validate_and_display_confidence
from middleware.exception_handler import handle_exceptions
from middleware.text_sanitizer import sanitize_text
from middleware.prompt_injection_guard import scan_for_prompt_injection

from utils.file_handler import get_uploaded_file_bytes
from services.pdf_service import extract_text_from_pdf
from services.gemini_service import analyze_contract

from analysis.prompt_builder import generate_analysis_prompt
from analysis.risk_analyzer import scan_for_manual_risks
from analysis.score_calculator import calculate_final_risk_score

if 'token_count' not in st.session_state: st.session_state.token_count = 0
if 'report_count' not in st.session_state: st.session_state.report_count = 0
if 'analysis_history' not in st.session_state: 
    from utils.history_db import load_history
    st.session_state.analysis_history = load_history()
if 'pending_analysis' not in st.session_state: st.session_state.pending_analysis = False
if 'last_input_hash' not in st.session_state: st.session_state.last_input_hash = None
if 'current_report' not in st.session_state: st.session_state.current_report = None
if 'current_score' not in st.session_state: st.session_state.current_score = None
if 'authenticated' not in st.session_state: st.session_state.authenticated = False
if 'user_email' not in st.session_state: st.session_state.user_email = None

@handle_exceptions("An unexpected error occurred while analyzing the contract. Our team has been notified.")
def process_contract_analysis(raw_text: str):
    """
    Orchestrates the pipeline: Sanitize -> Injection Guard -> Manual Scan -> Gemini AI -> Display.
    """
    logger = logging.getLogger(__name__)

    st.session_state.last_raw_text = raw_text
    personality = st.session_state.get('personality', 'Neutral Summarizer')
    sensitivity = st.session_state.get('sensitivity', 75)

    with st.status("✨ Extracting Intelligence from Document...", expanded=True) as status:
        st.write("🔍 Sanitizing and prepping text...")
        clean_text = sanitize_text(raw_text)
        
        if not clean_text:
            st.warning("No valid text found to analyze.")
            status.update(label="Analysis Aborted: No valid text.", state="error")
            return

        est_tokens = len(clean_text) // 4
        st.session_state.token_count += est_tokens
        
        st.write("🛡️ Running deep security checks...")
        is_injected = scan_for_prompt_injection(clean_text)
        if is_injected:
            st.error("🚨 Security injection detected!")

        st.write("🧠 AI Analyst is thinking...")
        manual_risks = scan_for_manual_risks(clean_text)
        prompt = generate_analysis_prompt(clean_text, personality=personality, sensitivity=sensitivity)
        report_data = analyze_contract(prompt)
        
        status.update(label="✅ Intelligence Extraction Complete!", state="complete", expanded=False)

    st.session_state.pending_analysis = False
    st.session_state.report_count += 1

    ai_risk_score = report_data.get("overall_risk_score", 0)
    final_risk_score = calculate_final_risk_score(ai_risk_score, manual_risks)
    
    history_entry = {
        "name": report_data.get("contract_type", "Unnamed Agreement"),
        "score": final_risk_score,
        "data": report_data,
        "timestamp": "Just now"
    }
    st.session_state.analysis_history.append(history_entry)
    st.session_state.current_report = report_data
    st.session_state.current_score = final_risk_score

    from utils.history_db import save_history
    save_history(st.session_state.analysis_history)

    st.toast("Analysis Complete! 🎉", icon='✅')
    
    st.rerun()

def main():
    inject_global_styles()
    
    if "session" in st.query_params and not st.session_state.authenticated:
        token = st.query_params["session"]
        try:
            from utils.persistent_auth import validate_session
            email = validate_session(token)
            if email:
                st.session_state.authenticated = True
                st.session_state.user_email = email
            else:
                
                st.query_params.clear()
        except Exception as e:
            
            st.query_params.clear()

    if not st.session_state.authenticated:
        from ui.auth import render_login_signup
        render_login_signup()
        return
    
    render_sidebar()
    render_hero_section()
    
    uploaded_file, pasted_text = render_input_area()
    
    current_input_hash = hash(str(uploaded_file.name if uploaded_file else "") + pasted_text)
    if current_input_hash != st.session_state.last_input_hash:
        if uploaded_file or pasted_text.strip():
            st.session_state.pending_analysis = True
        else:
            st.session_state.pending_analysis = False
        st.session_state.last_input_hash = current_input_hash
        st.rerun()

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        analyze_btn = st.button("🚀 Analyze Contract", use_container_width=True, type="primary", key="analyze_button")

    if analyze_btn:
        raw_text = ""
        
        if uploaded_file is not None:
            file_bytes = get_uploaded_file_bytes(uploaded_file)
            try:
                with st.spinner("Parsing PDF content..."):
                    raw_text = extract_text_from_pdf(file_bytes)
            except Exception as e:
                st.error(f"Could not parse the PDF file. Details: {e}")
                return
        
        elif pasted_text.strip():
            raw_text = pasted_text
        else:
            st.warning("Please upload a PDF or paste contract text to begin analysis.")
            return

        process_contract_analysis(raw_text)

    if st.session_state.current_report:
        st.markdown("---")
        
        display_analysis_report(
            st.session_state.current_report, 
            st.session_state.get('current_score', 0)
        )

    if not st.session_state.get('sidebar_auto_expanded_this_login', False):
        st.session_state['sidebar_auto_expanded_this_login'] = True
        st.components.v1.html(
            """
            <script>
            function forceOpenSidebar() {
                try {
                    // Search for Streamlit's native 'closed sidebar' generic container and button
                    let expandBtn = window.parent.document.querySelector('[data-testid="collapsedControl"]');
                    if (!expandBtn) {
                        expandBtn = window.parent.document.querySelector('.stSidebarCollapsedControl');
                    }
                    if (!expandBtn) {
                         // Most aggressive fallback: Find any button floating top-left (our CSS position)
                         let buttons = window.parent.document.querySelectorAll('button');
                         for(let btn of buttons) {
                             let rect = btn.getBoundingClientRect();
                             if(rect.top < 30 && rect.left < 30 && rect.width > 20) {
                                  expandBtn = btn;
                                  break;
                             }
                         }
                    }

                    if (expandBtn) {
                        // If it's closed, aggressively click it open!
                        if(window.parent.document.body.dataset.sidebarForced !== 'true') {
                            expandBtn.click();
                            window.parent.localStorage.setItem('sidebarState', 'expanded');
                            window.parent.document.body.dataset.sidebarForced = 'true';
                        }
                    }
                } catch (e) {}
            }
            
            // Fire multiple times aggressively to beat Streamlit's asynchronous shadow DOM rendering
            forceOpenSidebar();
            setTimeout(forceOpenSidebar, 100);
            setTimeout(forceOpenSidebar, 300);
            setTimeout(forceOpenSidebar, 500);
            setTimeout(forceOpenSidebar, 1000);
            </script>
            """,
            height=0,
        )

if __name__ == "__main__":
    main()