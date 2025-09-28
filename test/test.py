import pandas as pd
import numpy as np
from clima_eda.trends import trend_slope

def test_trend_slope_sign():
    years = np.arange(2000, 2011)
    t = 15 + 0.02*(years - 2000)
    df = pd.DataFrame({"city":"Test","year":years,"t_mean":t})
    res = trend_slope(df)
    slope = float(res.loc[res["city"]=="Test","trend_per_year"])
    assert 0.015 < slope < 0.03

def test_merge_shape_no_loss():
    temp = pd.DataFrame({"city":["A","A"],"year":[2020,2020],"month":[1,2],"t_mean":[10,11]})
    precip = pd.DataFrame({"city":["A","A"],"year":[2020,2020],"month":[1,2],"precip_mm":[5,6]})
    merged = temp.merge(precip, on=["city","year","month"], how="inner")
    assert merged.shape[0] == 2

def test_required_columns_present():
    df = pd.DataFrame({"city":["A"],"year":[2020],"month":[1],"t_mean":[10.0]})
    for col in ["city","year","month","t_mean"]:
        assert col in df.columns