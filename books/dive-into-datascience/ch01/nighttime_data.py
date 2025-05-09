import pandas as pd
hour=pd.read_csv('hour.csv')

print(hour.loc[3, 'count'])
print(hour.loc[2:4, 'registered'])
print(hour.loc[hour['hr']<5, 'registered'].mean())

# check for ridership counts on colder early mornings or warmer early mornings:

print(hour.loc[(hour['hr']<5) & (hour['temp']<.50), 'count'].mean())
print(hour.loc[(hour['hr']<5) & (hour['temp']>.50), 'count'].mean())