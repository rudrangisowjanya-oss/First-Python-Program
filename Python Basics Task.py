#Variables
name = "Sowjanya"
age = 20
Weight = 56
print(name)
print(age)
print(Weight)

#Data Types
a = 50
b = 10.5
c = "Internship"
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#Operators
#Arithmetic Operator
a = 60
b = 40
c = a+b
d = a-b
e = a*b
f = a/b
g = a%b
h = a**b
print("Addition : ", c)
print("Subtraction :",d)
print("Multiplication :",e)
print("Division :",f)
print("Modulus :",g)
print("Exponent :",f)

#Comparison Operators
print(10 > 5)
print(10 < 5)
print(10 == 5)
print(10 != 5)

#Logical Operators
x = True
y = False

print(x and y)
print(x or y)
print(not x)

#Loops
#For Loop
for i in range(1, 6):
    print(i)

#While Loop
count = 1

while count <= 5:
    print(count)
    count += 1

#Conditional Statements
#if Statement
age = 18

if age >= 18:
    print("Eligible to vote")  

#if-else Statement
num = 7

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")   

#functions       
#function without parameters
def name():
    print("Welcome to Sowjanya")

name()

#function with parameters
def add(a, b):
    return a + b

result = add(10, 20)
print(result)

print("Basic Python skills developed.")