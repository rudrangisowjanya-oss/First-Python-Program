#import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#load the dataset
data = pd.read_csv(r"C:\Users\Rudrangi Sowjanya\OneDrive\Desktop\Internship\Hours_Scores.csv")

#Display the first 5 rows
print("First 5 Rows:")
print(data.head())

#select input (x) and output (y)
x = data[['Hours']]
y = data['Scores']

#split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

#create the Linear Regression Model
model = LinearRegression()

# Train the model
model.fit(x_train, y_train)

print("\n Model Trained Successfully!")