import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    """
    `visits`: 2 columns
        * visit_id
        * customer_id
    
    `transactions`: 3 columns
        * transaction_id
        * visit_id
        * amount
    """

    # all `visit_id`s that have not made a purchase
    visits_no_transactions_mask = ~visits['visit_id'].isin(transactions['visit_id'])

    visits_no_transactions_df = (
        visits.loc[visits_no_transactions_mask]  # filter visits to ones without transactions
        .groupby('customer_id')

        # count how many no transaction visits each customer had
        .agg(count_no_trans=('visit_id', 'count'))

        # sort them in ascending order
        .sort_values(by='count_no_trans')
    )

    # make the index its own column since that is the customer_id
    # (since we grouped by that)
    return visits_no_transactions_df.reset_index()