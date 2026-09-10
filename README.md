# AgentSentry
Enterprise Governance Sidecar Proxy and Micro-Telemetry Engine designed for multi-agent LLM workflows (e.g., corporate financial auditing, PCAOB compliance checks).

## Core Purpose:
1. **Real-Time Firewall Interception**: Intercept agent execution outputs to catch policy breaches, material accounting risks (e.g., off-balance sheet liabilities, revenue overrides), and scope violations.
2. **Token Telemetry & Cost Governance**: Monitor token consumption, execution latency, and raw vs. prefix-cached optimized costs in SQLite, triggering budget alerts if execution costs exceed thresholds.
3. **Minto Pyramid Brief Synthesis**: Synthesize raw audit findings into structured executive directives (Situation, Complication, Governance Question, Actionable Answer) and auto-escalate breached traces to a Partner Queue.
