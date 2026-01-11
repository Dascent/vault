"""  
Diagnostics helpers for Healer++ (alternative modular file).  
This module can be used to extend advanced health metrics or to plug into  
external monitoring for Shapes.  
"""

from __future__ import annotations  
from typing import Dict, Any

def analyze_state(state: Dict[str, Any]) -> Dict[str, Any]:  
    """Return a compact health report dict for external consumption."""  
    mem_len = len(state.get("memory", []))  
    out_len = len(state.get("outputs", []))  
    drift = any("spiral" in s.lower() or "drift" in s.lower() for s in state.get("outputs", [])[-20:])  
    repetition = _count_repetition(state.get("outputs", [])[-10:])  
    score = 0.85  
    if drift:  
        score -= 0.25  
    if repetition > 2:  
        score -= 0.15  
    if mem_len > 100:  
        score -= 0.15  
    score = max(0.0, min(1.0, score))  
    return {  
        "healthScore": score,  
        "metrics": {  
            "memorySize": mem_len,  
            "outputsSize": out_len,  
            "driftDetected": drift,  
            "repetitionCountLast10": repetition,  
        },  
        "notes": "This is a starter health metric bundle. Integrate with real telemetry as needed."  
    }

def _count_repetition(outputs: list) -> int:  
    counts = {}  
    for o in outputs:  
        for t in o.split():  
            counts[t] = counts.get(t, 0) + 1  
    return sum(1 for c in counts.values() if c > 1)  