import streamlit as st
from streamlit_ace import st_ace

code = st_ace(language="python", theme="monokai", key="editor1")
st.write("You wrote:")
st.code(code or "")
