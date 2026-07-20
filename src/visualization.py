import matplotlib.pyplot as plt
import seaborn as sns


def plot_missing_values(df):
    plt.figure(figsize=(12, 6))
    sns.heatmap(df.isnull(), cbar=False)
    plt.title("Missing Values")
    plt.tight_layout()
    plt.show()


def plot_aqi_trend(df, city):
    city_df = df[df["City"] == city]

    plt.figure(figsize=(14, 6))
    plt.plot(city_df["Date"], city_df["AQI"])
    plt.title(f"{city} AQI Trend")
    plt.xlabel("Date")
    plt.ylabel("AQI")
    plt.tight_layout()
    plt.show()


def plot_city_comparison(df):
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x="City", y="AQI")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_pm25_heatmap(df):
    pivot = df.pivot_table(
        values="PM2.5",
        index="Month",
        columns="City",
        aggfunc="mean"
    )

    plt.figure(figsize=(12, 6))
    sns.heatmap(pivot, cmap="Reds")
    plt.title("Average PM2.5 by Month and City")
    plt.tight_layout()
    plt.show()


def plot_seasonal_analysis(df):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x="Season", y="AQI")
    plt.title("Seasonal AQI Distribution")
    plt.tight_layout()
    plt.show()


def plot_correlation(df):
    plt.figure(figsize=(10, 8))
    sns.heatmap(
        df.corr(numeric_only=True),
        annot=True,
        cmap="coolwarm"
    )
    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.show()


def plot_top_polluted_cities(df):
    city_mean = (
        df.groupby("City")["AQI"]
        .mean()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(10, 6))
    city_mean.plot(kind="bar")
    plt.title("Average AQI by City")
    plt.ylabel("AQI")
    plt.tight_layout()
    plt.show()
