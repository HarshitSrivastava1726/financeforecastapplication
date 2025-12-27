def detect_risk(forecast_df, threshold):
    risk_point = forecast_df[forecast_df["balance"] < threshold]

    if risk_point.empty:
        return "GREEN", "No cash risk detected in forecast period."

    first_hit = risk_point.iloc[0]
    days_left = (first_hit["week"] - forecast_df["week"].iloc[0]).days

    message = f"⚠️ Cash may drop below threshold in {days_left} days."
    return "RED", message
