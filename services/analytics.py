def get_kpis(df):
    total_sales = float(df["Sales"].sum())
    total_profit = float(df["Profit"].sum())
    total_orders = int(df["Order ID"].nunique())

    return {
        "total_sales": round(total_sales, 2),
        "total_profit": round(total_profit, 2),
        "total_orders": total_orders
    }


def profit_by_subcategory(df):
    grouped = (
        df.groupby("Sub-Category")["Profit"]
        .sum()
        .sort_values(ascending=False)
    )

    return {
        "labels": grouped.index.tolist(),
        "values": grouped.values.tolist()
    }


def sales_by_subcategory(df):
    grouped = (
        df.groupby("Sub-Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    return {
        "labels": grouped.index.tolist(),
        "values": grouped.values.tolist()
    }


def sales_by_category(df):
    grouped = (
        df.groupby("Category")["Sales"]
        .sum()
    )

    return {
        "labels": grouped.index.tolist(),
        "values": grouped.values.tolist()
    }


def profit_by_category(df):
    grouped = (
        df.groupby("Category")["Profit"]
        .sum()
    )

    return {
        "labels": grouped.index.tolist(),
        "values": grouped.values.tolist()
    }
