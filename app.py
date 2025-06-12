import streamlit as st


st.set_page_config(page_title="Optics Toolkit", page_icon="🔬")
# st.title("🔬 Calculators Suite")
st.markdown(
    """
    """
)


pages = {
    "Calculators": [
        st.Page("pages/geometry_calcs.py", title="optics Geometry", icon="🔄"),
        st.Page("pages/raman_calc.py", title="Raman shift", icon="🔄"),
    ],
}

pg = st.navigation(pages, position="sidebar", expanded=True)
pg.run()
