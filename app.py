# app.py
import streamlit as st
from spam_detector import predict_spam

st.title("📩 Spam Detection Web App")
st.write("Type a message below to check if it's spam or not.")

msg = st.text_area("Enter your message")

if st.button("Check"):
    result = predict_spam(msg)
    if result == 1:
        st.error("🚫 Spam Detected!")
    else:
        st.success("✅ Not Spam!")
