# AgentSentry

**Enterprise Governance Sidecar Proxy and Micro-Telemetry Audit Layer for Autonomous Multi-Agent Systems**

AgentSentry is an enterprise-grade governance sidecar proxy designed to intercept, audit, and enforce compliance across autonomous multi-agent Large Language Model (LLM) workflows (such as audit automation engines, M&A advisory chains, or tax research agents). It mitigates non-deterministic model output, enforces micro-financial token budgets, and automatically converts multi-agent execution traces into executive Minto Pyramid briefs for regulatory and leadership review.

---

## Executive Overview

As enterprise AI adoption transitions from static assistance to autonomous multi-agent orchestration, organizations face critical operational, financial, and regulatory risks:

* **Regulatory Non-Compliance**: Traditional point-in-time governance checklists fail to inspect dynamic, non-deterministic agent-to-agent negotiations.
* **Unbounded Compute Costs**: Multi-agent recursive loops and context inflation lead to unpredictable API cost spikes.
* **Lack of Auditability**: High-volume, raw JSON execution logs are impractical for human audit reviews required by frameworks such as PCAOB, SEC, and the EU AI Act.

AgentSentry resolves these challenges by operating as an inline compliance gatekeeper. It enforces strict boundary controls, records node-level micro-telemetry, and halts execution via a dynamic Human-in-the-Loop (HITL) circuit breaker whenever budget or risk thresholds are exceeded.

---

## System Architecture

```text
┌──────────────────────────┐      ┌────────────────────────────────────────────────────────┐      ┌──────────────────────────┐
│  Autonomous Agent Graph  │ ───► │                      AgentSentry                       │ ───► │ Enterprise LLM Gateway   │
│ (LangGraph Execution)    │      │  1. Micro-Telemetry & Trace UUID Interceptor           │      │ (Azure OpenAI / Ollama)  │
└──────────────────────────┘      │  2. Real-Time Policy Boundary Check (Budget / Risk)    │      └──────────────────────────┘
                                  │  3. Minto Pyramid Audit Trail Synthesizer              │
                                  └───────────────────────────┬────────────────────────────┘
                                                              │
                                                   [Risk Threshold Exceeded?]
                                                              │
                                                       Trigger HITL Gate
                                                 Executive Approval Workflow

```

---

## Core Operational Pillars

### 1. Micro-Financial Telemetry Ledger

* **Node-Level Attribution**: Tracks input/output token counts, compute cost, and latency per individual agent node execution.
* **Thread-Safe Persistence**: Logged to an embedded, high-throughput SQLite engine indexed by unique trace UUIDs.
* **Efficiency Analysis**: Quantifies economic margins captured through prompt optimization and prefix caching strategies.

### 2. Compliance and Policy Firewall

* **Real-Time Risk Scoring**: Evaluates agent outputs against pre-configured operational and domain-specific compliance rules.
* **Automated Circuit Breaking**: Halts execution state and routes the context to an executive escalation queue if cumulative spend or risk indexes cross policy limits.
* **Deterministic Boundary Enforcement**: Blocks high-stakes decision propagation prior to downstream context consumption.

### 3. Minto Pyramid Audit Brief Synthesizer

* **Structured Summarization**: Filters complex multi-agent execution graphs into standardized executive briefs formatted according to the Minto Pyramid Framework (Situation, Complication, Question, Answer).
* **Audit Readiness**: Generates human-readable compliance logs suitable for senior leadership sign-off and regulatory retention.

### 4. Enterprise Governance Console

* **Real-Time Visibility**: High-contrast operational dashboard displaying financial telemetry, risk indexes, and active agent traces.
* **Partner Control Point**: Enables manual review, state inspection, and override capabilities for flagged agent workflows.

---

## Technical Architecture

* **Agent Orchestration**: LangGraph / LangChain
* **Telemetry Persistence**: Python / SQLite3 (Thread-Safe Isolation)
* **Governance Console**: Streamlit 1.30+ (Custom Geometric CSS Architecture)
* **LLM Gateway Abstraction**: Hybrid Local-to-Cloud Routing (Ollama / Azure OpenAI / Anthropic)

---

## Repository Structure

```text
AgentSentry/
├── core/
│   ├── __init__.py
│   ├── agents.py              # Multi-agent execution graph definition
│   ├── firewall.py            # Policy interception and risk scoring logic
│   ├── monitor.py             # Telemetry capture and SQLite persistence engine
│   └── minto.py               # Minto Pyramid audit brief synthesis compiler
├── data/
│   └── compliance_ledger.db   # Persistent audit trail and telemetry storage
├── .env                       # Environment configuration and risk threshold settings
├── .gitignore
├── app.py                     # Streamlit Enterprise Governance Console
├── README.md                  # System documentation
└── requirements.txt           # Project dependencies

```

---

## Getting Started

### Prerequisites

* Python 3.10+
* Git
* Local or remote LLM endpoint (e.g., Ollama, Azure OpenAI)

### Installation

1. **Clone the Repository**:
```bash
git clone https://github.com/YOUR_ORGANIZATION/AgentSentry.git
cd AgentSentry

```


2. **Initialize Virtual Environment**:
```bash
python3 -m venv venv
source venv/bin/activate

```


3. **Install Dependencies**:
```bash
pip install --upgrade pip
pip install -r requirements.txt

```


4. **Configure Environment Variables**:
Create a `.env` file in the root directory:
```env
OLLAMA_BASE_URL=http://localhost:11434
DEFAULT_MODEL=llama3
MAX_TOKEN_BUDGET_PER_TRACE=0.0100
MAX_RISK_SCORE_THRESHOLD=0.75

```


5. **Launch the Governance Console**:
```bash
streamlit run app.py

```



---

## Configuration Parameters

| Variable Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| `OLLAMA_BASE_URL` | String | Endpoint URL for local LLM inference | `http://localhost:11434` |
| `DEFAULT_MODEL` | String | Model identifier for local or cloud calls | `llama3` |
| `MAX_TOKEN_BUDGET_PER_TRACE` | Float | Financial spend ceiling (USD) allowed per single execution trace | `0.0100` |
| `MAX_RISK_SCORE_THRESHOLD` | Float | Maximum allowable risk score (0.0 to 1.0) before triggering HITL gate | `0.75` |

---

## Enterprise Regulatory Alignment

AgentSentry provides measurable alignment with core enterprise governance requirements:

* **PCAOB & SEC Audit Standards**: Delivers deterministic, immutable audit trails showing the exact inputs, prompt parameters, and token spends that generated a financial assertion.
* **EU AI Act Governance**: Enforces real-time human oversight (Human-in-the-Loop) for high-risk autonomous decision chains.
* **Corporate Cost Management**: Prevents unbudgeted LLM compute inflation through real-time trace expenditure limits.
