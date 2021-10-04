users = ['Dor','Moshe','David']

try:
    for user in users:
        print(user)
except Exception as error:
    print(error)

def divid_two(num1,num2):
    return num1/num2

def power_two(num1,num2):
    return num1*num2

# print(divid_two(10,5))
# print(power_two(10,5))