
import pandas as pd

from components.constants import class_categories

def load_data_and_clean_data():

# Load Data

    df = pd.read_csv('data/Meteorite_Landings.csv')

    # Drop null values
    df = df.dropna()

    # Drop irrelevant columns
    df = df.drop(['nametype', 'GeoLocation'], axis=1)

    # Rename columns
    df = df.rename(columns={'mass (g)': 'mass', 'recclass':'class', 'reclat': 'latitude', 'reclong': 'longitude'})

    # Convert data types
    df['year'] = df['year'].astype(int)
    
    # Convert mass from grams to kilograms
    df['mass'] = df['mass'] / 1000
    df['mass'] = df['mass'].astype(int)

    # Sort by mass descending
    df = df.sort_values(by='mass', ascending=False)

    # Choose top 500 values
    df = df.iloc[:500]

    # Apply the class categories to the class column and create a new column called class_cat
    df['class_cat'] = df['class'].apply(lambda x: [k for k, v in class_categories.items() if x in v][0])

    # print(df.columns)
    # print(df.head())
    # print(len(df))
    # print(df.dtypes)
    # print(df.describe())

    return df

# %%
