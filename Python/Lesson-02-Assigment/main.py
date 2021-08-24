# ---------- Lesson-02- Assigment DevOps Course ----------

print('------A------')
x = 100
y = 200

if x > y:
    print('BIG')
else:
    print('Small')
print('-------------')
print('------B------')

for x in range(5):
    print(x)
print('-------------')


print('------C------')
check_month = 1

if(check_month == 1):
    print('summer')
elif check_month == 2:
    print('winter')
elif check_month == 3:
    print('fall')
elif check_month == 4:
    print('spring')
else:
    print('Please enter a valid number bettween (1-4) ')

print('-------------')

print('------D------')
count = 1
while count < 11:
    print(count)
    count += 1

# the loop will running 10 times
# the last number will be 10
print('-------------')

print('------E------')

my_age = 24
first_character = 'E'
isabroad = False
dollar = 3.22
apartmentnumber = 20

print(my_age, first_character, isabroad, dollar, apartmentnumber)
print(dollar+my_age)

print('-------------')

print('------F------')

while True:
    phone_number = input('Please ente your phone number:')
    if phone_number!='':
        print(phone_number)
        break

print('-------------')


print('------G------')


def printHello():
    return 'Hello'


print(printHello())
print('-------------')


def calculate():
    return 5+3.2


print(calculate())
print('-------------')
print('-----H-------')


def printfirstname(name):
    return name


print(printfirstname('Eyab'))


def dividebytwo(num):
    return num/2


print(dividebytwo(10))
print('-------------')

print('-----I-------')


def addnumbers(num1, num2):
    return num1 + num2


print(addnumbers(5, 10))


def twoStrings(str1, str2):
    return str1 + ' ' + str2


print(twoStrings('Eyab', 'Kabha'))
print('-------------')

print('------------ Challenges Part ------------')

print('------K------')
for i in range(0, 5):
    for j in range(i+1):
        print('* ', end=' ')
    print('\n')
print('-------------')


print('------M------')


def recivenum():
    numbertofunc = input('Please enter a number: ')
    calculatenumber(numbertofunc)


def calculatenumber(num):
    sum = 0
    for digit in num:
        sum+=int(digit)
    print(sum) 

recivenum()

print('-------------')