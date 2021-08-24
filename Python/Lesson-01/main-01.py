########### DevOps Course - First Assigment - 01 - Python ###########

first = 7
second = 44.3

sum = first + second
multi = first * second
divided = second // first

print('-----------------A-------------------')
print(f'Sum of {first} and {second} = {sum}')
print(f'Multiplying of {first} and {second} = {multi}')
print(f'Divide of {second} and {first} = {divided}')
print('-------------------------------------')

print('-----------------B-------------------')
a = 8    
a = 17
a = 9
b = 6
c = a+b
b = c+a 
b = 8  
print(f'A is {a} , B is {b} and C is {c}') # 9 8 15
print('-------------------------------------')

print('-----------------C-------------------')

#Is there a difference between the two lines below? Why?
name = "John"
name = 'John'

# The answer is :
###    There is no difference between the lines above, it is two ways to define varibale.

# the issue occurs due to the incorrect concat (we try to concat String + integer) 
my_number = 5+5
#print("Result is : " + my_number)
print('-------------------------------------')


print('----------------D--------------------')
x = 5
y = 2.36
#The result is : 7, int function returns the number without .026 for example 
print('-------------------------------------')

print('----------------CHALLENGE-------------------')
a = 8 
b = "123"
print(a+int(b)) #131
print('-------------------------------------')
