def create_time_features(df):
    """Extract useful features from Date column."""

    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["Day"] = df["Date"].dt.day
    df["Weekday"] = df["Date"].dt.day_name()

    season_map = {
        12: "Winter",
        1: "Winter",
        2: "Winter",
        3: "Summer",
        4: "Summer",
        5: "Summer",
        6: "Monsoon",
        7: "Monsoon",
        8: "Monsoon",
        9: "Monsoon",
        10: "Post-Monsoon",
        11: "Post-Monsoon",
    }

    df["Season"] = df["Month"].map(season_map)

    return df
