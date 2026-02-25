import streamlit as st

def inject_global_styles():
    """
    Injects custom CSS to achieve the Glassmorphism SaaS aesthetic.
    """
    st.markdown("""
        <style>
        
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif !important;
        }

        ::-webkit-scrollbar {
            display: none !important;
        }
        html, body, .stApp {
            scrollbar-width: none !important;
            -ms-overflow-style: none !important;
            overflow: hidden !important; 
            height: 100vh !important;
        }
        
        .stApp {
            background: 
                radial-gradient(at 0% 0%, rgba(93, 92, 222, 0.05) 0px, transparent 50%),
                radial-gradient(at 100% 0%, rgba(16, 185, 129, 0.05) 0px, transparent 50%),
                radial-gradient(at 100% 100%, rgba(93, 92, 222, 0.05) 0px, transparent 50%),
                radial-gradient(at 0% 100%, rgba(16, 185, 129, 0.05) 0px, transparent 50%),
                #F8FAFC !important;
            color: #475569;
        }
        
        header[data-testid="stHeader"] {
            background-color: transparent !important;
            border-bottom: 1px solid rgba(226, 232, 240, 0.5) !important;
            backdrop-filter: blur(8px);
            z-index: 99 !important;
        }

        [data-testid="stAppDeployButton"], 
        [data-testid="stMainMenu"],
        [data-testid="stStatusWidget"],
        .stAppDeployButton {
            display: none !important;
        }

        iframe[title="st.iframe"] {
            display: none !important;
            height: 0px !important;
            margin: 0px !important;
            padding: 0px !important;
        }

        .branding-spotlight {
            position: fixed;
            top: 12px;
            left: 70px;
            z-index: 1001;
            padding: 8px 16px;
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(13, 148, 136, 0.2);
            border-left: 4px solid #0D9488;
            border-radius: 8px;
            color: #0F172A;
            font-weight: 700;
            font-size: 14px;
            letter-spacing: 0.05em;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            display: flex;
            align-items: center;
            gap: 8px;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .branding-spotlight:hover {
            background: rgba(255, 255, 255, 0.9);
            border-color: #0D9488;
            box-shadow: 0 8px 20px rgba(13, 148, 136, 0.15);
            transform: translateY(-1px);
        }

        .branding-spotlight::before {
            content: '💎';
            font-size: 12px;
        }

        [data-testid="collapsedControl"],
        .stSidebarCollapsedControl {
            position: fixed !important;
            top: 12px !important;
            left: 12px !important;
            right: auto !important;
            z-index: 1000 !important;
        }

        [data-testid="collapsedControl"] button,
        .stSidebarCollapsedControl button,
        button[data-testid="stExpandSidebarButton"] {
            visibility: visible !important;
            display: flex !important;
            background-color: #ffffff !important;
            border: 1px solid #CBD5E1 !important;
            border-radius: 8px !important;
            width: 40px !important;
            height: 40px !important;
            justify-content: center !important;
            align-items: center !important;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1) !important;
            transition: all 0.2s ease !important;
        }

        [data-testid="collapsedControl"] button:hover,
        .stSidebarCollapsedControl button:hover,
        button[data-testid="stExpandSidebarButton"]:hover {
            background-color: #F1F5F9 !important;
            border-color: #94A3B8 !important;
            transform: translateY(-1px);
        }

        [data-testid="stSidebar"] button[kind="header"] {
            background-color: #ffffff !important;
            border: 1px solid #CBD5E1 !important;
            border-radius: 6px !important;
            width: 32px !important;
            height: 32px !important;
            margin-bottom: 12px !important;
        }

        .block-container {
            padding: 1rem 3.5rem !important; 
            max-width: 1100px !important;
            margin: auto !important;
        }

        [data-testid="baseButton-secondary"], 
        [data-testid="baseButton-primary"] {
            background-color: #0D9488 !important;
            color: #ffffff !important;
            border: 1px solid #0D9488 !important;
            font-weight: 600 !important;
            border-radius: 8px !important;
            transition: all 0.2s ease !important;
        }
        
        [data-testid="baseButton-secondary"]:hover,
        [data-testid="baseButton-primary"]:hover {
            background-color: #0F766E !important; 
            border: 1px solid #0F766E !important;
            box-shadow: 0 8px 20px rgba(13, 148, 136, 0.3) !important;
            transform: translateY(-2px);
        }

        button[kind="primaryFormSubmit"],
        [data-testid="stButton"] button[kind="primary"] {
            background: linear-gradient(135deg, #FF4B4B 0%, #E63946 100%) !important;
            border: none !important;
            height: 3.5rem !important;
            font-size: 1.15rem !important;
            font-weight: 700 !important;
            border-radius: 12px !important;
            box-shadow: 0 4px 10px rgba(255, 75, 75, 0.2) !important;
            margin-top: 10px !important;
            
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        }
        
        button[kind="primaryFormSubmit"]:hover,
        [data-testid="stButton"] button[kind="primary"]:hover {
            
            box-shadow: 0 16px 36px rgba(255, 75, 75, 0.4) !important;
            transform: translateY(-8px) scale(1.02) !important;
        }

        button[kind="primaryFormSubmit"]:active,
        [data-testid="stButton"] button[kind="primary"]:active {
            
            transform: translateY(2px) scale(0.98) !important;
            box-shadow: 0 2px 8px rgba(255, 75, 75, 0.2) !important;
        }

        div[data-testid="stProgress"] > div > div > div {
            background-color: #0D9488 !important;
        }

        .hero-title {
            font-size: 3.5rem !important;
            font-weight: 800 !important;
            background: linear-gradient(135deg, #5D5CDE 0%, #0D9488 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem !important;
            letter-spacing: -0.02em;
        }

        .hero-subtitle {
            color: #64748B !important;
            font-size: 1.2rem !important;
            font-weight: 400 !important;
            margin-bottom: 2.5rem !important;
            opacity: 0.8;
        }

        .glass-card {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.4);
            border-radius: 16px;
            padding: 20px; 
            margin-bottom: 12px; 
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.03);
            transition: all 0.3s ease;
        }
        
        .glass-card:hover {
            border-color: rgba(93, 92, 222, 0.3);
            box-shadow: 0 12px 40px rgba(93, 92, 222, 0.08);
            transform: translateY(-2px);
        }
        
        .stTextArea textarea, .stTextInput input {
            color: #1E293B !important;
            background-color: #ffffff !important;
            border: 1px solid #CBD5E1 !important;
        }

        [data-testid="stFileUploadDropzone"] {
            background-color: #ffffff !important;
            border: 1px dashed #94A3B8 !important;
        }
        
        [data-testid="stFileUploadDropzone"] div, 
        [data-testid="stFileUploadDropzone"] span {
            color: #475569 !important;
        }
        
        [data-testid="stTabs"] [data-baseweb="tab-list"] {
            gap: 12px !important;
            background: rgba(241, 245, 249, 0.5) !important;
            padding: 6px !important;
            border-radius: 12px !important;
            border: 1px solid #E2E8F0 !important;
        }

        [data-testid="stTabs"] button {
            color: #64748b !important;
            border: none !important;
            border-radius: 8px !important;
            background: transparent !important;
            transition: all 0.2s ease !important;
        }

        [data-testid="stTabs"] button[aria-selected="true"] {
            color: #5D5CDE !important;
            background: #ffffff !important;
            box-shadow: 0 4px 12px rgba(93, 92, 222, 0.1) !important;
            font-weight: 600 !important;
        }
        
        label, div[class*="stWidgetLabel"] p, div[class*="stWidgetLabel"] span {
            color: #1E293B !important;
            font-weight: 500 !important;
        }
        
        .stMarkdown p, .stMarkdown span {
            color: #475569 !important;
        }
        
        h1, h2, h3, h4 {
            color: #1E293B !important;
        }

        [data-testid="stSidebar"] {
            background-color: #F8FAFC !important;
            border-right: 1px solid #E2E8F0;
        }
        
        div[data-testid="metric-container"] {
            background: #ffffff;
            border: 1px solid #E2E8F0;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            transition: transform 0.2s ease;
        }
        
        div[data-testid="metric-container"]:hover {
            transform: translateY(-4px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        }

        .metric-spotlight {
            border-left: 4px solid #0D9488 !important;
        }

        .chart-container {
            background: #ffffff;
            border: 1px solid #E2E8F0;
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 2rem;
            box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
        }
        
        div[data-testid="metric-container"] > div {
            color: #0D9488 !important; 
            font-weight: 700 !important;
        }
        div[data-testid="metric-container"] label {
            color: #64748B !important; 
        }
        
        .streamlit-expanderHeader {
            background-color: #F1F5F9 !important;
            border-radius: 6px !important;
            color: #1E293B !important;
            border: 1px solid #E2E8F0 !important;
        }

        .badge {
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.8em;
            font-weight: 600;
            display: inline-block;
            margin-bottom: 8px;
        }
        
        .badge-info { background: #DBEAFE; color: #1D4ED8; border: 1px solid #BFDBFE; }
        .badge-warning { background: #FEF3C7; color: #B45309; border: 1px solid #FDE68A; }
        .badge-danger { background: #FEE2E2; color: #B91C1C; border: 1px solid #FECACA; }
        .badge-success { background: #D1FAE5; color: #047857; border: 1px solid #A7F3D0; }
        
        .status-pill {
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 48px;
            width: 100%;
            border-radius: 8px;
            font-size: 0.85rem;
            font-weight: 600;
            padding: 4px 8px;
            text-align: center;
            line-height: 1.2;
        }
        
        .status-pill-success { background-color: #D1FAE5; color: #065F46; border: 1px solid #A7F3D0; }
        .status-pill-error { background-color: #FEE2E2; color: #991B1B; border: 1px solid #FECACA; }
        .status-pill-info { background-color: #DBEAFE; color: #1E40AF; border: 1px solid #BFDBFE; }
        
        .status-pill-standby {
            background-color: #F0FDFA;
            color: #0D9488;
            border: 1px solid #CCFBF1;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(13, 148, 136, 0.4); }
            70% { transform: scale(1.02); box-shadow: 0 0 0 10px rgba(13, 148, 136, 0); }
            100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(13, 148, 136, 0); }
        }
        
        .sidebar-title {
            font-size: 1.5rem !important;
            font-weight: 800 !important;
            background: linear-gradient(135deg, #0D9488 0%, #10B981 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1.5rem !important;
        }

        .sidebar-label {
            color: #64748B !important;
            font-size: 0.75rem !important;
            font-weight: 700 !important;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 0.5rem !important;
        }

        [data-testid="stSidebar"] button[key^="open_hist_"] {
            background-color: #ffffff !important;
            border: 1px solid #E2E8F0 !important;
            color: #475569 !important;
            text-align: left !important;
            padding: 0.75rem !important;
            border-radius: 8px !important;
            width: 100% !important;
            transition: all 0.2s ease !important;
            display: block !important;
            margin-bottom: 0.5rem !important;
        }

        [data-testid="stSidebar"] button[key^="open_hist_"] div[data-testid="stMarkdownContainer"] p {
            white-space: nowrap !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
            margin: 0 !important;
            width: 100% !important;
            display: block !important;
        }

        [data-testid="stSidebar"] button[key^="open_hist_"]:hover {
            border-color: #0D9488 !important;
            color: #0D9488 !important;
            background-color: #F0FDFA !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05) !important;
            transform: translateX(4px);
        }

        [data-testid="stSidebar"] div[data-testid="column"]:nth-of-type(2) button {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            padding: 0.75rem 0 !important;
            background-color: #ffffff !important;
            border: 1px solid #E2E8F0 !important;
            border-radius: 8px !important;
            transition: all 0.2s ease !important;
            width: 100% !important;
        }

        [data-testid="stSidebar"] div[data-testid="column"]:nth-of-type(2) button div,
        [data-testid="stSidebar"] div[data-testid="column"]:nth-of-type(2) button p {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            margin: auto !important;
            width: 100% !important;
            text-align: center !important;
        }

        [data-testid="stSidebar"] div[data-testid="column"]:nth-of-type(2) button:hover {
            background-color: #FEE2E2 !important;
            border-color: #EF4444 !important;
            color: #B91C1C !important;
            transform: scale(1.05);
        }

        [data-testid="stSidebar"] [data-testid="stSelectbox"] > div[data-baseweb="select"] > div {
            background-color: #ffffff !important;
            border-radius: 8px !important;
        }
        
        [data-testid="stSidebar"] [data-testid="stSlider"] [data-testid="stThumb"] {
            background-color: #0D9488 !important;
        }

        .sidebar-footer {
            margin-top: 2rem;
            padding-top: 1rem;
            border-top: 1px solid #E2E8F0;
            color: #94A3B8 !important;
            font-size: 0.7rem !important;
            text-align: center;
        }

        .model-tag {
            background: #F1F5F9;
            color: #475569 !important;
            padding: 2px 8px;
            border-radius: 4px;
            font-family: monospace;
            display: inline-block;
            margin-bottom: 4px;
        }
        
        [data-testid="stDropzone"] {
            border: 2px dashed #CBD5E1 !important;
            border-radius: 12px !important;
            background-color: #F8FAFC !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            cursor: pointer !important;
        }

        [data-testid="stDropzone"]:hover {
            border-color: #0D9488 !important;
            background-color: #F0FDFA !important;
            box-shadow: 0 4px 15px rgba(13, 148, 136, 0.1) !important;
            transform: translateY(-2px);
        }

        [data-testid="stDropzone"] button {
            background-color: transparent !important;
            border: 1px solid #0D9488 !important;
            color: #0D9488 !important;
            font-weight: 600 !important;
            transition: all 0.2s ease !important;
        }

        [data-testid="stDropzone"] button:hover {
            background-color: #0D9488 !important;
            color: white !important;
            box-shadow: 0 4px 10px rgba(13, 148, 136, 0.2) !important;
            transform: scale(1.02);
        }

        .auth-card {
            max-width: 400px;
            margin: 20px auto; 
            background: #ffffff;
            border-radius: 24px;
            padding: 30px; 
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.05);
            text-align: center;
            border: 1px solid #F1F5F9;
        }

        .auth-logo {
            margin-bottom: 12px; 
            display: inline-block;
        }

        .auth-title {
            color: #5D5CDE !important;
            font-size: 1.8rem !important; 
            font-weight: 800 !important;
            margin-bottom: 0.25rem !important; 
            letter-spacing: -0.02em;
        }

        .auth-subtitle {
            color: #94A3B8 !important;
            font-size: 0.95rem !important; 
            margin-bottom: 1.5rem !important; 
        }

        .auth-button button {
            background: #5D5CDE !important;
            color: #ffffff !important;
            border-radius: 12px !important;
            height: 3rem !important; 
            font-weight: 700 !important;
            font-size: 1.1rem !important;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            border: none !important;
        }

        .auth-button button:hover {
            background: #4B4ACD !important;
            transform: scale(1.02) !important;
            box-shadow: 0 8px 25px rgba(93, 92, 222, 0.3) !important;
        }

        div[class*="st-key-to_"] {
            display: flex;
            align-items: center;
        }

        div[class*="st-key-to_"] button {
            background: transparent !important;
            border: none !important;
            color: #5D5CDE !important;
            font-weight: 600 !important;
            padding: 0 !important;
            margin: 0 !important;
            min-height: auto !important;
            height: auto !important;
            line-height: normal !important;
            box-shadow: none !important;
            font-size: 0.95rem !important; 
        }

        div[class*="st-key-to_"] button:hover {
            text-decoration: underline !important;
            transform: none !important;
            box-shadow: none !important;
            color: #4B4ACD !important;
        }

        [data-testid="stSlider"] [data-testid="stTickBar"] {
            display: none !important;
        }

        .shimmer {
            background: linear-gradient(
                90deg,
                rgba(93, 92, 222, 0.05) 25%,
                rgba(93, 92, 222, 0.1) 50%,
                rgba(93, 92, 222, 0.05) 75%
            );
            background-size: 200% 100%;
            animation: shimmer-swipe 1.5s infinite linear;
            border-radius: 8px;
        }

        @keyframes shimmer-swipe {
            from { background-position: 200% 0; }
            to { background-position: -200% 0; }
        }

        [data-testid="stSidebar"] {
            min-width: 420px !important;
            max-width: 420px !important;
        }

        div[class*="st-key-login_email"], 
        div[class*="st-key-login_password"],
        div.st-key-login_btn {
            max-width: 400px !important;
            margin: 0 auto !important;
            width: 100% !important;
        }

        div[data-testid="InputInstructions"] {
            display: none !important;
        }

        div[class*="st-key-login_"] input,
        div.st-key-login_btn button {
            max-width: 400px !important;
        }

        div[class*="st-key-reg_"],
        div.st-key-signup_btn {
            max-width: 400px !important;
            margin: 0 auto !important;
            width: 100% !important;
        }

        div[class*="st-key-reg_"] input,
        div.st-key-signup_btn button {
            max-width: 400px !important;
        }
        </style>
    """, unsafe_allow_html=True)