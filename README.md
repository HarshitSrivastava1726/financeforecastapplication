# financeforecastapplication
Help SME founders and finance heads predict cash flow, spot risk early, and make better decisions—without hiring a full finance team.
finance-forecast-mvp/
│
├── app.py                     # Streamlit entry point
├── requirements.txt
│
├── data/
│   ├── sample_input.xlsx      # Example SME data
│   └── uploads/               # User uploads
│
├── core/
│   ├── __init__.py
│   ├── loader.py              # File loading & validation
│   ├── forecast.py            # Cash-flow forecasting logic
│   ├── risk.py                # Risk & alert logic
│
├── ui/
│   ├── charts.py              # Plotly charts
│   └── messages.py            # Human-readable insights
│
├── auth/
│   ├── auth.py                # Login / trial logic
│
├── config/
│   ├── settings.py            # Constants & thresholds
│
└── utils/
    └── helpers.py
