import streamlit as st
import math

st.title("Optics Calculator")

st.header("1. Numerical Aperture (NA) Calculator")
n = st.number_input("Refractive index (n)", value=1.0, step=0.1)
theta_deg = st.number_input("Half-angle θ (in degrees)", value=7.69)

theta_rad = math.radians(theta_deg)
na = n * math.sin(theta_rad)
st.write(f"**Numerical Aperture (NA) = {na:.5f}**")

st.markdown("---")

st.header("2. Angle Multiplication (e.g., for etendue)")
theta_x = st.number_input("θₓ (in radians)", value=0.0225)
theta_y = st.number_input("θᵧ (in radians)", value=0.1055)

product = theta_x * theta_y
st.write(f"**θₓ × θᵧ = {product:.6f} rad²**")
