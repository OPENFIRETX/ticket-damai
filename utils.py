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
def findElFromListByKey(listClassName, keyClassName, driver, handleFn):
    # 最外层list
    show_list = driver.find_elements(By.CLASS_NAME, listClassName)
    show_index = -1
    print("外层list")
    print(show_list)
    for (index, show) in enumerate(show_list):
        # 文字的元素列表
        texts = show.find_element(By.CLASS_NAME, keyClassName)
        texts_list = texts.text.split("\n")  # 获取日期时 div里所有文字
        for (j, text) in enumerate(texts_list):
            # 自定义判断
            show_index = handleFn(text, index, show_index)
            print("WWWWW", show_index)

    # 判断搜到没有
    if show_index == -1:
        print("没有!!!!!!!!!!!!!!!!")
        return
    else:
        print("有!!!!!!!!!!!!!!!!!")

    sleep(1)
    # 点击找到的日期
    print(show_list[show_index].text)
    show_list[show_index].click()
    sleep(5)
