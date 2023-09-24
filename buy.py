from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from userInfo import date
from utils import findElFromList, findElFromListByKey


def buy(driver: webdriver):
    print("buy")
    buy_button = driver.find_element(By.CLASS_NAME, 'buy__button')
    sleep(1)
    buy_button.click()
    sleep(1)

    # 查找日期
    findElFromListByKey("bui-calendar-day-box", "day-item", driver, "25")
