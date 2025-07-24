import pandas as pd

df = pd.read_csv('Pandas Trainning/Exercise 3/orders.csv')

df[['DeliveryDate', 'ShipDate']] = df[['DeliveryDate', 'ShipDate']].apply(pd.to_datetime)

df['DeliveryTime'] = (df['DeliveryDate'] - df['ShipDate']).dt.days

def isLate(row):
    if row['DeliveryTime'] > 7:
        return 1
    else:
        return 0
    
df['isLate'] = df.apply(isLate, axis=1)

df = df[df['DeliveryDate'].notna()]

df2 = df.groupby(by='Status')['DeliveryTime'].mean()

df.to_csv('Pandas Trainning/Exercise 3/CleanOrders.csv')
df2.to_csv('Pandas Trainning/Exercise 3/ordersSummary.csv')