import pandas as pd
hour=pd.read_csv('hour.csv')
print(hour.loc[3, 'count'])