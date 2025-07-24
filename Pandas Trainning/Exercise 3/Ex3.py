import pandas as pd

df = pd.read_csv('Exercise 3/orders.csv')

df[['DeliveryDate', 'ShipDate']] = df[['DeliveryDate', 'ShipDate']].apply(pd.to_datetime)

df['DeliveryTime'] = (df['DeliveryDate'] - df['ShipDate']).dt.days

def isLate(row):
    if row['DeliveryTime'] > 7:
        return 1
    else:
        return 0
    
df['isLate'] = df.apply(isLate, axis=1)

print(df.head())