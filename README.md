# taurexruns
Different retrieval runs on wasp 107 b transmission spectrum

# 🧪 TauREx Retrieval Log — WASP-107b 

---

## Run 1: Full Chemistry + Clouds
- **Free parameters**: `T_int_guillot`, `planet_radius`, `log(H₂O)`, `log(CH₄)`, `log(CO₂)`, `log(CO)`, `log(NH₃)`, `log(SO₂)`, `clouds_pressure`
- **Priors**: Standard wide log-scale from 1e-12 to 1e-1
- **Clouds**: Included via `SimpleCloudsContribution`
- **Result**:
  - H₂O somewhat constrained: log₁₀ ≈ -2.7
  - CH₄ poorly constrained
  - Cloud pressure + CH₄ + H₂O degeneracy visible
  - Rp/R★ sharply constrained

---

## Run 2: H₂O + CH₄ Only, No Clouds, T Fixed
- **Free parameters**: `planet_radius`, `log(H₂O)`, `log(CH₄)`
- **Temperature**: Fixed
- **Clouds**: Removed
- **Result**:
  - H₂O posterior tightens slightly (log₁₀ ≈ -2.74)
  - CH₄ still not well constrained
  - Fit still good → no clouds needed to match spectrum
  - Evidence of CH₄ unnecessary, but model tolerates low abundance

---

## Run 3: H₂O + CH₄, No Clouds, Free `T_int_guillot`
- **Free parameters**: `planet_radius`, `log(H₂O)`, `log(CH₄)`, `T_int_guillot`
- **Temperature prior**: 200–550 K
- **Result**:
  - T_int not constrained (posterior flat)
  - H₂O similar to before
  - CH₄ still poorly constrained
  - Model spectrum fit unchanged → temperature doesn’t matter much here

---

## Run 4: H₂O-Only, No Clouds, T Fixed
- **Free parameters**: `planet_radius`, `log(H₂O)`
- **Chemistry**: CH₄, CO, CO₂, NH₃, SO₂ removed
- **Result**:
  - Excellent spectral fit without CH₄
  - H₂O posterior centered at log₁₀ ≈ -2.73, similar to multi-gas runs
  - Proves CH₄ is not needed by the data
  - Cleanest run with fewest degeneracies
"""
