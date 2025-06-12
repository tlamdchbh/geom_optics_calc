
# 🔬 Optics Toolkit

**Modular Streamlit app** for optical engineering calculations, including numerical
aperture (NA), reflectance loss, and Raman shift/spectral range analysis.

## 📦 Features

### 1. Geometry Calculations (`geometry_calcs.py`)

- **Numerical Aperture (NA)** from angle and index.
- **Angle from NA** in radians and degrees.
- **Geometric mean** of two values.
- **Reflectance loss** from mirror efficiency and bounce count.

### 2. Raman Calculations (`raman_calc.py`)

- **Raman Shift Calculator**: bidirectional input for laser wavelength and Raman shift.
- **Spectral Range Calculator**: interactive start/end range in both nm and cm⁻¹ with
  real-time sync.

## ▶️ Launch

To run the application:
```bash
streamlit run app.py
```

The sidebar provides navigation between the calculators.

## 🗂 File Structure

```
.
├── app.py                   # Main multipage Streamlit app
├── pages/
│   ├── geometry_calcs.py    # NA, angle, reflectance tools
│   └── raman_calc.py        # Raman shift and spectral range
├── README.md                # Project documentation
```

> ✅ Compatible with Python 3.10+

## 🛠 Requirements

Install dependencies (if not already):

```bash
pip install streamlit
```

You may also use a `requirements.txt` or `pyproject.toml` if the project expands.

## 💡 Example Use Cases

- Designing fiber coupling systems
- Estimating signal loss in reflective paths
- Calculating spectral coverage of Raman spectrometers

## 📝 License

MIT License — for internal and educational use.

---

**Developed for internal optics tooling.**

