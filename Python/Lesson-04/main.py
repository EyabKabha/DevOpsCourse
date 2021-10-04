from selenium import webdriver
from time import sleep

my_driver = webdriver.Chrome(executable_path="C:\\Users\\admin\Desktop\\chromedriver_win32\\chromedriver")

my_driver.get('C:\\Users\\admin\\Downloads\\tip_calc\\tip_calc\\index.html')

# for i in range(5):
#     print('in loop')
#     sleep(5)
#     my_driver.refresh()


my_driver.find_element_by_id('billamt').send_keys('100')

my_driver.find_element_by_id('serviceQual').send_keys('30')
my_driver.find_element_by_id('peopleamt').send_keys('2')
my_driver.find_element_by_id('calculate').click()

my_driver.find_element_by_tag_name('tittle')
