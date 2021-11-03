from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


def getGongChaStore(result):
    gongChaStoreURL = 'http://www.gong-cha.co.kr/brand/store/search.php'
    browser = webdriver.Chrome()
    browser.get(gongChaStoreURL)

    time.sleep(2)

    while True:
        scrollBar = browser.find_element(By.CLASS_NAME, 'mCSB_dragger')
        browser.execute_script("arguments[0].scrollBy(0, Y)", scrollBar)


        # browser.execute_script("arguments[0].scrollBy(0, Y)")
        # scrollBar = browser.find_element(By.CLASS_NAME, 'mCSB_dragger_bar')
        # scrollBar.send_keys(Keys.DOWN)


def main():
    pass


    result = []

    getGongChaStore(result)



if __name__ == '__main__':
    main()