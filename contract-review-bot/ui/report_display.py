import streamlit as st
import json
import plotly.graph_objects as go
import plotly.express as px

def get_risk_badge(risk_level: str) -> str:
    """Returns an HTML badge depending on risk level keyword."""
    if isinstance(risk_level, dict):
        lvl = str(risk_level.get("severity", "None")).lower()
    else:
        lvl = str(risk_level).lower()
        
    if "high" in lvl:
        return "<span class='badge badge-danger'>High Risk</span>"
    elif "medium" in lvl:
        return "<span class='badge badge-warning'>Medium Risk</span>"
    elif "low" in lvl:
        return "<span class='badge badge-info'>Low Risk</span>"
    else:
        return "<span class='badge badge-success'>Safe / None</span>"

@st.cache_data
def render_risk_heatmap(risks: dict):
    """
    Renders a 2D Heatmap (Likelihood vs Severity).
    """
    
    z_data = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    map_idx = {"low": 0, "medium": 1, "high": 2}
    
    has_data = False
    for risk_key in risks:
        r = risks[risk_key]
        if isinstance(r, dict):
            sev = r.get("severity", "none").lower()
            lik = r.get("likelihood", "none").lower()
            if sev in map_idx and lik in map_idx:
                z_data[map_idx[lik]][map_idx[sev]] += 1
                has_data = True
                
    if not has_data:
        return None

    fig = go.Figure(data=go.Heatmap(
        z=z_data,
        x=['Low Severity', 'Med Severity', 'High Severity'],
        y=['Low Likelihood', 'Med Likelihood', 'High Likelihood'],
        colorscale='GnBu',
        showscale=False,
        text=z_data,
        texttemplate="%{text}",
        textfont={"size":16, "color":"#1E293B"}
    ))

    fig.update_layout(
        height=250,
        margin=dict(l=10, r=10, t=10, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={'family': "Inter"}
    )
    return fig

@st.cache_data
def render_confidence_gauge(score: int):
    """
    Renders a premium Plotly gauge for AI Confidence.
    """
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "AI Confidence", 'font': {'size': 18, 'color': '#64748B'}},
        gauge = {
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "#94A3B8"},
            'bar': {'color': "#0D9488"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "#E2E8F0",
            'steps': [
                {'range': [0, 50], 'color': '#FEE2E2'},
                {'range': [50, 80], 'color': '#FEF3C7'},
                {'range': [80, 100], 'color': '#D1FAE5'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': score
            }
        }
    ))
    
    fig.update_layout(
        height=220, 
        margin=dict(l=30, r=30, t=50, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        font={'color': "#1E293B", 'family': "Inter"}
    )
    return fig

def render_dashboard_header(report_data: dict, final_risk_score: int):
    """
    Renders the 'Hot Spot' KPI header.
    """
    st.markdown("## 💎 Contract Intelligence Dashboard")
    
    col1, col2, col3 = st.columns([1, 1, 1.5])
    
    with col1:
        st.markdown('<div class="metric-spotlight">', unsafe_allow_html=True)
        st.metric("Contract Type", report_data.get("contract_type", "Unknown"))
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="metric-spotlight">', unsafe_allow_html=True)
        st.metric("Total Risk", f"{final_risk_score}/100")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col3:
        conf_score = report_data.get("confidence_score", 0)
        st.plotly_chart(render_confidence_gauge(conf_score), use_container_width=True, config={'displayModeBar': False})

@st.cache_data
def render_risk_analytics(risks: dict):
    """
    Renders a Plotly horizontal bar chart showing risk distribution.
    """
    
    categories = ["Liability", "Auto-Renewal", "Exit Clause"]
    levels = [
        risks.get("liability_risk", "None"),
        risks.get("auto_renewal_risk", "None"),
        risks.get("missing_exit_clause_risk", "None")
    ]
    
    score_map = {"high": 100, "medium": 60, "low": 30, "none": 5, "safe": 5}
    values = [score_map.get(str(l).lower().split()[0], 5) for l in levels]
    
    if all(v <= 5 for v in values):
        st.info("✅ **Safe Profile Detected:** No significant high-level risks identified in these categories.")
        return None

    fig = px.bar(
        x=values,
        y=categories,
        orientation='h',
        color=values,
        color_continuous_scale=['#D1FAE5', '#FEF3C7', '#FEE2E2'],
        range_color=[0, 100],
        labels={'x': 'Risk Intensity (%)', 'y': 'Category'}
    )
    
    fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=20, b=20),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        coloraxis_showscale=False,
        font={'family': "Inter"}
    )
    
    return fig

def display_analysis_report(report_data: dict, final_risk_score: int):
    """
    Renders the structured report dynamically based on Gemini's JSON extraction.
    
    Args:
        report_data (dict): The parsed JSON from the LLM.
        final_risk_score (int): The combined risk score (AI + Manual).
    """
    
    render_dashboard_header(report_data, final_risk_score)
    
    st.markdown("<br/>", unsafe_allow_html=True)
    
    st.markdown("<br/>", unsafe_allow_html=True)
    
    st.markdown("### 📈 Risk Intelligence Analytics")
    col_a1, col_a2 = st.columns([1.5, 1])
    
    with col_a1:
        st.markdown("**Risk Distribution Profile**")
        analytics_fig = render_risk_analytics(report_data.get("risk_flags", {}))
        if analytics_fig:
            with st.container(border=True):
                st.plotly_chart(analytics_fig, use_container_width=True, config={'displayModeBar': False})
        else:
            st.info("✅ **Safe Profile:** No category risks detected.")

    with col_a2:
        st.markdown("**Dynamic Risk Matrix**")
        heatmap_fig = render_risk_heatmap(report_data.get("risk_flags", {}))
        if heatmap_fig:
            with st.container(border=True):
                st.plotly_chart(heatmap_fig, use_container_width=True, config={'displayModeBar': False})
        else:
            st.info("No heatmap data.")

    st.markdown("### 🚨 Critical Vulnerabilities")
    risks = report_data.get("risk_flags", {})
    
    for risk_name, details in risks.items():
        if isinstance(details, dict) and details.get("severity", "none").lower() != "none":
            with st.container(border=True):
                c1, c2 = st.columns([1, 4])
                with c1:
                    st.markdown(get_risk_badge(details), unsafe_allow_html=True)
                with c2:
                    st.markdown(f"**{risk_name.replace('_', ' ').title()}**")
                    st.write(details.get("explanation", "N/A"))

    risky_sentences = report_data.get("risky_sentences", [])
    if risky_sentences:
        st.markdown("### 🖋️ Contextual Highlighting")
        st.info("Click a clause below to focus the source text panel.")
        
        if 'focused_clause' not in st.session_state: st.session_state.focused_clause = None
        
        selected_clause = st.selectbox("Select extraction to verify in context:", ["None Selected"] + risky_sentences)
        
        if selected_clause != "None Selected":
            from utils.text_utils import find_context_snippet
            
            raw_contract = st.session_state.get('last_raw_text', "Source contract text not found in session memory.")
            
            with st.container(border=True):
                st.markdown("**Original Source Context:**")
                st.markdown(find_context_snippet(raw_contract, selected_clause))

    st.markdown("<br/>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("### 📝 Plain English Summary")
        st.write(report_data.get("plain_english_summary", "No summary provided."))
                
    st.markdown("### 🔍 Key Extracted Terms")
    with st.expander("Parties Involved"):
        st.write(report_data.get("parties", "N/A"))
        
    with st.expander("Duration & Renewal Terms"):
        st.write("**Duration:**", report_data.get("contract_duration", "N/A"))
        st.write("**Renewal Terms:**", report_data.get("renewal_terms", "N/A"))
        
    with st.expander("Financial & Payment Terms"):
        st.write(report_data.get("payment_terms", "N/A"))
        
    with st.expander("Termination Rights"):
        st.write(report_data.get("termination_clauses", "N/A"))
        
    with st.expander("Liability & Indemnification"):
        st.write(report_data.get("liability_clauses", "N/A"))
        
    st.markdown("---")
    if st.checkbox("Show Raw AI JSON Output"):
        st.json(report_data)
        
    json_string = json.dumps(report_data, indent=2)
    st.download_button(
        label="Download Full Report (JSON)",
        file_name="contract_analysis_report.json",
        mime="application/json",
        data=json_string
    )