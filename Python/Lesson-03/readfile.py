
# print(read_users.readlines())
# read_users.close()

def write_users(users):
    write_users = open('Lesson-03\\users.txt', 'a')
    write_users.write(users + '\n')
    write_users.close()

def print_users():
    read_users = open('Lesson-03\\users.txt', 'r')
    print(read_users.readlines())
    read_users.close()

write_users('test')
print_users()
#print users 
#write users

