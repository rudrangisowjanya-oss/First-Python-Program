# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
df = pd.read_csv(r"C:\Users\Rudrangi Sowjanya\OneDrive\Desktop\Internship\Hours_Scores.csv")

# Display first 5 rows
print(df.head())

# Select input and output columns
# Replace these column names with the ones in your dataset
X = df[['Hours']]      # Input column
y = df['Scores']       # Target column

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test data
predictions = model.predict(X_test)
y_pred = model.predict(X_test)

# Compare actual and predicted values
results = pd.DataFrame({
    "Actual Score": y_test.values,
    "Predicted Score": predictions
})
# Calculate evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Display results
print("Model Evaluation Results")
print("------------------------")
print("Mean Absolute Error (MAE):", round(mae, 2))
print("Mean Squared Error (MSE):", round(mse, 2))
print("R² Score:", round(r2, 2))
print(results)



