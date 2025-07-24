import pandas as pd

df = pd.read_csv('customers.csv')

df = df.loc[df['Country'] == 'Colombia']

df['AverageOrderValue'] = round(df['TotalSpent'] / df['Orders'], 2)

def segment(row):
    if row['AverageOrderValue'] < 50:
        return 'Low'
    elif row['AverageOrderValue'] >= 50 and row['AverageOrderValue'] <= 200:
        return 'Medium'
    else:
        return 'High'

df['Segment'] = df.apply(segment, axis=1)

print(df.head())

df.to_csv('colombian_customers.csv')