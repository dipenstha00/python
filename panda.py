"""import pandas as pd
df = pd.read_csv('bills.csv',index_col = 'SN')

print(df)

data = {'name':['Ram', 'Shyam', 'Hari'],
        'age':[34,56,78],
        'add':['Kathmandu','Bhaktapur','Lalitpur']}
df = pd.DataFrame(data)
print(df)

import csv
data = ['Oreo',2,20]
with open('clean_data.csv','w') as file:
        x = csv.writer(file)
        x.writerow(data)

data = [['Product Name', 'Quantity', 'Price'],
        ['Oreo', 2, 20],
        ['KitKat', 3, 50],
        ['Snickers', 2, 90]]
with open('clean_data.csv','a') as file:
        x = csv.writer(file)
        x.writerows(data)

import csv
with open('clean_data.csv','r') as file:
        reader = csv.DictReader(file)
        for data in reader:
                print(data)

import pandas as pd
df = pd.read_csv('data.csv',index_col = 'name')
#print(df.head(3))
#print(df.tail(4))
#print(df.iloc[1:4])    #considers the index data
#print(df.loc[2:4])      #considers the value data
print(df.loc['Shyam':'Sita'])   #searching with name or any other data field, we need to define the index_col

import pandas as pd
df = pd.read_csv('data.csv',index_col = 'sn')
print(df[df['add'] == 'Kathmandu'])

import pandas as pd
df = pd.read_csv('data.csv',index_col = 'sn')       #to filter using conditions
print(df[df['age'] > 24])

import pandas as pd
df = pd.read_csv('data.csv',index_col = 'sn')       #to copy the data that meet the conditions and copy to the file data.csv
data = df[(df['age'] > 24) & (df['add'] == 'Kathmandu')]
data.to_csv('data1.csv')

import csv
data = [5,'Jamal', 55, 'Pokhara']
with open('data1.csv','a') as file:
    x = csv.writer(file)
    x.writerow(data)

import csv
add_data = []
with open('data.csv','r') as file:
    reader = csv.DictReader(file)
    for data in reader:
        print(data) #to read as dictionary
        #add_data.append(data) #to read as list
#print(add_data)"""


import pandas as pd
data1 = {'name' : ['Ram', 'Shyam', 'Hari'],
         'age' : [24,53,32],
         'add' : ['Kathmadnu','Pokhara', 'Bhaktapur']}
data2 = {'name' : ['Ram', 'Shyam', 'Hari'],
         'age' : [24,53,32],
         'add' : ['Kathmadnu','Pokhara', 'Bhaktapur']
        }

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df = pd.concat([df1,df2])
print(df)