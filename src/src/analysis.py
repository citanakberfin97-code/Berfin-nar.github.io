import pandas as pd

def get_summary(df):
    summary = {
        "total_revenue": df["revenue"].sum(),
        "avg_profit": df["net_income"].mean(),
        "max_revenue": df["revenue"].max()
    }
    return summary
