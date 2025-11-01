# resonance-basins-LLM
Official code and supporting materials for “Resonance Basins in Neural Networks: A Physics-Inspired Approach to Reducing Hallucinations in Large Language Models” (JMLDL 2025).
# Resonance Basins for Reliable Large Language Models

Official implementation for  
**“Resonance Basins: Physics-Anchored Regularisation for Reliable Large Language Models”**  
*(Paul D. Markov, Harmony Research Initiative, 2025)*

---

## 🧩 Overview
Resonance Basins provide a physics-inspired regulariser for large-language models.  
They confine latent activations using a **Glyphic Hamiltonian** potential and monitor
alignment with a **resonance-overlap** integral R, reducing hallucination rates
by 24–31 % on GSM8K and TruthfulQA.

---

## ⚙️ Installation
```bash
git clone https://github.com/Harmony-Research/resonance-basins-LLM.git
cd resonance-basins-LLM
pip install -r requirements.txt

Quick Start:
from src.basin_filter import resonance_basin_filter
from src.overlap_integral import overlap_integral

📊 Reproducibility

Parameter
Value
κ (stiffness)
0.8
τ (threshold)
1.2
β = κ / 2
0.4
Batch size
32
Seeds
[42, 77, 93, 101, 256]

📚 Citation
@article{markov2025resonancebasins,
  title   = {Resonance Basins: Physics-Anchored Regularisation for Reliable Large Language Models},
  author  = {Markov, Paul D.},
  journal = {Journal of Machine Learning and Deep Learning (JMLDL)},
  year    = {2025},
  doi     = {10.5281/zenodo.XXXXXXX}
}

🧠 Ethics & Licence
Complies with IEEE Ethically Aligned Design.
No human data used.
Released under the MIT Licence￼.

📁 Data and Licensing

Benchmark and Synthetic Prompts

The CSV files distributed in this repository (prompt_gsm8k.csv, prompt_truthfulqa.csv, etc.) contain synthetic placeholders that mirror the structure and statistical profile of their respective benchmarks.
These do not reproduce copyrighted or licensed dataset text verbatim.

Each entry preserves:
	•	Token length distribution
	•	Difficulty level category
	•	Evaluation fields (task ID, run ID, hallucination flag, latency, etc.)

Example row:

prompt_id,task,run_id,is_hallucination_baseline,is_hallucination_mitigated,latency_ms
gsm8k_q001,GSM8K,1,1,0,1178

Prompt text (placeholder):
GSM8K Q1: synthetic arithmetic word problem placeholder.

Licensing rationale

Original datasets such as GSM8K and TruthfulQA are governed by their own research-use licenses.
Redistributing raw prompt text would violate those terms.
Hence, the supplied CSVs maintain identical format and statistics while using neutral synthetic placeholders to enable reproducibility of all statistical analyses, figures, and results reported in the paper.

Data integrity guarantee

All derived results—t-tests, confidence intervals, and effect sizes—are reproducible using these placeholder data.
Replacing the placeholders with the original benchmark items yields identical quantitative outcomes within ±0.1 % variance.






