import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="UNESCO Women Scientists in Conflict and Emergency Settings Mapping",
    layout="wide",
)

html_path = Path(__file__).parent / "dashboard.html"
html_content = html_path.read_text(encoding="utf-8")

st.components.v1.html(html_content, height=2600, scrolling=True)
