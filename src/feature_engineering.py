import pandas as pd

def create_features(df):
    df["revenue_growth"] = df["revenue"].pct_change()
    df["profit_margin"] = df["net_income"] / df["revenue"]
    return df
