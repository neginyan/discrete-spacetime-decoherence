# Emergence of Regular Spacetime Geometry & Carrier Sampling Theory
### Numerical Verification & Theoretical Foundations

[![DOI (Part 3)](https://zenodo.org/badge/DOI/10.5281/zenodo.22879106.svg)](https://zenodo.org/records/22879106)
[![DOI (Part 2)](https://zenodo.org/badge/DOI/10.5281/zenodo.22871687.svg)](https://zenodo.org/records/22871687)
[![DOI (Part 1)](https://zenodo.org/badge/DOI/10.5281/zenodo.22705901.svg)](https://zenodo.org/records/22705901)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)

This repository provides the official numerical implementation and mathematical verification scripts for the research series:  
**"Emergence of Regular Spacetime Geometry and the Holographic Entropy Bound from Carrier Sampling Axioms."**

> **Overview (日本語要約):**  
> 本リポジトリは、時空を有限解像度を持つ情報キャリアとして定式化し、ブラックホール特異点の解消・アインシュタイン作用の創発・ベッケンシュタイン＝ホーキングの $1/4$ エントロピー則の代数的導出を行った研究シリーズ（Part 1〜3）の数値シミュレーションおよび数式検証コードを提供します。

---

## 📄 Publications & Preprints (Zenodo)

The full theoretical framework is documented across three primary parts deposited on Zenodo:

1. **Part 1: Regular Gravitational Potential and Finite Self-Energy**  
   * **Title:** *Emergence of Regular Gravitational Potential and Finite Self-Energy from Carrier Sampling Resolution*  
   * **DOI:** [`10.5281/zenodo.22705901`](https://zenodo.org/records/22705901)  
   * **Key Highlights:** Deduction of the Plummer-type effective density from carrier sampling convolution; proof of total mass conservation and finite static field self-energy $U_{\text{field}} = -\frac{3\pi}{32}\frac{GM^2}{\sigma_0}$.

2. **Part 2: Krein-Space Duality and Causal Regularization**  
   * **Title:** *Krein-Space Duality, Indefinite Metrics, and Causal Regularization in Carrier Dynamics*  
   * **DOI:** [`10.5281/zenodo.22871687`](https://zenodo.org/records/22871687)  
   * **Key Highlights:** Formulation of canonical state spaces on Krein spaces $\mathcal{H}_{\text{total}} = \mathcal{H}_{\text{phys}} \oplus \mathcal{H}_{\text{dual}}$; implementation of the fundamental symmetry operator $J = \operatorname{diag}(-1, 1, 1, 1)$ converting Riemannian Fisher metrics into physical Lorentzian manifolds.

3. **Part 3: Spacetime Geometry and the Holographic Entropy Bound (Core Paper)**  
   * **Title:** *Emergence of Regular Spacetime Geometry and the Holographic Entropy Bound from Carrier Sampling Axioms*  
   * **DOI:** [`10.5281/zenodo.22879106`](https://zenodo.org/records/22879106)  
   * **Key Highlights:** Double-root analysis of regular black hole horizons ($M_{\text{crit}} = \frac{3\sqrt{3}}{4}\frac{c^2\sigma_0}{G}$, $r_{\text{ext}} = \sqrt{2}\sigma_0$); emergence of the Einstein-Hilbert functional from 4D geodesic volume deficits ($\Delta V_4/V_4^{\text{flat}} = \frac{\epsilon^2}{36}R$); algebraic derivation of the $1/4$ area-law factor via the composite action of Krein temporal causality ($\mathcal{P}_{\text{time}} = 1/2$) and null Clifford boundary trapping ($\mathcal{P}_{\text{space}} = 1/2$).

---

## 🔬 Key Theoretical Results Verified by Code

- **Singularity-Free Curvature:** Finite Ricci ($R(0) = 4\Lambda_{\text{eff}}$) and Kretschmann scalars ($\lim_{r \to 0} K(r) < \infty$) at the origin.
- **Horizon Phase Diagram:** Numerical evaluation of horizon existence conditions and extremal horizon degeneracy at $r = \sqrt{2}\sigma_0$.
- **Clifford Null Projections:** Explicit $2 \times 2$ matrix algebra verifying the idempotent, orthogonal, and completeness properties of the ingoing/outgoing null boundary projectors ($\mathcal{P}_\pm$).
- **Volume Contraction:** Riemannian normal coordinate expansion of 4-ball volume deficits matching $\frac{\epsilon^2}{36}R(g)$.

---

## 🚀 Quick Start

### Installation

Clone this repository and ensure Python 3.8+ is installed:

```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
cd YOUR_REPOSITORY_NAME
pip install -r requirements.txt
