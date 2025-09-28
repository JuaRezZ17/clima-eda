import matplotlib.pyplot as plt

def plot_city_timeseries(df, city, value="t_mean", rolling=True):
    sub = df[df["city"]==city].sort_values(["year","month"]).copy()
    x = sub["year"] + (sub["month"]-1)/12
    plt.plot(x, sub[value], label=value)
    roll_col = f"{value}_roll12"
    if rolling and roll_col in sub.columns:
        plt.plot(x, sub[roll_col], label=roll_col)
    plt.title(f"{city} - {value}")
    plt.xlabel("Año"); plt.ylabel(value)
    plt.legend(); plt.tight_layout(); plt.show()

def plot_rankings_bar(df, value="trend_per_decade", title="Tendencia (°C/década)"):
    plt.bar(df["city"], df[value])
    plt.xticks(rotation=45, ha="right")
    plt.title(title); plt.ylabel(value)
    plt.tight_layout(); plt.show()

def plot_distribution(df, value="t_anomaly"):
    groups = [g[value].dropna().values for _, g in df.groupby("city")]
    labels = list(df["city"].drop_duplicates())
    plt.boxplot(groups)
    plt.xticks(range(1, len(labels)+1), labels, rotation=45)
    plt.title(f"Distribución de {value} por ciudad")
    plt.tight_layout(); plt.show()

def plot_scatter(df, x="t_anomaly", y="precip_mm"):
    sub = df[[x,y]].dropna()
    plt.scatter(sub[x], sub[y])
    plt.xlabel(x); plt.ylabel(y)
    plt.title(f"{y} vs {x}")
    plt.tight_layout(); plt.show()