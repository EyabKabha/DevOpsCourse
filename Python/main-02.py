#   1. Write a python program to swap two numbers using a third variable

#Define values.
num1 = 10
num2 = 5
temp = 0  # temp value
print(f'Before Swapping\n{num1} {num2}')

# Swap the numbers
temp = num1
num1 = num2
num2 = temp
print(f'After Swapping\n{num1} {num2}')


#  2. Write a python program to swap two numbers without using third variable
print('----Swapping the numbers without third variable----')
num1, num2 = num2, num1
print(num1,num2)

#  3. Write a python program to read two numbers and find the sum of their cubes

def sumOfCubes(n):
    sum = 0
    for i in range(1, n+1):
        sum += i*i*i
                    # 1 * 1 * 1 = 1
                    # 2 * 2 * 2 = 8
                    # 3 * 3 * 3 = 27
                    # 4 * 4 * 4 = 64
                    # 5 * 5 * 5 = 125
                    #Sum = 225
    return sum
n = 5
print(sumOfCubes(n)) #Call the function

#  4. Write a python program to read three numbers and if any two variables are equal , print that number

number1 = input("Please enter first number ")
number2 = input("Please enter second number ")
number3 = input("Please enter third number ")

if (number1 == number2) or (number1 == number3):
    equalnumber = number1
elif (number2 == number1) or (number2 == number3):
    equalnumber = number2
else:
    equalnumber = 'Any numbers are equal.' # in case we do not have numbers equal.

print(f"The Equal number is: {equalnumber}")

#  5. Write a python program to read three numbers and find the smallest among them

# number1 = input("Please enter first number ")
# number2 = input("Please enter second number ")
# number3 = input("Please enter third number ")

if (number1 < number2) and (number1 < number3):
    smallest = number1
elif (number2 < number1) and (number2 < number3):
    smallest = number2
else:
    smallest = number3

print(f"The smallest number is {smallest}")
