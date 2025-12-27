import streamlit as st
from core.loader import load_file
from core.forecast import forecast_cashflow
from core.risk import detect_risk

st.title("SME Cash Flow Forecaster")

file = st.file_uploader("Upload transaction file")

opening_balance = st.number_input("Opening Cash Balance", value=100000.0)
threshold = st.number_input("Risk Threshold", value=50000.0)

if file:
    df = load_file(file)
    forecast = forecast_cashflow(df, opening_balance)
    status, msg = detect_risk(forecast, threshold)

    st.subheader("Risk Status")
    st.write(status)
    st.warning(msg)

    st.line_chart(forecast.set_index("week")["balance"])
