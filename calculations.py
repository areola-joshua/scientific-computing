import numpy as np

# Function to calculate Heat Transfer
def heat_transfer(U, A, delta_T):
    """
    U: overall heat transfer coefficient
    A: area
    delta_T: temperature difference (T_hot - T_cold)
    Returns: heat transfer rate (q)
    """
    q = U * A * delta_T
    return q

# Function to calculate Reaction Rate using Arrhenius equation
def reaction_rate(A, Ea, R, T):
    """
    A: pre-exponential factor
    Ea: activation energy
    R: universal gas constant (8.314 J/mol.K)
    T: temperature in Kelvin
    Returns: reaction rate constant (k)
    """
    k = A * np.exp(-Ea / (R * T))
    return k

# Function to calculate Reactor Volume for a CSTR
def cstr_volume(F_A0, X, k, C_A0):
    """
    F_A0: inlet molar flow rate of species A (mol/s)
    X: conversion (dimensionless)
    k: reaction rate constant (1/s)
    C_A0: inlet concentration of species A (mol/L)
    Returns: volume of the reactor (L)
    """
    if X == 1:
        raise ValueError("Conversion X cannot be 1 (100%) as it leads to infinite volume.")
    
    V = (F_A0 * X) / (k * C_A0 * (1 - X))
    return V