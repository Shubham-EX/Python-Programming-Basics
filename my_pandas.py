import pandas as pd

SER = ["shubh",18]
print(SER[1])

DICT = {
    "NAME":['shubham','viny','prince'],
    "AGE": [20,19,20]
    }

#DataFrames are versatile structures for representing tabular data.
df = pd.DataFrame(DICT)
print(df)

#accesing column
print("Age colomn\n",df['AGE']) #column age

#accesing row
print("row 1\n",df.iloc[1]) #row 1





df = pd.read_csv('filecsv.csv')
print(df)

# Display the first few rows of a DataFrame.
print(df.head(1))

#Display the last few rows of a DataFrame.
print(df.tail(1))

#Print the DataFrame's shape (number of rows and columns)
print(df.shape)

#Generate a summary of the DataFrame's statistical properties.
print(df.describe())

#Display information about the DataFrame's structure, including data types, memory usage, and index information.
print("info:",df.info())

#Return a DataFrame indicating missing values.
print(df.isnull())


#sorting 
print(df.sort_values('age'))


print("------------------------------------------------------------------------------")


dict = {
    "Name" : ["shubh","viny","Prince","Disha"],
    "Age"  : [20,20,19,18],
    "city" : ["Mehsana","Ahmedabad","USA","USA"]
}

df = pd.DataFrame(dict)
print(df)

#shape gives a total rows and column used in dataframe
print("\nshape:",df.shape)

#give definds some rows from the end
print("\ntail:",df.tail(2))

#give disctiption about dataframe
print("\ndescrible",df.describe())

#sum()
print("\nsum:",df.sum())






""" 
read_csv(), read_excel(), etc.: Reading data from various file formats.
head(), tail(), info(): Previewing and obtaining information about the DataFrame.
**loc[], iloc[]: Selecting rows and columns by label or position.

"""

import numpy as np

#creating dataframe random

newdf = pd.DataFrame(np.random.rand(200,4),index = np.arange(200))

print(newdf)

