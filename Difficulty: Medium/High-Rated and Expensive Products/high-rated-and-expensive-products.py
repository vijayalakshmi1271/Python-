def filter_high_rated_expensive(df):
    result = df[
        (df["rating"] >= 4.5) &
        (df["quantity_in_stock"] > 0) &
        (df["price"] >= 300.0)
    ][["product_id", "product_name", "rating", "quantity_in_stock", "price"]]
    return result