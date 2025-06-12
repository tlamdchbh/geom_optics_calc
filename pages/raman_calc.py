"""
Raman Shift & Spectral Range Calculator – Two-Way Input

"""

import streamlit as st

# ---------------------------------------------------------------------
# Helper-Funktionen
# ---------------------------------------------------------------------
def shift_from_wavelength(laser_nm: float, wavelength_nm: float) -> float:
    """Δσ (cm-1) aus λ_ex und λ"""
    return (1 / laser_nm - 1 / wavelength_nm) * 1e7


def wavelength_from_shift(laser_nm: float, shift_cm: float) -> float:
    """λ (nm) aus λ_ex und Δσ"""
    return 1 / (1 / laser_nm - shift_cm / 1e7)


# ---------------------------------------------------------------------
# Callback-Funktionen – Single Raman Shift Calculator
# ---------------------------------------------------------------------
def cb_single_from_wavelength() -> None:
    """Rechnet Δσ aus λ, wenn λ editiert wurde."""
    st.session_state.shift_single = shift_from_wavelength(
        st.session_state.laser_single, st.session_state.wavelength_single
    )


def cb_single_from_shift() -> None:
    """Rechnet λ aus Δσ, wenn Δσ editiert wurde."""
    st.session_state.wavelength_single = wavelength_from_shift(
        st.session_state.laser_single, st.session_state.shift_single
    )


# ---------------------------------------------------------------------
# Callback-Funktionen – Spectral Range Calculator (Start)
# ---------------------------------------------------------------------
def cb_start_from_nm() -> None:
    st.session_state.start_shift = shift_from_wavelength(
        st.session_state.laser_rng, st.session_state.start_nm
    )


def cb_start_from_shift() -> None:
    st.session_state.start_nm = wavelength_from_shift(
        st.session_state.laser_rng, st.session_state.start_shift
    )


# ---------------------------------------------------------------------
# Callback-Funktionen – Spectral Range Calculator (End)
# ---------------------------------------------------------------------
def cb_end_from_nm() -> None:
    st.session_state.end_shift = shift_from_wavelength(
        st.session_state.laser_rng, st.session_state.end_nm
    )


def cb_end_from_shift() -> None:
    st.session_state.end_nm = wavelength_from_shift(
        st.session_state.laser_rng, st.session_state.end_shift
    )


# ---------------------------------------------------------------------
# Streamlit UI
# ---------------------------------------------------------------------
st.title("Raman Shift & Spectral Range Calculator")

# ---------------------------- Raman Shift Calculator ------------------
with st.expander("► Raman Shift Calculator", expanded=True):
    st.write(
        "Geben Sie **entweder** die absolute Wellenlänge *oder* den Raman-Shift ein – "
        "das jeweils andere Feld wird sofort aktualisiert."
    )

    # Laser-Wellenlänge
    st.number_input(
        "Laser excitation wavelength λ_ex (nm)",
        key="laser_single",
        min_value=100.0,
        value=785.0,
        step=0.1,
    )

    # Absolut-Wellenlänge (nm)  ⇄  Raman-Shift (cm-1)
    st.number_input(
        "Absolute wavelength λ (nm)",
        key="wavelength_single",
        min_value=100.0,
        value=785.0,
        step=0.01,
        on_change=cb_single_from_wavelength,
    )

    st.number_input(
        "Raman shift Δσ (cm⁻¹)",
        key="shift_single",
        value=0.0,
        step=1.0,
        on_change=cb_single_from_shift,
    )

# ------------------------ Raman Spectral Range Calculator -------------
with st.expander("► Raman Spectral Range Calculator", expanded=True):
    st.write(
        "Zwei-Wege-Eingabe für Start- und Endpunkte: "
        "Füllen Sie **beliebige** Felder aus – das System synchronisiert automatisch."
    )

    # Laser-Wellenlänge für Range-Berechnung
    st.number_input(
        "Laser excitation wavelength λ_ex (nm)",
        key="laser_rng",
        min_value=100.0,
        value=785.0,
        step=0.1,
    )

    # ---------- Start-Punkt ----------
    st.subheader("Start")
    col_start_nm, col_start_shift = st.columns(2)

    with col_start_nm:
        st.number_input(
            "Start wavelength λ_start (nm)",
            key="start_nm",
            min_value=100.0,
            value=785.0,
            step=0.01,
            on_change=cb_start_from_nm,
            format="%.2f",
        )
    with col_start_shift:
        st.number_input(
            "Start shift Δσ_start (cm⁻¹)",
            key="start_shift",
            value=0.0,
            step=1.0,
            on_change=cb_start_from_shift,
        )

    # ---------- End-Punkt ----------
    st.subheader("End")
    col_end_nm, col_end_shift = st.columns(2)

    with col_end_nm:
        st.number_input(
            "End wavelength λ_end (nm)",
            key="end_nm",
            min_value=100.0,
            value=wavelength_from_shift(st.session_state.laser_rng, 3500.0)
            if "end_nm" not in st.session_state
            else st.session_state.end_nm,
            step=0.01,
            on_change=cb_end_from_nm,
            format="%.2f",
        )
    with col_end_shift:
        st.number_input(
            "End shift Δσ_end (cm⁻¹)",
            key="end_shift",
            value=3500.0,
            step=1.0,
            on_change=cb_end_from_shift,
        )

    # ---------- KPI-Dashboard ----------
    spec_range_shift = abs(st.session_state.end_shift - st.session_state.start_shift)
    spec_range_nm = abs(st.session_state.end_nm - st.session_state.start_nm)

    st.metric("Spectral range (cm⁻¹)", f"{spec_range_shift:,.0f}")
    st.metric("Spectral range (nm)", f"{spec_range_nm:,.2f}")
