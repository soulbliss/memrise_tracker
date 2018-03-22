from selenium import webdriver
import os


browser = webdriver.Chrome()

browser.get('https://www.memrise.com/login/')


username = browser.find_element_by_name('username')

username.send_keys('xyz@hotmail.com')

password = browser.find_element_by_name('password')

password.send_keys('generic_password')

password.submit()

content = browser.find_element_by_css_selector('p.number.js-num')

mem_num = content.text

file = open('pipe.txt','w')

file.write(mem_num)

print(mem_num)

file.close()

browser.quit()