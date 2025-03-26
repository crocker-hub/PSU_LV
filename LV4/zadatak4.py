1.
Broj automobila u datasetu: 6699
2.
Tipovi podataka u dataframeu:
 name              object    
year               int64     
selling_price    float64     
km_driven          int64     
fuel              object     
seller_type       object     
transmission      object     
owner             object
mileage          float64
engine             int64
max_power        float64
seats              int64
dtype: object
3.
Najskuplji automobil:
name             BMW X7 xDrive 30d DPE
year                              2020
selling_price                15.789592
km_driven                         5000
fuel                            Diesel
seller_type                 Individual
transmission                 Automatic
owner                      First Owner
mileage                          13.38
engine                            2993
max_power                        265.0
seats                                7
Name: 2591, dtype: object
Najjeftiniji automobil:
name             Maruti 800 AC
year                      1997
selling_price        10.308919
km_driven                80000
fuel                    Petrol
seller_type         Individual
transmission            Manual
owner              Third Owner
mileage                   16.1
engine                     796
max_power                 37.0
seats                        4
Name: 4778, dtype: object
4.
Broj automobila proizvedenih 2012. godine: 575
5.
Automobil s najviše kilometara:
name             Maruti Wagon R LXI Minor
year                                 2010
selling_price                   12.175613
km_driven                          577414
fuel                               Petrol
seller_type                    Individual
transmission                       Manual
owner                        Second Owner
mileage                              18.9
engine                               1061
max_power                            67.0
seats                                   5
Name: 3067, dtype: object
Automobil s najmanje kilometara:
name             Maruti Eeco 5 STR With AC Plus HTR CNG
year                                               2011
selling_price                                  12.25009
km_driven                                             1
fuel                                                CNG
seller_type                                  Individual
transmission                                     Manual
owner                              Fourth & Above Owner
mileage                                            15.1
engine                                             1196
max_power                                          73.0
seats                                                 5
Name: 6514, dtype: object
6.
Najčešći broj sjedala: 5
7.
Prosječna kilometraža za dizel automobile: 88039.97 km
Prosječna kilometraža za benzinske automobile: 54101.88 km

kod: 
import pandas as pd

df = pd.read_csv('C:/Users/student/Desktop/cars_processed.csv')

num_cars = df.shape[0]
print(f'Broj automobila u datasetu: {num_cars}')

types = df.dtypes
print('Tipovi podataka u dataframeu:\n', types)

df_sorted = df.sort_values(by='selling_price')
most_expensive = df_sorted.iloc[-1]
least_expensive = df_sorted.iloc[0]
print(f'Najskuplji automobil:\n{most_expensive}')
print(f'Najjeftiniji automobil:\n{least_expensive}')

cars_2012 = df[df['year'] == 2012].shape[0]
print(f'Broj automobila proizvedenih 2012. godine: {cars_2012}')

most_km = df.iloc[df['km_driven'].idxmax()]
least_km = df.iloc[df['km_driven'].idxmin()]
print(f'Automobil s najviše kilometara:\n{most_km}')
print(f'Automobil s najmanje kilometara:\n{least_km}')

most_seats = df['seats'].mode()[0]
print(f'Najčešći broj sjedala: {most_seats}')

avg_km_diesel = df[df['fuel'] == 'Diesel']['km_driven'].mean()
avg_km_petrol = df[df['fuel'] == 'Petrol']['km_driven'].mean()
print(f'Prosječna kilometraža za dizel automobile: {avg_km_diesel:.2f} km')
print(f'Prosječna kilometraža za benzinske automobile: {avg_km_petrol:.2f} km')
