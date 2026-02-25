import streamlit as st
from services.api_status_service import check_api_connection
from config.settings import MODEL_NAME

def render_sidebar():
    """
    Renders the production-grade interactive sidebar utility belt.
    """
    
    if 'token_count' not in st.session_state: st.session_state.token_count = 0
    if 'report_count' not in st.session_state: st.session_state.report_count = 0
    if 'analysis_history' not in st.session_state: st.session_state.analysis_history = []
    
    with st.sidebar:
        
        st.markdown('<div class="sidebar-title">🛡️ Secure Core</div>', unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown('<div class="sidebar-label">📊 System Health</div>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            
            with st.spinner("Ping..."):
                from services.api_status_service import ping_gemini_api
                api_active = ping_gemini_api()
            
            with col1:
                if api_active:
                    st.markdown(f"""
                        <div class="status-pill status-pill-success">
                            <svg class="pulse" width="12" height="12" viewBox="0 0 24 24" fill="currentColor" style="margin-right: 6px;">
                                <circle cx="12" cy="12" r="10" fill="#059669"/>
                            </svg>
                            API Live
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown('<div class="status-pill status-pill-error">API Offline</div>', unsafe_allow_html=True)
            with col2:
                if st.session_state.get('pending_analysis', False):
                    st.markdown(f"""
                        <div class="status-pill status-pill-standby">
                            <svg class="pulse" width="12" height="12" viewBox="0 0 24 24" fill="currentColor" style="margin-right: 6px;">
                                <circle cx="12" cy="12" r="10" fill="#0D9488"/>
                            </svg>
                            Thinking
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown('<div class="status-pill status-pill-info">Guard Active</div>', unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown('<div class="sidebar-label">⚙️ Analysis Settings</div>', unsafe_allow_html=True)
            st.session_state.personality = st.selectbox(
                "Analyst Personality", 
                ["Aggressive Auditor", "Neutral Summarizer", "Risk-Focused Scout"],
                help="Changes how the AI interprets and prioritizes contract language."
            )
            
            st.session_state.sensitivity = st.slider(
                "Risk Sensitivity", 
                0, 100, 75,
                help="Higher sensitivity flags minor nuances as risks."
            )
            
            slider_color = "#10B981" 
            if st.session_state.sensitivity > 40: slider_color = "#F59E0B" 
            if st.session_state.sensitivity > 75: slider_color = "#EF4444" 
            
            st.markdown(f"""
                <style>
                    div[data-testid="stSlider"] [data-baseweb="slider"] > div:first-child > div:first-child {{
                        background: linear-gradient(to right, {slider_color} {st.session_state.sensitivity}%, #E2E8F0 {st.session_state.sensitivity}%) !important;
                    }}
                </style>
            """, unsafe_allow_html=True)
            
            st.toggle("Deep Privacy Masking", value=True)

        with st.container(border=True):
            st.markdown('<div class="sidebar-label">📈 Session Analytics</div>', unsafe_allow_html=True)
            m_col1, m_col2, m_col3 = st.columns(3)
            with m_col1:
                st.metric("Tokens", f"{st.session_state.token_count}")
            with m_col2:
                st.metric("Reports", f"{st.session_state.report_count}")
            with m_col3:
                pending_count = 1 if st.session_state.get('pending_analysis', False) else 0
                st.metric("Pending", f"{pending_count}")

        if st.session_state.analysis_history:
            st.markdown('<div class="sidebar-label">🕒 Recent History</div>', unsafe_allow_html=True)
            for i, entry in enumerate(st.session_state.analysis_history[::-1]): 
                h_col1, h_col2 = st.columns([8, 1])
                with h_col1:
                    if st.button(f"📄 {entry['name']}", key=f"open_hist_{i}", use_container_width=True):
                        st.session_state.current_report = entry['data']
                        st.session_state.current_score = entry['score']
                        st.toast(f"Opening {entry['name']}...")
                        st.rerun()
                with h_col2:
                    
                    real_idx = len(st.session_state.analysis_history) - 1 - i
                    if st.button("🗑️", key=f"del_hist_{i}", help="Delete from history", use_container_width=True):
                        deleted_name = st.session_state.analysis_history.pop(real_idx)['name']
                        
                        from utils.history_db import save_history
                        save_history(st.session_state.analysis_history)
                        
                        if st.session_state.current_report == entry['data']:
                            st.session_state.current_report = None
                            st.session_state.current_score = None
                        
                        st.toast(f"Removed {deleted_name}")
                        st.rerun()
        
        st.markdown("<br/>", unsafe_allow_html=True)
        if st.button("🗑️ Clear Session Data", use_container_width=True):
            from utils.history_db import save_history
            save_history([])
            st.session_state.clear()
            st.rerun()

        st.markdown("---")
        if st.button("🚪 Sign Out", use_container_width=True, type="primary"):
            
            from utils.persistent_auth import destroy_session
            if "session" in st.query_params:
                destroy_session(st.query_params["session"])
                st.query_params.clear()
            
            st.session_state.authenticated = False
            st.session_state.user_email = None
            st.rerun()
            
        st.markdown(f"""
            <div class="sidebar-footer">
                <div class="model-tag">🤖 {MODEL_NAME}</div><br/>
                Enterprise Review Bot • v1.2.0-beta<br/>
                © 2026 Secure Core AI
            </div>
        """, unsafe_allow_html=True)