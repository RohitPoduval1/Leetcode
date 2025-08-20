import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    # 3 columns, id, name, customerId
    merged_df = customers.merge(orders, how='outer', left_on='id', right_on='customerId')

    return (
        merged_df.loc[merged_df['customerId'].isna()]  # df of customers who never order
        .loc[:, 'name']       # get only name column (becomes Series)
        .rename('Customers')  # rename Series to "Customers" from "name"
        .to_frame()           # convert to DataFrame for answer
    )
    