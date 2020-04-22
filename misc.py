import pandas as pd
import os

#MISC file for testing, ignore or delete

DataReading = "data.csv"
DataTraining = "training_data.csv"

df1 = pd.read_csv(os.path.join(os.getcwd(),DataReading),encoding = "ISO-8859-1", engine="python", dtype=str, error_bad_lines=False)
df2 = pd.read_csv(os.path.join(os.getcwd(),DataTraining), encoding = "ISO-8859-1", engine="python", error_bad_lines=False)

for i in range(df1.shape[0]):
    #Check to see if this user has been compared before, if its not, get their values
    if df1.loc[i]['Name'] in df2['Name']:
        print(df1.iloc[i,0:])

print(df1.shape[0])
print("------")
#print(value2)