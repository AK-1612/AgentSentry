# Telemetry capture and SQLite persistence engine
import os
import sqlite3
import threading
from typing import List, Dict, Any

class TokenMonitor:
    def __init__(self, db_path: str = "data/compliance_ledger.db"):
        self.db_path = db_path
        self._lock = threading.Lock()
        self._init_db()

    def _init_db(self):
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        with self._lock:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS telemetry (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    trace_id TEXT NOT NULL,
                    agent_name TEXT NOT NULL,
                    prompt_tokens INTEGER NOT NULL,
                    completion_tokens INTEGER NOT NULL,
                    latency_sec REAL NOT NULL,
                    raw_cost_usd REAL NOT NULL,
                    optimized_cost_usd REAL NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
            conn.close()

    def log_execution(
        self, 
        trace_id: str, 
        agent_name: str, 
        prompt_tokens: int, 
        completion_tokens: int, 
        latency_sec: float, 
        raw_cost_usd: float, 
        optimized_cost_usd: float
    ):
        with self._lock:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO telemetry (
                    trace_id, agent_name, prompt_tokens, completion_tokens, 
                    latency_sec, raw_cost_usd, optimized_cost_usd
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (trace_id, agent_name, prompt_tokens, completion_tokens, latency_sec, raw_cost_usd, optimized_cost_usd))
            conn.commit()
            conn.close()

    def get_trace_logs(self, trace_id: str) -> List[Dict[str, Any]]:
        with self._lock:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("""
                SELECT agent_name, prompt_tokens, completion_tokens, latency_sec, raw_cost_usd, optimized_cost_usd, timestamp
                FROM telemetry WHERE trace_id = ? ORDER BY id ASC
            """, (trace_id,))
            rows = cursor.fetchall()
            conn.close()

        logs = []
        for r in rows:
            logs.append({
                "agent": r[0],
                "metrics": {
                    "prompt_tokens": r[1],
                    "completion_tokens": r[2],
                    "latency_sec": r[3],
                    "raw_cost_usd": r[4],
                    "optimized_cost_usd": r[5],
                    "timestamp": r[6]
                }
            })
        return logs