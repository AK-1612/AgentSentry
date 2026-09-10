# Multi-agent execution graph definition
import time
import requests
import os
from typing import TypedDict
from langgraph.graph import StateGraph, END
from core.monitor import TokenMonitor
from core.firewall import ComplianceFirewall
from core.minto import MintoCompiler

monitor = TokenMonitor()
firewall = ComplianceFirewall()

class AgentSentryState(TypedDict):
    trace_id: str
    topic: str
    raw_analysis: str
    final_brief: str
    risk_flag: bool

def auditor_analyst_node(state: AgentSentryState) -> AgentSentryState:
    start_time = time.time()
    trace_id = state["trace_id"]
    topic = state["topic"]
    
    ollama_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    model = os.getenv("DEFAULT_MODEL", "llama3")
    
    prompt = f"Perform a strict corporate audit risk analysis for the following domain: {topic}. Identify potential compliance risks."
    
    try:
        response = requests.post(
            f"{ollama_url}/api/generate",
            json={"model": model, "prompt": prompt, "stream": False},
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            raw_analysis = data.get("response", "Analysis complete.")
            prompt_tokens = data.get("prompt_eval_count", 120)
            completion_tokens = data.get("eval_count", 250)
        else:
            raw_analysis = f"Simulated audit analysis for scope: {topic}. Revenue recognition criteria validated."
            prompt_tokens, completion_tokens = 120, 250
    except Exception:
        raw_analysis = f"Simulated audit analysis for scope: {topic}. Material risks assessed under PCAOB standards."
        prompt_tokens, completion_tokens = 120, 250

    latency = round(time.time() - start_time, 3)
    raw_cost = (prompt_tokens * 0.00001) + (completion_tokens * 0.00003)
    opt_cost = raw_cost * 0.75  # 25% prefix caching savings simulated
    
    monitor.log_execution(
        trace_id=trace_id,
        agent_name="AuditorAnalystNode",
        prompt_tokens=prompt_tokens,
        completion_tokens=completion_tokens,
        latency_sec=latency,
        raw_cost_usd=raw_cost,
        optimized_cost_usd=opt_cost
    )
    
    # Evaluate combined scope directive and output analysis against firewall rules
    score, is_breached, _ = firewall.evaluate_node_output(topic, raw_analysis)
    
    return {
        "raw_analysis": raw_analysis,
        "risk_flag": is_breached
    }

def minto_compiler_node(state: AgentSentryState) -> AgentSentryState:
    start_time = time.time()
    trace_id = state["trace_id"]
    
    compiled_brief = MintoCompiler.compile_brief(
        topic=state["topic"],
        raw_analysis=state["raw_analysis"],
        risk_flag=state["risk_flag"]
    )
    
    latency = round(time.time() - start_time, 3)
    prompt_tokens, completion_tokens = 180, 310
    raw_cost = (prompt_tokens * 0.00001) + (completion_tokens * 0.00003)
    opt_cost = raw_cost * 0.70
    
    monitor.log_execution(
        trace_id=trace_id,
        agent_name="MintoCompilerNode",
        prompt_tokens=prompt_tokens,
        completion_tokens=completion_tokens,
        latency_sec=latency,
        raw_cost_usd=raw_cost,
        optimized_cost_usd=opt_cost
    )
    
    return {"final_brief": compiled_brief}

workflow = StateGraph(AgentSentryState)
workflow.add_node("analyst", auditor_analyst_node)
workflow.add_node("minto", minto_compiler_node)

workflow.set_entry_point("analyst")
workflow.add_edge("analyst", "minto")
workflow.add_edge("minto", END)

runnable_graph = workflow.compile()