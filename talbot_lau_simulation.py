import numpy as np
import matplotlib.pyplot as plt

# ==============================================================================
# 物理定数 (SI単位系)
# ==============================================================================
HBAR = 1.054571817e-34 # プランク定数 / 2pi [J s]
AMU = 1.66053906660e-27 # 統一原子質量単位 [kg]

# ==============================================================================
# 実験系パラメータ (Arndt型 Talbot-Lau干渉計セットアップ)
# ==============================================================================
d = 266e-9 # 回折格子の周期 [m] (266 nm)
L = 2.0 # 干渉計の全長 (飛行距離) [m]
v = 100.0 # ビーム通過速度 [m/s]
t_flight = L / v # 飛行時間 [s] (20 ms)
w0 = 10e-9 # コリメーション初期波束幅 [m] (10 nm)
V_base = 0.50 # 実験系のベースライン可視度 (開口率・波長分散による定数)

# ==============================================================================
# 理論モデルのパラメータ
# ==============================================================================
# 既存実験 (25 kDa) の可視度維持から逆算された時空解像度の上限近傍を採用
sigma = 1.5e-8 # 時空のサンプリング解像度 [m] (15 nm)

# ==============================================================================
# 質量スキャン範囲 (1 kDa から 10^7 kDa = 10 MDa)
# ==============================================================================
mass_kDa = np.logspace(0, 7, 1000) # 1 kDa 〜 10,000,000 kDa
mass_kg = mass_kDa * 1000.0 * AMU

# ==============================================================================
# 可視度 (Visibility) の計算
# ==============================================================================
# 1. 飛行後の量子拡散波束幅 w(t)
# w(t)^2 = w0^2 + (hbar * t / (2 * m * w0))^2
w_t_sq = (w0**2) + ( (HBAR * t_flight) / (2.0 * mass_kg * w0) )**2

# 2. 本モデルにおける干渉抑制因子 D(t)
# 分母: 4 * (sigma^2 + 2 * w(t)^2)
# 分子: d^2 (回折格子間隔に相当する空間分離)
exponent = -(d**2) / (4.0 * (sigma**2 + 2.0 * w_t_sq))
D_t = np.exp(exponent)

# 観測される干渉縞可視度
V_NT = V_base * D_t # 本モデル (時空サンプリング限界)
V_QM = np.full_like(mass_kDa, V_base) # 環境デコヒーレンスを極限まで排除した標準量子力学

# ==============================================================================
# 臨界質量 m_c の特定 (可視度がベースラインの50%に落ちる点: D = 0.5)
# ==============================================================================
idx_critical = np.where(D_t <= 0.5)[0][0]
m_c_kDa = mass_kDa[idx_critical]
m_c_kg = mass_kg[idx_critical]

print(f"=== 計算結果 ===")
print(f"時空解像度パラメータ sigma : {sigma * 1e9:.1f} nm")
print(f"干渉が急激に崩壊する臨界質量 m_c : {m_c_kDa:.2e} kDa ({m_c_kg:.2e} kg)")

# ==============================================================================
# プロット描画
# ==============================================================================
plt.figure(figsize=(10, 6), dpi=120)

plt.plot(mass_kDa, V_QM, 'k--', label="Standard QM (Zero-Environment Decoherence)", linewidth=1.8)
plt.plot(mass_kDa, V_NT, 'r-', label="This Model (Spacetime Resolution Floor)", linewidth=2.5)

# 既存実験ベンチマーク (25 kDa: Arndt et al.)
plt.axvline(x=25, color='gray', linestyle=':', label="Arndt et al. Benchmark (25 kDa)")
plt.plot(25, V_base * np.exp(-(d**2) / (4.0 * (sigma**2 + 2.0 * ((w0**2) + ((HBAR*t_flight)/(2*25000*AMU*w0))**2)))),
         'bo', markersize=8, label="Existing Experiment (D ≈ 0.999)")

# 臨界質量 m_c のマーキング
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
