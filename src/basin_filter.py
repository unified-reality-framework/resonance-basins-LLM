"""
basin_filter.py
Implements the forward-pass resonance basin filter from the JMLDL 2025 paper.
"""
import torch

def resonance_basin_filter(x, kappa=0.8, tau=1.2):
    """
    Damps high-norm latent activations to stabilise representation energy.

    Args:
        x (torch.Tensor): input activations
        kappa (float): basin stiffness coefficient
        tau (float): threshold for damping activation norm
    Returns:
        torch.Tensor: filtered activations
    """
    beta = kappa / 2
    norms = torch.norm(x, dim=-1, keepdim=True)
    mask = norms > tau
    x_filtered = x * torch.exp(-beta * norms**2)
    return torch.where(mask, x_filtered, x)
