from selenium.webdriver.common.by import By
from time import sleep


# 找到元素点击
def clickElementByClassName(className, driver):
    search_icon_ele = driver.find_element(By.CLASS_NAME, "home-top__search")
    search_icon_ele.click()
    sleep(0.5)


# 从列表中找到要点击的元素
def findElFromList(listClassName, keyClassName, driver):
    show_list = driver.find_elements(By.CLASS_NAME, listClassName)
    show_index = 0
    for (index, show) in enumerate(show_list):
        print("查到的数据")
        print(show.text)
    # if show.text.index("成都"):
    # print(index)
    # 判断搜到没有
    if show_index == -1:
        print("没有")
        return
    my_show = driver.find_elements(By.CLASS_NAME, keyClassName)[0]
    sleep(3)
    my_show.click()
    sleep(5)


# 从列表中找到要点击的元素
def findElFromListByKey(listClassName, keyClassName, driver, key):
    show_list = driver.find_elements(By.CLASS_NAME, listClassName)
    # print(show_list)
    show_index = 0

    for (index, show) in enumerate(show_list):
        print("查到的数据")
        # print(show.getText())

        test = show.find_elements(By.CLASS_NAME, "day-item")
        print(test[0].find_elements(By.TAG_NAME, "div")[0].text)
        print(test[0].find_elements(By.TAG_NAME, "div")[1].text)
        print("test")

        # if (show.getText().index(key)):
        #     show_index = index
    # if show.text.index("成都"):
    # print(index)
    # 判断搜到没有
    if show_index == -1:
        print("没有")
        return
    my_show = driver.find_elements(By.CLASS_NAME, keyClassName)[show_index]
    sleep(3)
    my_show.click()
    sleep(5)
