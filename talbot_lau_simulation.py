import numpy as np
import matplotlib.pyplot as plt

# ==============================================================================
# Physical Constants (SI Units)
# ==============================================================================
HBAR = 1.054571817e-34  # Reduced Planck constant [J s]
AMU  = 1.66053906660e-27 # Unified atomic mass unit [kg]

# ==============================================================================
# Experimental Parameters (Arndt-type Talbot-Lau Interferometer Setup)
# ==============================================================================
d        = 266e-9       # Grating period [m] (266 nm)
L        = 2.0          # Total interferometer length / flight distance [m]
v        = 100.0        # Beam velocity [m/s]
t_flight = L / v        # Time of flight [s] (20 ms)
w0       = 10e-9        # Initial collimation wavepacket width [m] (10 nm)
V_base   = 0.50         # Baseline visibility (set by aperture and dispersion)

# ==============================================================================
# Theoretical Model Parameter
# ==============================================================================
# Upper bound of spacetime sampling resolution consistent with 25 kDa benchmarks
sigma = 1.5e-8          # Spacetime sampling resolution [m] (15 nm)

# ==============================================================================
# Mass Scan Range (1 kDa to 10^7 kDa = 10 MDa)
# ==============================================================================
mass_kDa = np.logspace(0, 7, 1000)  # 1 kDa to 10,000,000 kDa
mass_kg  = mass_kDa * 1000.0 * AMU

# ==============================================================================
# Fringe Visibility Calculation
# ==============================================================================
# 1. Quantum dispersive wavepacket width after free flight w(t)
#    w(t)^2 = w0^2 + (hbar * t / (2 * m * w0))^2
w_t_sq = (w0**2) + ( (HBAR * t_flight) / (2.0 * mass_kg * w0) )**2

# 2. Decoherence damping factor D(t) derived from spacetime sampling geometry
#    Denominator: 4 * (sigma^2 + 2 * w(t)^2)
#    Numerator:   d^2 (spatial separation corresponding to grating period)
exponent = -(d**2) / (4.0 * (sigma**2 + 2.0 * w_t_sq))
D_t = np.exp(exponent)

# Observable fringe visibility
V_NT = V_base * D_t                     # This model (spacetime resolution limit)
V_QM = np.full_like(mass_kDa, V_base)   # Standard QM (isolated environment)

# ==============================================================================
# Identification of Critical Mass m_c (D(t) = 0.5 threshold)
# ==============================================================================
idx_critical = np.where(D_t <= 0.5)[0][0]
m_c_kDa = mass_kDa[idx_critical]
m_c_kg  = mass_kg[idx_critical]

print("=== Simulation Results ===")
print(f"Spacetime resolution parameter sigma: {sigma * 1e9:.1f} nm")
print(f"Critical mass for rapid decoherence m_c: {m_c_kDa:.2e} kDa ({m_c_kg:.2e} kg)")

# ==============================================================================
# Plotting
# ==============================================================================
plt.figure(figsize=(10, 6), dpi=120)

plt.plot(mass_kDa, V_QM, 'k--', label="Standard QM (Zero-Environment Decoherence)", linewidth=1.8)
plt.plot(mass_kDa, V_NT, 'r-',  label="This Model (Spacetime Resolution Floor)", linewidth=2.5)

# Benchmark: Existing experiment (25 kDa, Arndt et al.)
plt.axvline(x=25, color='gray', linestyle=':', label="Arndt et al. Benchmark (25 kDa)")
benchmark_vis = V_base * np.exp(-(d**2) / (4.0 * (sigma**2 + 2.0 * ((w0**2) + ((HBAR * t_flight) / (2 * 25000 * AMU * w0))**2))))
plt.plot(25, benchmark_vis, 'bo', markersize=8, label="Existing Experiment (D ≈ 0.999)")

# Critical mass m_c marking
plt.axvline(x=m_c_kDa, color='red', linestyle='-.', alpha=0.7)
plt.plot(m_c_kDa, V_base * 0.5, 'ro', markersize=8, label=f"Critical Mass $m_c$ ≈ {m_c_kDa:.1e} kDa")

plt.xscale('log')
plt.ylim(-0.02, V_base * 1.15)
plt.xlabel("Particle Mass $m$ [kDa]", fontsize=12)
plt.ylabel("Fringe Visibility $\mathcal{V}$", fontsize=12)
plt.title("Quantum-to-Classical Phase Transition Floor in Matter-Wave Interferometry", fontsize=13, fontweight='bold')
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.legend(loc="lower left", fontsize=10)

plt.tight_layout()
plt.show()
