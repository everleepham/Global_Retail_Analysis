import pandas as pd


def clean_data(filepath):
    df = pd.read_csv(filepath)

    df = df.drop_duplicates()
    df['Order.Date'] = pd.to_datetime(df['Order.Date'])

    df['Year'] = df['Order.Date'].dt.year

    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].mean())

    df = df.dropna()
    print(df.dtypes)

    return df

def test_clean_data():
    filepath = 'data/superstore.csv'
    cleaned_df = clean_data(filepath)
    assert cleaned_df.isnull().sum().sum() == 0
    assert len(cleaned_df) == 51289
    assert cleaned_df['Order.ID'].is_unique
    assert cleaned_df['Customer.ID'].is_unique
    assert cleaned_df['Product.ID'].is_unique
    assert cleaned_df['Year'].dt.year.min() == 2011
    assert cleaned_df['Year'].dt.year.max() == 2014
    


if __name__ == '__main__':
    filepath = 'data/superstore.csv'
    cleaned_df = clean_data(filepath)
    print(cleaned_df.head(10))
    print(cleaned_df.tail(10))

    
