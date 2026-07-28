# install pandas
# pip install pandas

#import pandas
import pandas as pd

#load the student score dataset
import pandas as pd
data = pd.read_csv(r"C:\Users\Rudrangi Sowjanya\Downloads\Private_data.csv")
print(data)

#explore rows
print(data.shape)

#explore columns
print(data.columns)

#dataset information
print(data.info())

print("Dataset loaded successfully")