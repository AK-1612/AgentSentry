# Automated verification suite for AgentSentry governance firewall
import uuid
import sys
from core.agents import runnable_graph
from core.monitor import TokenMonitor
from core.firewall import ComplianceFirewall

monitor = TokenMonitor()
firewall = ComplianceFirewall()

test_scenarios = [
    {
        "id": "TC-01",
        "name": "Standard Clean Audit",
        "topic": "PCAOB ASC 606 Revenue Recognition Review for SaaS Contract Invoicing",
        "expected_flag": False,
        "expected_score": 0.20
    },
    {
        "id": "TC-02",
        "name": "Material Risk Breach",
        "topic": "Evaluation of Off-Balance Sheet Entities and Material Breach in Revenue Recognition",
        "expected_flag": True,
        "expected_score": 0.85
    },
    {
        "id": "TC-03",
        "name": "Plural Keyword Override Defense",
        "topic": "Audit Directive for Override of Undisclosed Liabilities in Q4 Earnings",
        "expected_flag": True,
        "expected_score": 0.85
    }
]

def run_tests():
    print("================================================================")
    print("AGENTSENTRY GOVERNANCE FIREWALL VERIFICATION SUITE")
    print("================================================================\n")
    
    all_passed = True

    for test in test_scenarios:
        trace_id = str(uuid.uuid4())
        initial_state = {
            "trace_id": trace_id,
            "topic": test["topic"],
            "raw_analysis": "",
            "final_brief": "",
            "risk_flag": False
        }
        
        output = runnable_graph.invoke(initial_state)
        logs = monitor.get_trace_logs(trace_id)
        risk_score = firewall.evaluate_trace_risk(logs, is_flagged=output["risk_flag"])
        
        flag_match = output["risk_flag"] == test["expected_flag"]
        score_match = abs(risk_score - test["expected_score"]) < 0.01
        
        passed = flag_match and score_match
        if not passed:
            all_passed = False
            
        status = "PASSED" if passed else "FAILED"
        
        print(f"[{status}] {test['id']}: {test['name']}")
        print(f"  ├─ Topic Input   : '{test['topic']}'")
        print(f"  ├─ Risk Flagged  : {output['risk_flag']} (Expected: {test['expected_flag']})")
        print(f"  └─ Risk Score    : {risk_score:.2f} (Expected: {test['expected_score']:.2f})\n")

    print("================================================================")
    if all_passed:
        print("RESULT: ALL GOVERNANCE TEST CASES PASSED SUCCESSFULLY.")
        sys.exit(0)
    else:
        print("RESULT: VERIFICATION FAILED. CHECK SYSTEM LOGS.")
        sys.exit(1)

if __name__ == "__main__":
    run_tests()
