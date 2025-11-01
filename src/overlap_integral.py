"""
overlap_integral.py
Monte-Carlo overlap integral estimator for R = ∫ ρ_h(x) ρ_a(x) dx
"""
import torch

def overlap_integral(rho_h, rho_a, n_samples=10000, dim=512):
    """
    Estimates resonance-overlap integral between human and AI embeddings.

    Args:
        rho_h, rho_a (callables): density functions
        n_samples (int): number of Monte Carlo samples
        dim (int): embedding dimension
    Returns:
        float: estimated overlap value R
    """
    x = torch.randn(n_samples, dim)
    return torch.mean(rho_h(x) * rho_a(x)).item()
