# Policy interception and risk scoring logic
import os
from typing import List, Dict, Any, Tuple

class ComplianceFirewall:
    def __init__(self):
        # Default budget fallback set to 0.0200 USD to accommodate standard baseline runs (~0.01430 USD)
        self.max_budget = float(os.getenv("MAX_TOKEN_BUDGET_PER_TRACE", "0.0200"))
        self.risk_threshold = float(os.getenv("MAX_RISK_SCORE_THRESHOLD", "0.75"))
        
        # Root stems to capture plurals, verb tenses, and phrasing variations
        self.high_risk_keywords = [
            "guarantee", 
            "override", 
            "unverified", 
            "off-balance", 
            "material breach", 
            "revenue bypass", 
            "undisclosed liabilit"
        ]

    def evaluate_node_output(self, topic: str, content: str) -> Tuple[float, bool, str]:
        """
        Evaluates both input directive (topic) and output analysis (content) for compliance risk keywords.
        """
        score = 0.10
        matched_flags = []

        combined_text = f"{topic} {content}".lower()
        for kw in self.high_risk_keywords:
            if kw in combined_text:
                score += 0.35
                matched_flags.append(kw)

        score = min(score, 1.0)
        is_breached = score >= self.risk_threshold
        reason = f"Flags detected: {', '.join(matched_flags)}" if matched_flags else "Standard execution"

        return score, is_breached, reason

    def evaluate_trace_risk(self, trace_logs: List[Dict[str, Any]], is_flagged: bool = False) -> float:
        """
        Calculates total trace compliance risk index synchronized with graph node escalation state.
        """
        if not trace_logs:
            return 0.0
        
        total_cost = sum(log["metrics"]["optimized_cost_usd"] for log in trace_logs)
        cost_penalty = 0.25 if total_cost > self.max_budget else 0.0
        base_score = 0.85 if is_flagged else 0.20
        
        return min(base_score + cost_penalty, 1.0)