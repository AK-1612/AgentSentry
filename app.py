import uuid
import streamlit as st
from core.monitor import TokenMonitor
from core.firewall import ComplianceFirewall
from core.agents import runnable_graph

# Initialize Core Services
monitor = TokenMonitor()
firewall = ComplianceFirewall()

# Page Configuration
st.set_page_config(
    page_title="AgentSentry | Enterprise Governance Console", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enterprise Modular Styling System
st.markdown("""
    <style>
        .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 2rem !important;
            max-width: 95% !important;
        }
        .stApp {
            background-color: #161616;
            color: #E0E0E0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }
        .ey-header {
            border-left: 3px solid #FFE600;
            padding-left: 16px;
            margin-bottom: 1.8rem;
        }
        .ey-title {
            font-size: 1.6rem;
            font-weight: 700;
            letter-spacing: 0.05rem;
            color: #FFFFFF;
            margin: 0;
            text-transform: uppercase;
        }
        .ey-subtitle {
            color: #8C8C8C;
            font-size: 0.85rem;
            margin: 4px 0 0 0;
            font-weight: 400;
            letter-spacing: 0.02rem;
        }
        [data-testid="stVerticalBlockBorderWrapper"], 
        div[data-testid="stContainer"] {
            background-color: #1F1F1F !important;
            border: 1px solid #2A2A2A !important;
            border-radius: 0px !important;
            padding: 1.25rem !important;
            margin-bottom: 1rem !important;
        }
        div[data-baseweb="input"], 
        [data-testid="stTextInput"] input {
            background-color: #141414 !important;
            border: 1px solid #333333 !important;
            border-radius: 0px !important;
            color: #FFFFFF !important;
            font-size: 0.9rem !important;
        }
        [data-testid="stMetricValue"], 
        [data-testid="stMetricMetric"] {
            font-family: -apple-system, BlinkMacSystemFont, sans-serif;
            font-weight: 600;
            color: #FFFFFF !important;
            font-size: 1.8rem !important;
        }
        [data-testid="stMetricLabel"] {
            font-size: 0.7rem !important;
            text-transform: uppercase;
            letter-spacing: 0.08rem;
            color: #8C8C8C !important;
            margin-bottom: 0.25rem !important;
        }
        [data-testid="stBaseButton-primary"], 
        button[kind="primary"] {
            background-color: #FFE600 !important;
            color: #161616 !important;
            font-weight: 700 !important;
            border-radius: 0px !important;
            border: none !important;
            text-transform: uppercase;
            letter-spacing: 0.06rem;
            font-size: 0.8rem !important;
            padding: 0.6rem 1.5rem !important;
            height: auto !important;
            transition: background-color 0.15s ease;
        }
        [data-testid="stBaseButton-primary"]:hover, 
        button[kind="primary"]:hover {
            background-color: #E5CC00 !important;
            color: #161616 !important;
        }
        .stTabs [data-baseweb="tab-list"] {
            gap: 4px;
            background-color: #161616;
            border-bottom: 1px solid #2A2A2A;
            padding-bottom: 0px;
        }
        .stTabs [data-baseweb="tab"] {
            height: 42px;
            background-color: #1F1F1F;
            border: 1px solid #2A2A2A;
            border-bottom: none;
            border-radius: 0px !important;
            color: #8C8C8C;
            font-weight: 600;
            font-size: 0.75rem;
            letter-spacing: 0.06rem;
            padding: 0 1.25rem;
            text-transform: uppercase;
        }
        .stTabs [aria-selected="true"] {
            background-color: #2A2A2A !important;
            color: #FFE600 !important;
            border-top: 2px solid #FFE600 !important;
        }
        div[data-testid="stExpander"] {
            background-color: #141414 !important;
            border: 1px solid #2A2A2A !important;
            border-radius: 0px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
    <div class="ey-header">
        <p class="ey-title">AgentSentry</p>
        <p class="ey-subtitle">Enterprise Governance Sidecar Proxy and Micro-Telemetry Engine for Autonomous Audit Chains</p>
    </div>
""", unsafe_allow_html=True)

# Operational Control Panel
with st.container():
    st.markdown("<p style='color:#FFE600; font-weight:700; font-size:0.75rem; text-transform:uppercase; letter-spacing:0.06rem; margin-bottom: 0.5rem;'>AUDIT DIRECTIVE INTERCEPTOR</p>", unsafe_allow_html=True)
    
    col_in, col_btn = st.columns([4, 1], gap="medium")
    
    with col_in:
        topic_input = st.text_input(
            label="Engagement Scope Directive", 
            value="PCAOB ASC 606 Revenue Recognition Review for SaaS Contract Invoicing",
            label_visibility="collapsed"
        )
    with col_btn:
        execute_clicked = st.button("RUN GOVERNANCE AUDIT", type="primary", use_container_width=True)

# Execution Workspace
if execute_clicked:
    with st.spinner("Processing execution graph through governance proxy..."):
        current_trace_id = str(uuid.uuid4())
        initial_state = {
            "trace_id": current_trace_id, 
            "topic": topic_input, 
            "raw_analysis": "", 
            "final_brief": "",
            "risk_flag": False
        }
        
        final_output = runnable_graph.invoke(initial_state)
        trace_logs = monitor.get_trace_logs(current_trace_id)
        
        # Key Financial & Governance Metrics
        if trace_logs:
            total_raw_cost = sum(log["metrics"]["raw_cost_usd"] for log in trace_logs)
            total_opt_cost = sum(log["metrics"]["optimized_cost_usd"] for log in trace_logs)
            
            # Pass node escalation flag into risk calculator for metric card sync
            risk_score = firewall.evaluate_trace_risk(
                trace_logs,
                is_flagged=final_output.get("risk_flag", False)
            )
            
            with st.container():
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric(label="TOTAL INGESTION SPEND", value=f"${total_opt_cost:.5f}")
                with col2:
                    st.metric(label="CALCULATED BASE COST", value=f"${total_raw_cost:.5f}")
                with col3:
                    st.metric(
                        label="COMPLIANCE RISK INDEX", 
                        value=f"{risk_score:.2f}",
                        delta="PASSED" if risk_score < 0.75 else "ESC-REQUIRED",
                        delta_color="normal" if risk_score < 0.75 else "inverse"
                    )

        # Modular Workspace Tabs
        tab_brief, tab_logs, tab_ledger = st.tabs([
            "EXECUTIVE BRIEF", 
            "NODE INTERCEPTION TRAIL", 
            "TELEMETRY LEDGER"
        ])
        
        with tab_brief:
            with st.container():
                st.markdown("<p style='color:#FFE600; font-weight:700; font-size:0.75rem; text-transform:uppercase; letter-spacing:0.06rem;'>MINTO PYRAMID STRUCTURED BRIEF</p>", unsafe_allow_html=True)
                st.markdown("<div style='border-top: 1px solid #2A2A2A; margin-top:8px; margin-bottom:15px;'></div>", unsafe_allow_html=True)
                st.markdown(final_output.get("final_brief", "No brief generated."))
                
        with tab_logs:
            with st.container():
                st.markdown("<p style='color:#FFFFFF; font-weight:700; font-size:0.75rem; text-transform:uppercase; letter-spacing:0.06rem;'>REAL-TIME FIREWALL INTERCEPTION LOGS</p>", unsafe_allow_html=True)
                st.markdown("<div style='border-top: 1px solid #2A2A2A; margin-top:8px; margin-bottom:15px;'></div>", unsafe_allow_html=True)
                
                for idx, log in enumerate(trace_logs):
                    with st.expander(f"Agent Node: {log['agent']}", expanded=(idx == 0)):
                        st.json(log["metrics"])

        with tab_ledger:
            with st.container():
                st.markdown("<p style='color:#FFFFFF; font-weight:700; font-size:0.75rem; text-transform:uppercase; letter-spacing:0.06rem;'>PERSISTENT AUDIT TRAIL DATA</p>", unsafe_allow_html=True)
                st.markdown("<div style='border-top: 1px solid #2A2A2A; margin-top:8px; margin-bottom:15px;'></div>", unsafe_allow_html=True)
                
                table_data = []
                for log in trace_logs:
                    table_data.append({
                        "Agent Node": log["agent"],
                        "Prompt Tokens": log["metrics"]["prompt_tokens"],
                        "Completion Tokens": log["metrics"]["completion_tokens"],
                        "Latency (s)": log["metrics"]["latency_sec"],
                        "Cost (USD)": f"${log['metrics']['optimized_cost_usd']:.5f}",
                        "Timestamp": log["metrics"]["timestamp"]
                    })
                st.table(table_data)