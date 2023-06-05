import pandas as pd

if __name__ == '__main__':
    sales_data_0 = pd.read_csv("./data/daily_sales_data_0.csv")
    sales_data_1 = pd.read_csv("./data/daily_sales_data_1.csv")
    sales_data_2 = pd.read_csv("./data/daily_sales_data_2.csv")

    output_sales_data = pd.concat([sales_data_0, sales_data_1, sales_data_2], ignore_index=True)
    output_sales_data = output_sales_data.loc[output_sales_data['product'] == 'pink morsel']

    output_sales_data["price"] = output_sales_data["price"].str.replace('$', '')
    output_sales_data["price"] = output_sales_data["price"].astype(float)
    output_sales_data["sales"] = output_sales_data.apply(lambda row: row.price * float(row.quantity), axis=1)
    output_sales_data.dropna()
    output_sales_data = output_sales_data[['sales', 'date', 'region']]

    output_sales_data.to_csv("./data/output_sales_data.csv", index=False)
