import pandas as pd
data=pd.read_csv("Weather Data.csv")

#to check the first five rows
data.head()

#to check how many rows and colums 
data.shape  

#to check indexes
print(data.index)  #RangeIndex(start=0, stop=8784, step=1)

# to check column names
print(data.columns)  

#to check datatypes of columns
print(data.dtypes)

# to check unique values in specific column  , works only on single column
print( data["Weather"].unique() )

#to check how many unique values are there in every column
print( data.nunique() )

#to check total numbers of non null value
print( data.count() )    # there are no null values

# to check unique values with their total counts in single column
print(data["Weather"].value_counts())

# to get basic information
print(data.info())

#Find all the unique "Wind Speed" in the data
print(data['Wind Speed_km/h'].unique())
print(data["Wind Speed_km/h"].nunique())

# Find the number of times when the Weather is exactly clear  , there are 3 methods
print( data["Weather"].value_counts())   #1st
print(data.groupby("Weather").get_group("Clear"))   #2nd
print(data[data.Weather=="Clear"])

# Find the number of times when the Wind speed was exacty 4km
print(data["Wind Speed_km/h"].value_counts())  #474   1st method
print(data.groupby("Wind Speed_km/h").get_group(4))  #2nd method
print(data[data["Wind Speed_km/h"] == 4])   #3rd method

# Find out the null values in the data
print(data.isnull().sum())   #  1st method
print(data.count())   #2nd method

# Rename the column name Weateh to Weather Condition
print(data.rename(columns={"Weather":"Weather Condition"}))    #this is only temporary, if inpalce =True than its permanent

# What is the mean of Visibility
print( data["Visibility_km"].mean() )

# What is standard deviation of Presseure
print( data["Press_kPa"].std() )

# What is the variance od relative humidity
print( data["Rel Hum_%"].var() )

# Find all the instances when Snow was recorded
print( data[data["Weather"]=="Snow"])
print(data[ data["Weather"].str.contains("Snow")])   # this gives data wherever the snow word is present

#Find all instances when wind speed is above 24 and visibility is 25
print(data[(data["Wind Speed_km/h"]>24) & (data["Visibility_km"]==25)])

# What is the min and max value of each coloumn against each Weather Condition
print(data.groupby("Weather").min())
print(data.groupby("Weather").max())

# Show all the records where weather is fog
print(data.groupby("Weather").get_group("Fog"))
print(data[data["Weather"]=="Fog"])

# Find all the instances where weather is clear or visibility is above 40
print( data[(data["Weather"]=="Clear") | (data["Visibility_km"] > 40)])

# Find all the instances when Weather is clear and humidity is greater than 50,   or visibility is above 40
print( data[ ( (data["Weather"]=="Clear") & (data['Rel Hum_%'] > 50) ) | (data["Visibility_km"] > 40)] ) 