from time import sleep
from userInfo import url
from selenium import webdriver

from search import search
from buy import buy

# 打开浏览器
driver = webdriver.Chrome()
driver.get(url)

# 查到
search(driver)

# 进入选座购买
buy(driver)






sleep(50)
