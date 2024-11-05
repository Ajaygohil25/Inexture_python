import pandas as pd 

df = pd.read_csv("dataFile.csv")

print("----Read from the file ------")
print(df)

# write in csv files 

df= pd.DataFrame([["ajay", "python", 4], ["gautam","AI", 3], ["Dwarkesh", "Python", 3]], columns=['Name','Training field', 'Rating'])

df.to_csv("dataFile.csv")

print("----After writing in the file ------")
print(df)