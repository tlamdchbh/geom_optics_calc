import streamlit as st
import math


def calculate_na(n: float, theta_deg: float) -> float:
    """Calculate Numerical Aperture from angle in degrees."""
    theta_rad = math.radians(theta_deg)
    return n * math.sin(theta_rad)


def na_to_angle(na: float, n: float) -> tuple[float, float]:
    """Convert NA back to angle in radians and degrees."""
    if na > n:
        return float('nan'), float('nan')  # Invalid NA
    theta_rad = math.asin(na / n)
    theta_deg = math.degrees(theta_rad)
    return theta_rad, theta_deg


def geometric_mean(x: float, y: float) -> float:
    """Return geometric mean of two values."""
    return math.sqrt(x * y)


# --- Streamlit UI ---

st.title("Optics Calculator")

# --- Block 1: NA from angle ---
st.header("1. Calculate NA from angle")
n1 = st.number_input("Refractive index (n)", value=1.0, step=0.1, key="n1")
theta_deg1 = st.number_input("Half-angle θ (degrees)", value=7.0, key="theta_deg1")

na1 = calculate_na(n1, theta_deg1)
st.write(f"**Numerical Aperture (NA) = {na1:.4f}**")

st.markdown("---")

# --- Block 2: Geometric Mean ---
st.header("2. Geometric Mean of Two Values")
val1 = st.number_input("Value 1", value=0.1, key="val1")
val2 = st.number_input("Value 2", value=0.1, key="val2")

geo_avg = geometric_mean(val1, val2)
st.write(f"**Geometric Mean = {geo_avg:.5f}**")

st.markdown("---")

# --- Block 3: Angle from NA ---
st.header("3. Calculate Angle from NA")
na2 = st.number_input("Numerical Aperture (NA)", value=0.1, key="na2")
n2 = st.number_input("Refractive index (n)", value=1.0, step=0.1, key="n2")

theta_rad2, theta_deg2 = na_to_angle(na2, n2)
if math.isnan(theta_rad2):
    st.error("Invalid input: NA must be ≤ n")
else:
    st.write(f"**Angle = {theta_rad2:.4f} rad = {theta_deg2:.2f}°**")
