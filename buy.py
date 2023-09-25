from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from userInfo import date
from utils import findElFromList, findElFromListByKey


def buy(driver: webdriver):
    # 点击购买进入选择日期
    buy_button = driver.find_element(By.CLASS_NAME, 'buy__button')
    sleep(1)
    buy_button.click()
    sleep(1)

    # 点击日期进入选择场次
    def chooseDate(text, index, show_index):
        if text.isdigit():
            if "29" == text:
                print("找到了 ", text)
                return index
            else:
                return show_index
        else:
            return show_index

    findElFromListByKey("bui-calendar-day-box", "day-item", driver, chooseDate)

    # 选择场次
    def chooseTime(text, index, show_index):
        if "14:30" in text:
            return index
        else:
            return show_index

    findElFromListByKey("bui-dm-sku-card-item-box", "item-content", driver, chooseTime)

    # 选择票价
    def choosePrice(text, index, show_index):
        print(text)
        if "79元" in text:
            return index
        else:
            return show_index

    findElFromListByKey("bui-dm-sku-card-item-box", "item-content", driver, choosePrice)
