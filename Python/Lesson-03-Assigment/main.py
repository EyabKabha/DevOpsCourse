# ---------- Lesson - 03 - Assigment DevOps Course ----------

#1+2
try:
    a = 1/0
except Exception as e:
    print('zeroDivisionError')

# Questions - 03
#Yes

#4
# Except handles all types of exceptions

# 5
# This type of exception handler is a "not good practice" because it will give partial information.

# 6
# Except IOError - handles I/O (input/output) exceptions
# Except ZeroDivisionError - handles divison by zero

# 7 + 8 
read_name = open('Lesson-03-Assigment\\words.txt', 'w')
read_name.write('Eyab Kabha')
read_name.close()

#9 
read_name = open('Lesson-03-Assigment\\words.txt', 'r')
print(read_name.readlines())
read_name.close()

#10
read_name_hebrew = open('Lesson-03-Assigment\\words_hebrw.txt', 'w', encoding='utf-8')
read_name_hebrew.write('איאב')
read_name_hebrew.close()


read_name_hebrew = open('Lesson-03-Assigment\\words_hebrw.txt', 'r', encoding='utf-8')
print(read_name_hebrew.readlines())
read_name_hebrew.close()

#11
from flask import Flask
app = Flask(__name__)

@app.route('/content')
def read_file():
    return open('Lesson-03-Assigment\\words.txt').read(), 200

@app.route('/register')
def regitser():
    open('Lesson-03-Assigment\\flasktest.txt','w').write('Hello Admin')
    return 'Success', 201 

#challenge part
from PIL import Image,ImageDraw

new_image = Image.new('RGB',(300,300),color=(100,149,237))
new_draw = ImageDraw.Draw(new_image)
new_draw.text((150,200),'DevOps Course 2021\nBy Doron Nuni',fill=(233,150,122))
new_image.show()

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=30000)