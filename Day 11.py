# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset
# Replace 'student_scores.csv' with your dataset name
data = pd.read_csv(r"C:\Users\Rudrangi Sowjanya\OneDrive\Desktop\Internship\Hours_Scores.csv")

# Features (Study Hours) and Target (Scores)
X = data[['Hours']]
y = data['Scores']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# -------------------------------
# Prediction App
# -------------------------------
print("===== Student Score Prediction App =====")

while True:
    try:
        hours = float(input("\nEnter study hours: "))

        # Predict score
        predicted_score = model.predict([[hours]])

        print(f"Predicted Score: {predicted_score[0]:.2f}")

        choice = input("\nDo you want to predict again? (yes/no): ").lower()

        if choice != "yes":
            print("Thank you for using the Prediction App!")
            break

    except ValueError:
        print("Please enter a valid numeric value.")