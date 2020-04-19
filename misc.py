import pandas as pd
import os

DataReading = "data.csv"
DataTraining = "training_data.csv"

df = pd.read_csv(os.path.join(os.getcwd(),DataReading),encoding = "ISO-8859-1", engine="python")

value1 = df.loc[df['Name']=='Csbtkrillex'].index[0]

value2 = df.iloc[value1, 0:].tolist()

print(df.shape[0])
print("------")
#print(value2)