def apply_filters(df, region=None, state=None):
    filtered_df = df

    if region:
        filtered_df = filtered_df[filtered_df["Region"] == region]

    if state:
        filtered_df = filtered_df[filtered_df["State"] == state]

    return filtered_df
