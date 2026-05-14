import streamlit as st

st.set_page_config(page_title="Knowledge Based System", layout="wide")

st.title("🛡️ Cybersecurity Knowledge Based System")

st.write("Welcome to the Knowledge Based System project built using Streamlit.")

st.header("User Input")

issue = st.text_input("Enter the cybersecurity issue:")

if st.button("Analyze"):
    if issue:
        st.success(f"Analysis completed for: {issue}")
        st.info("This is a placeholder response from the inference engine.")
    else:
        st.warning("Please enter an issue first.")
