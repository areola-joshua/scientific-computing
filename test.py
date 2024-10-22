import numpy as np
import matplotlib.pyplot as plt
from calculations import heat_transfer, reaction_rate, cstr_volume 

# Example 1: Heat Transfer Calculation
U = 500   # overall heat transfer coefficient (W/m^2.K)
A = 10    # area (m^2)
delta_T = 30  # temperature difference (K)

q = heat_transfer(U, A, delta_T)
print(f"Heat Transfer Rate: {q}W")

# Example 2: Reaction Rate using Arrhenius Equation
A_factor = 1e12     # pre-exponential factor
Ea = 50000          # activation energy (J/mol)
R = 8.314           # gas constant (J/mol.K)
T = np.linspace(300, 1000, 100)  # temperature range in Kelvin

reaction_rates = reaction_rate(A_factor, Ea, R, T)

# Plotting the reaction rate vs temperature
plt.plot(T, reaction_rates)
plt.title("Reaction Rate vs Temperature")
plt.xlabel("Temperature (K)")
plt.ylabel("Reaction Rate Constant (k)")
plt.grid(True)
plt.show()

# Example 3: CSTR Volume Calculation
F_A0 = 5.0    # inlet molar flow rate (mol/s)
X = 0.8       # desired conversion (80%)
k = 0.02      # reaction rate constant (1/s)
C_A0 = 2.0    # inlet concentration (mol/L)

V = cstr_volume(F_A0, X, k, C_A0)
print(f"Required Reactor Volume: {V} L")