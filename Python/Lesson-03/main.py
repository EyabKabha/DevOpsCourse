import requests
import datetime


# print(datetime.datetime.now())

# url = "http://localhost:3001/login/addnew"

def check_url(url): 
    try:
        req = requests.get(url)
        if(req.status_code == 200):
            print('We are OK')
    except requests.exceptions.MissingSchema:
        # raise('git hub is a bad web!!')
        print('Invalid URL')
    except SyntaxError:
        print('SyntaxError')

check_url('')
