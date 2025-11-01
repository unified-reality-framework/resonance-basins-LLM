"""
validate_metrics.py
Computes summary statistics for hallucination mitigation experiments.
"""
import pandas as pd
from scipy import stats
import numpy as np

def validate_metrics(csv_path):
    """
    Compute mean reduction, t-test, and Cohen's d across runs.
    """
    df = pd.read_csv(csv_path)
    grouped = df.groupby(["task", "run_id"]).mean(numeric_only=True)
    base = grouped["is_hallucination_baseline"]
    mitig = grouped["is_hallucination_mitigated"]

    t_stat, p_val = stats.ttest_rel(base, mitig)
    d = (base.mean() - mitig.mean()) / np.sqrt(((base.std()**2 + mitig.std()**2) / 2))
    return {"t_stat": t_stat, "p_value": p_val, "Cohen_d": d}
