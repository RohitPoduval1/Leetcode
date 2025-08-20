import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # get series of emails with how many times they appear
    # index is email and number of occurences is the value
    vc_series = person['email'].value_counts()

    return (
        vc_series[vc_series.values > 1]  # filter to emails that occur more than once
        .index                           # get the actual emails
        .rename('Email')                 # rename Series to 'Email' from 'email'
        .to_frame()                      # convert to DataFrame for answer
    )