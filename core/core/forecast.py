import pandas as pd

def forecast_cashflow(df, opening_balance, periods=12):
    df["week"] = df["date"].dt.to_period("W").apply(lambda r: r.start_time)

    weekly = df.groupby(["week", "type"])["amount"].sum().unstack(fill_value=0)
    weekly["net"] = weekly.get("inflow", 0) - weekly.get("outflow", 0)

    avg_net = weekly["net"].mean()
    future_weeks = pd.date_range(
        start=weekly.index.max(),
        periods=periods + 1,
        freq="W"
    )[1:]

    forecast = pd.DataFrame({"week": future_weeks})
    forecast["net"] = avg_net
    forecast["balance"] = opening_balance + forecast["net"].cumsum()

    return forecast
