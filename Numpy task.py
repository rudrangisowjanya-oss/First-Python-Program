#install numpy
#pip install numpy

#import munpy
import numpy as np

#1D Array
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr)

#2D Array
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr)

#Aray Indexing
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
print(arr[2])
print(arr[-1])

# 2D Array Indexing
import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60]])

print(arr[0, 1])
print(arr[1, 2])

#Array Slicing
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])
print(arr[:3])
print(arr[2:])

#Mathematical Operations
#Addition
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)

#Subtraction
print(a - b)

#Multiplication
print(a * b)

#Division
print(a / b)

#Array Statistics
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Sum =", np.sum(arr))
print("Mean =", np.mean(arr))
print("Maximum =", np.max(arr))
print("Minimum =", np.min(arr))

#Reshaping Arrays
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

new_arr = arr.reshape(2, 3)

print(new_arr)

#Special Arrays
#Zeros Array
import numpy as np

print(np.zeros((2, 3)))

#Ones Array
import numpy as np

print(np.ones((2, 3)))

#Identity Matrix
import numpy as np

print(np.eye(3))

#Basic Array Calculate Program
#sum and average of an array
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print("Array:", numbers)
print("Sum:", np.sum(numbers))
print("Average:", np.mean(numbers))

#addition of two arrays
import numpy as np

array1 = np.array([10, 20, 30])
array2 = np.array([40, 50, 60])

result = array1 + array2

print("Array 1:", array1)
print("Array 2:", array2)
print("Addition:", result)

print("NumPy fundamentals completed")