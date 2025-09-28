import pandas as pd

def climatology(df: pd.DataFrame, value: str = "t_mean") -> pd.DataFrame:
    base = (df.groupby(["city","month"])[value]
            .mean().rename(f"{value}_clim").reset_index())
    return base

def add_anomaly(df: pd.DataFrame, clim: pd.DataFrame, value: str = "t_mean") -> pd.DataFrame:
    out = df.merge(clim, on=["city","month"], how="left")
    out[f"{value}_anomaly"] = out[value] - out[f"{value}_clim"]
    return out

def rolling_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.sort_values(["city","year","month"]).copy()
    if "t_mean" in out.columns:
        out["t_mean_roll12"] = (out.groupby("city")["t_mean"].transform(lambda s: s.rolling(12, min_periods=6).mean()))
    if "precip_mm" in out.columns:
        out["precip_roll12"] = (out.groupby("city")["precip_mm"].transform(lambda s: s.rolling(12, min_periods=6).sum()))
    return out