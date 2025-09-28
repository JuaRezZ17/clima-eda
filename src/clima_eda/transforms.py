import pandas as pd

def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    return df.rename(columns=lambda c: c.strip().lower().replace(" ", "_"))

def ensure_year_month(df: pd.DataFrame, date_col: str = "date") -> pd.DataFrame:
    if date_col in df.columns:
        d = pd.to_datetime(df[date_col], errors="coerce")
        df["year"] = d.dt.year
        df["month"] = d.dt.month
    return df

def monthly_aggregate(df: pd.DataFrame, group_cols=("city","year","month"), agg_map=None) -> pd.DataFrame:
    agg_map = agg_map or {"t_mean": "mean", "t_max":"mean", "t_min":"mean", "precip_mm":"sum"}
    keep_cols = [c for c in agg_map.keys() if c in df.columns]
    return (df.groupby(list(group_cols))[keep_cols]
            .agg(agg_map).reset_index())

def standardize_city_country(df: pd.DataFrame) -> pd.DataFrame:
    if "city" in df: df["city"] = df["city"].astype(str).str.strip().str.title()
    if "country" in df: df["country"] = df["country"].astype(str).str.strip().str.title()
    return df

def build_key(df: pd.DataFrame) -> pd.DataFrame:
    df["key"] = df["city"] + "_" + df["year"].astype(str) + "_" + df["month"].astype(str)
    return df