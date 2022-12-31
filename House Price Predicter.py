import pandas as pd
from sklearn import linear_model

prices_df = pd.read_csv('C:\\Users\\LAXMI YADAV\\Downloads\\HOUSE PRICES.csv', sep=',', header=0)

x = prices_df[['Area', 'No. of Bedrooms', 'SwimmingPool', 'CarParking', 'WashingMachine',	'AC', 'Wifi', "Children'splayarea", 'LiftAvailable', 'BED', 'Microwave', 'TV', 'DiningTable', 'Sofa', 'Wardrobe', 'Refrigerator']]
y = prices_df[['Price']]

regr = linear_model.LinearRegression()
regr.fit(x,y)

area = (input('Enter area: '))
area = float(area)
bedrooms = int(input("Enter no. of bedrooms: "))
swim_pool = int(input("Is there swimming pool: "))
car_park = int(input("Is there car parking: "))
wash = int(input("Do you have a washing machine: "))
ac = int(input('AC ?: '))
w = int(input('Wifi ?: '))
play_area = int(input("Do you have a play area: "))
lift = int(input('Do you have a lift: '))
bed = int(input('Do you have bed: '))
microwave = int(input('Do you have microwave: '))
tv = int(input('Do you have a tv: '))
din_table = int(input('Do you have a dining table: '))
sofa = int(input('Do you have a sofa: '))
wardrobe = int(input('Do you have a wardrobe: '))
ref = int(input('Do you have a refrigerator: '))


predicted_price = regr.predict([[area, bedrooms, swim_pool, car_park, wash, ac, w, play_area, lift, bed, microwave, tv, din_table, sofa, wardrobe, ref]])
print(predicted_price)