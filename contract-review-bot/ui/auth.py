import streamlit as st
import time

from utils.auth_db import save_user, verify_credentials

def render_login_signup():
    """Renders the Login and Signup interface."""
    
    if "auth_mode" not in st.session_state:
        st.session_state.auth_mode = "login"
    
    if st.session_state.auth_mode == "login":
        render_login_form()
    else:
        render_signup_form()

def render_login_form():
    st.markdown("""
        <div class="auth-card">
            <div class="auth-logo">
                <svg width="60" height="60" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 2C10.8954 2 10 2.89543 10 4V5H14V4C14 2.89543 13.1046 2 12 2Z" fill="#5D5CDE"/>
                    <path d="M12 7C9.23858 7 7 9.23858 7 12V15C7 16.1046 7.89543 17 9 17H15C16.1046 17 17 16.1046 17 15V12C17 9.23858 14.7614 7 12 7Z" fill="#5D5CDE"/>
                    <path opacity="0.4" d="M12 7C14.7614 7 17 9.23858 17 12V15H7V12C7 9.23858 9.23858 7 12 7Z" fill="#5D5CDE"/>
                    <rect x="9" y="10" width="2" height="2" rx="1" fill="white"/>
                    <rect x="13" y="10" width="2" height="2" rx="1" fill="white"/>
                    <path d="M5 12H3V15C3 16.1046 3.89543 17 5 17H6" stroke="#5D5CDE" stroke-width="2" stroke-linecap="round"/>
                    <path d="M19 12H21V15C21 16.1046 20.1046 17 19 17H18" stroke="#5D5CDE" stroke-width="2" stroke-linecap="round"/>
                </svg>
            </div>
            <div class="auth-title">Welcome Back</div>
            <div class="auth-subtitle">Enter your credentials to access the contract portal.</div>
    """, unsafe_allow_html=True)
    
    with st.container():
        email = st.text_input("Email Address", placeholder="name@company.com", label_visibility="collapsed", key="login_email")
        password = st.text_input("Password", type="password", placeholder="Enter your password", label_visibility="collapsed", key="login_password")
        
        st.markdown('<div class="auth-button">', unsafe_allow_html=True)
        if st.button("Login →", use_container_width=True, key="login_btn"):
            if not email or not password:
                st.error("Please fill in all fields.")
            elif verify_credentials(email, password):
                from utils.persistent_auth import create_session
                token = create_session(email)
                
                st.query_params["session"] = token
                
                st.session_state.authenticated = True
                st.session_state.user_email = email
                st.success("Login successful!")
                time.sleep(0.5)
                st.rerun()
            else:
                st.error("Invalid credentials.")
        st.markdown('</div>', unsafe_allow_html=True)
                
        st.write("") 
        col_pad1, col1, col2, col_pad2 = st.columns([0.8, 3, 2, 0.8])
        with col1:
            st.markdown('<div style="text-align: right; color: #64748B; padding-top: 5px; padding-right: 5px; font-size: 0.95rem;">Don\'t have an account?</div>', unsafe_allow_html=True)
        with col2:
            if st.button("Sign up", key="to_signup", use_container_width=False):
                st.session_state.auth_mode = "signup"
                st.rerun()

def render_signup_form():
    st.markdown(f"""
        <div class="auth-card">
            <div class="auth-logo">
                <svg width="60" height="60" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="12" cy="12" r="10" stroke="#5D5CDE" stroke-width="2"/>
                    <path d="M12 8V16M8 12H16" stroke="#5D5CDE" stroke-width="2" stroke-linecap="round"/>
                </svg>
            </div>
            <div class="auth-title">Create Account</div>
            <div class="auth-subtitle">Join the professional legal intelligence platform.</div>
    """, unsafe_allow_html=True)
    
    with st.container():
        email = st.text_input("Email Address", placeholder="work@email.com", label_visibility="collapsed", key="reg_email")
        password = st.text_input("Password", type="password", placeholder="Minimum 6 characters", label_visibility="collapsed", key="reg_pass")
        confirm_password = st.text_input("Confirm Password", type="password", placeholder="Repeat password", label_visibility="collapsed", key="reg_confirm")
        
        st.markdown('<div class="auth-button">', unsafe_allow_html=True)
        if st.button("Register →", use_container_width=True, key="signup_btn"):
            if not email or not password or not confirm_password:
                st.error("Please fill in all fields.")
            elif password != confirm_password:
                st.error("Passwords do not match.")
            elif len(password) < 6:
                st.error("Password too short.")
            else:
                if save_user(email, password):
                    st.balloons()
                    st.success("Account created!")
                    time.sleep(1.5)
                    st.session_state.auth_mode = "login"
                    st.rerun()
                else:
                    st.warning("⚠️ Account already exists. Please log in.")
        st.markdown('</div>', unsafe_allow_html=True)
                     
        st.write("") 
        col_pad1, col1, col2, col_pad2 = st.columns([0.8, 3, 2, 0.8])
        with col1:
            st.markdown('<div style="text-align: right; color: #64748B; padding-top: 5px; padding-right: 5px; font-size: 0.95rem;">Already have an account?</div>', unsafe_allow_html=True)
        with col2:
            if st.button("Sign in", key="to_login", use_container_width=False):
                st.session_state.auth_mode = "login"
                st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)