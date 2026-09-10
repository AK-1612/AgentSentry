# AgentSentry
Enterprise Governance Sidecar Proxy and Micro-Telemetry Engine designed for multi-agent LLM workflows (e.g., corporate financial auditing, PCAOB compliance checks).

## Core Features
1. **Real-Time Firewall Interception**: Intercept agent execution outputs to catch policy breaches, material accounting risks (e.g., off-balance sheet liabilities, revenue overrides), and scope violations.
2. **Token Telemetry & Cost Governance**: Monitor token consumption, execution latency, and raw vs. prefix-cached optimized costs in SQLite, triggering budget alerts if execution costs exceed thresholds.

## Project Structure
- `app.py`: Streamlit Enterprise Governance Console UI.
- `test_governance.py`: Automated assertion test suite to verify the firewall.
- `core/`: Contains the core logic for the LangGraph agents, firewall, and SQLite telemetry monitor.
- `data/`: Contains the auto-generated `compliance_ledger.db` SQLite database.

## Setup Instructions

1. **Create a virtual environment:**
```bash
python3 -m venv venv
```

2. **Activate the virtual environment:**
```bash
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Environment Variables (Optional):**
Create a `.env` file in the root directory to configure the execution settings:
```ini
MAX_TOKEN_BUDGET_PER_TRACE=0.0200
MAX_RISK_SCORE_THRESHOLD=0.75
OLLAMA_BASE_URL=http://localhost:11434
DEFAULT_MODEL=llama3
```

## Running the Application

**Run the automated test suite to verify the firewall rules:**
```bash
python test_governance.py
```

**Launch the Streamlit Governance UI:**
```bash
streamlit run app.py
```
