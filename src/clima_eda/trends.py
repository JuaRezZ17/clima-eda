import numpy as np
import pandas as pd

def annual_agg(df: pd.DataFrame) -> pd.DataFrame:
    return (df.groupby(["city","year"])\
            .agg(t_mean_year=("t_mean","mean"),
                precip_year=("precip_mm","sum"))\
            .reset_index())

def trend_slope(df: pd.DataFrame, value: str = "t_mean") -> pd.DataFrame:
    yearly = (df.groupby(["city","year"])[value].mean().reset_index())
    rows = []
    for city, sub in yearly.groupby("city"):
        if sub["year"].nunique() < 5:
            continue
        x = sub["year"].values
        y = sub[value].values
        p = np.polyfit(x, y, 1)
        y_pred = np.polyval(p, x)
        ss_res = ((y - y_pred)**2).sum()
        ss_tot = ((y - y.mean())**2).sum()
        r2 = 1 - ss_res/ss_tot if ss_tot > 0 else np.nan
        rows.append({
            "city": city,
            "trend_per_year": p[0],
            "trend_per_decade": p[0]*10,
            "r2": r2,
            "n_years": int(sub["year"].nunique()),
            "year_start": int(sub["year"].min()),
            "year_end": int(sub["year"].max()),
        })
    return pd.DataFrame(rows)

def correlation_temp_precip(df: pd.DataFrame) -> pd.DataFrame:
    out = []
    for city, sub in df.groupby("city"):
        if {"t_mean","precip_mm"}.issubset(sub.columns) and sub[["t_mean","precip_mm"]].dropna().shape[0] >= 10:
            out.append({"city": city, "corr_t_precip": sub["t_mean"].corr(sub["precip_mm"])})
    return pd.DataFrame(out)

def rank_cities_by_warming(trends: pd.DataFrame, top: int = 5):
    t = trends.sort_values("trend_per_decade", ascending=False)
    return t.head(top), t.tail(top)