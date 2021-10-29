from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

def getPuradakStores(result):
    # 프라닭 매장 입구 사이트 접속
    puradakUrl = 'https://puradakchicken.com/startup/store.asp'
    browser = webdriver.Chrome()

    browser.get(puradakUrl)
    time.sleep(2)

    # 시도 선택
    eleSelect = Select(browser.find_element(By.ID, 'areaidx'))
    eleSelect.select_by_index(0)
    time.sleep(2)

    storesEle = browser.find_element(By.ID, 'resultCnt')
    storesCnt = storesEle.text

    storesPageCnt = int(storesCnt) / 20
    if storesPageCnt % 10 != 0:

        storesPageCnt = storesPageCnt + 1

    storesPageCnt = int(storesPageCnt)

    for i in range(10):
        nextBtn = browser.find_element(By.CLASS_NAME, 'next')
        browser.execute_script('arguments[0].click()', nextBtn)

        time.sleep(1)

        for j in range(2, 22):

            try:
                storeName = browser.find_element(By.CSS_SELECTOR, f'#result_search > li:nth-child({j}) > span > p.name')
                storeJibun = browser.find_element(By.CSS_SELECTOR, f'#result_search > li:nth-child({j}) > span > p.juso > span.jibun')
                storeDoro = browser.find_element(By.CSS_SELECTOR, f'#result_search > li:nth-child({j}) > span > p.juso > span.doro')
                storeTel = browser.find_element(By.CSS_SELECTOR, f'#result_search > li:nth-child({j}) > span > p.tel')

                print(f'storeName : {storeName.text}')
                print(f'storeJibun : {storeJibun.text}')
                print(f'storeDoro : {storeDoro.text}')
                print(f'storeTel : {storeTel.text}')

            except Exception as e:
                print(e)
                print('no store info')

            else:
                print('success')


def main():

    result = []

    getPuradakStores(result)

if __name__ == '__main__':
    main()
