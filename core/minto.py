# Minto Pyramid audit brief synthesis compiler
class MintoCompiler:
    @staticmethod
    def compile_brief(topic: str, raw_analysis: str, risk_flag: bool) -> str:
        status_indicator = "ACTION REQUIRED: ESCALATED TO PARTNER QUEUE" if risk_flag else "PASS: VERIFIED COMPLIANT"
        
        brief = f"""
### EXECUTIVE DIRECTIVE OVERVIEW
**Engagement Target**: {topic}  
**Compliance Status**: {status_indicator}

---

### 1. SITUATION
Autonomous agent execution completed an audit review on the target domain. Initial scope established baseline ledger alignment and preliminary transaction validation.

### 2. COMPLICATION
{"High-stakes decision boundaries or financial budget thresholds were flagged during analysis, requiring partner oversight." if risk_flag else "Standard data patterns observed with minor variances across operational context streams."}

### 3. GOVERNANCE QUESTION
Does the synthesized evidence provide adequate assurance to approve the financial reporting classification without additional manual disclosures?

### 4. ACTIONABLE ANSWER & DIRECTIVE
* **Primary Recommendation**: {"Route state to Senior Partner Escalation Queue for manual override and verification." if risk_flag else "Proceed with standard automated audit synthesis and archive telemetry record."}
* **Supporting Finding**: {raw_analysis}
"""
        return brief