import pandas as pd

# Load dataset
data = pd.read_csv(r"C:\Users\Rudrangi Sowjanya\Downloads\Private_data.csv")

# Display first 5 rows
print(data.head())

# Check missing values
print(data.isnull().sum())

# Remove missing values
data = data.dropna()

# Remove duplicate rows
data = data.drop_duplicates()

# Display dataset information
print(data.info())

# Display statistical summary
print(data.describe())

# Save cleaned dataset
data.to_csv("Cleaned_Private_data.csv", index=False)

print("Dataset cleaned successfully.")