from selenium import webdriver

# my_driver1 = webdriver.Chrome(
#     executable_path="C:\\Users\\admin\Desktop\\chromedriver_win32\\chromedriver")

# my_driver2 = webdriver.Chrome(
#     executable_path="C:\\Users\\admin\Desktop\\chromedriver_win32\\chromedriver")

# web_page = ['http://www.walla.co.il', 'http://ynet.co.il']

# # - 1
# #   A & B
# my_driver1.get(web_page[0])
# my_driver2.get(web_page[1])


# 2
# A & B
# walla_title = 'וואלה! - האתר המוביל בישראל - עדכונים מסביב לשעון'
# ynet_title = 'ynet - חדשות, כלכלה, ספורט ובריאות - דיווחים שוטפים מהארץ ומהעולם'

# my_driver1 = my_driver1.refresh()
# my_driver2 = my_driver2.refresh()

# get_name1 = my_driver1.current_url
# get_name2 = my_driver2.current_url

# # 2 C 
# if(get_name1 == walla_title and get_name2 == ynet_title):
#     print('We are equal')
# else:
#     print('We are not equal')

# 3

# my_driver1_element = webdriver.Chrome(
#     executable_path="C:\\Users\\admin\Desktop\\chromedriver_win32\\chromedriver")

# my_driver2_element = webdriver.Chrome(
#     executable_path="C:\\Users\\admin\Desktop\\chromedriver_win32\\chromedriver")

# my_driver1_element.get('http://www.ynet.co.il')
# my_driver2_element.get('http://www.walla.co.il')

# my_driver1_element.find_element_by_tag_name('title')
# my_driver2_element.find_element_by_tag_name('title')

## the answer is Yes, any website has a "title" element. 
# 4

# my_driver_for_translate = webdriver.Chrome(
#     executable_path="C:\\Users\\admin\Desktop\\chromedriver_win32\\chromedriver")

# my_driver_for_translate.get('https://translate.google.co.il/')
# my_driver_for_translate.find_element_by_class_name('er8xn').send_keys('DevOps Course')



# 5 
# my_driver_for_youtube = webdriver.Chrome(
#     executable_path="C:\\Users\\admin\Desktop\\chromedriver_win32\\chromedriver")

# my_driver_for_youtube.get('https://www.youtube.com/')

# my_driver_for_youtube.find_element_by_id('search').send_keys('Focus Music for Work and Studying')
# my_driver_for_youtube.find_element_by_id('search-icon-legacy').click()

# 6 

# my_driver_for_translate2 = webdriver.Chrome(
#     executable_path="C:\\Users\\admin\Desktop\\chromedriver_win32\\chromedriver")

# my_driver_for_translate2.get('https://translate.google.co.il/')

# my_driver_for_translate2.find_element_by_class_name('er8xn').send_keys('Test Translate')

# # my_driver_for_translate2.find_elements_by_class_name('VfPpkd-YVzG2b').click()
# my_driver_for_translate2.find_element_by_xpath('//*[@id="i13"]/span[3]').click()

# # text_Hebrew = my_driver_for_translate2.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span')[0].text
# my_element = my_driver_for_translate2.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[2]')

# print(f'my elemnt is {my_element.text}')

# 7

my_driver_for_facebook = webdriver.Chrome(
    executable_path="C:\\Users\\admin\Desktop\\chromedriver_win32\\chromedriver")

my_driver_for_facebook.get('https://www.facebook.com/login')


my_driver_for_facebook.find_element_by_xpath('//*[@id="email"]').send_keys('example.com')

my_driver_for_facebook.find_element_by_xpath('//*[@id="pass"]').send_keys('example.com')

my_driver_for_facebook.find_element_by_id('loginbutton').click()

# 8 

### Challenges part ###
#######################
#######################


# my_driver_for_cookies = webdriver.Chrome(
#     executable_path="C:\\Users\\admin\Desktop\\chromedriver_win32\\chromedriver")

# my_driver_for_cookies.get('https://www.ynet.co.il')

# my_driver_for_cookies.delete_all_cookies()

# 9

# my_driver_for_github = webdriver.Chrome(
#     executable_path="C:\\Users\\admin\\Desktop\\chromedriver_win32\\chromedriver.exe")

# my_driver_for_github.get('https://www.github.com')

# my_driver_for_github.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label').send_keys('Selenium')

# my_driver_for_github.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label').send_keys(u'\ue007')