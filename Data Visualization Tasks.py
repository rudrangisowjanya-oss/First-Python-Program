#Data Visualization Tasks
#Import Matplotlib
import matplotlib.pyplot as plt

#Scatter Plot
# Data
x = [1, 2, 3, 4, 5]
y = [10, 15, 20, 25, 30]

#Scatter Plot
plt.scatter(x, y)

# Labels
plt.title("Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# Show Graph
plt.show()

#Bar Chart
# Data
students = ["A", "B", "C", "D", "E"]
marks = [85, 90, 75, 80, 95]

# Bar Chart
plt.bar(students, marks)

# Labels
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

# Show Graph
plt.show()

#Line Chart
# Data
days = [1, 2, 3, 4, 5]
sales = [100, 120, 150, 130, 170]

# Line Chart
plt.plot(days, sales)

# Labels
plt.title("Sales Over 5 Days")
plt.xlabel("Days")
plt.ylabel("Sales")

# Show Graph
plt.show()

#Expected Outcome
print("Basic Chart Created")