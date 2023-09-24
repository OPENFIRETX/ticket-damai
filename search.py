from userInfo import url, name
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils import clickElementByClassName, findElFromList


def search(driver: webdriver):
    # 进入搜索
    clickElementByClassName("home-top__search", driver)

    # 搜索场次
    input_ele = driver.find_element(By.TAG_NAME, "input")
    input_ele.send_keys(name)
    sleep(4)

    # 结果列表
    findElFromList("bui-calendar-day-box", "search_projects_content_item_project", driver)
