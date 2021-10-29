from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import mariadb
from urllib import request as rq


def getBookStores(result):
    # 베스트셀러 홈페이지
    bookStoreURL = 'http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?orderClick=d79'
    browser = webdriver.Chrome()
    browser.get(bookStoreURL)

    time.sleep(2)

    bookGenre = browser.find_element(By.CSS_SELECTOR, '#main_contents > div.box_sub_category.fixed_sub_category > ul > li:nth-child(2) > a')
    bookGenre.click()

    for i in range(1, 21):

        bookTitle = browser.find_element(By.CSS_SELECTOR, f'#main_contents > ul > li:nth-child({i*6}) > div.detail > div.title > a > strong')
        bookAuthor = browser.find_element(By.CSS_SELECTOR, f'#main_contents > ul > li:nth-child({i*6}) > div.detail > div.author')
        browser.find_element(By.CSS_SELECTOR, f'#main_contents > ul > li:nth-child({i*6}) > div.detail > div.price > strong')

        print(f'title : {bookTitle.text}')
        print(f'author : {bookAuthor.text}')

        authorList = bookAuthor.split('|')

        author = authorList[0].strip()
        print(f'autohr : {author}')


    # for i in range(2, 31):
    #
    #     bookGenre = browser.find_element(By.CSS_SELECTOR, f'main_contents > div.box_sub_category.fixed_sub_category > ul > li:nth-child({i}) > a')
    #     browser.execute_script('arguments[0].click()', bookGenre)
    #
    #     time.sleep(1)

def main():

    result = []

    getBookStores(result)

if __name__ == '__main__':
    main()

# 교보문고 사이트 접속




time.sleep(2)

# SELECT 아이템들

# 베스트 버튼 클릭


# 책 50개씩 보기 옵션 선택하기
# view_option_selector = '#main_contents > div.list_header > div > span:nth-child(1) > a'
# open_option_class = browser.find_element(By.CSS_SELECTOR, view_option_selector)
# open_option_class.click()
#
# view_50cnt_class_selector = '#main_contents > div.list_header > div > span:nth-child(1) > ul > li:nth-child(2) > a'
# select_50cnt = browser.find_element(By.CSS_SELECTOR, view_50cnt_class_selector)
# select_50cnt.click()

# 책 제목
# book_title_selector = '#main_contents > ul > li > div.detail > div.title > a > strong'
# book_titles = browser.find_elements(By.CSS_SELECTOR, book_title_selector)
# for idx, title in enumerate(book_title):
#     print(idx + 1, title.text)

# 책 저자
# book_author_selector = '#main_contents > ul > li > div.detail > div.author'
# book_authors = browser.find_elements(By.CSS_SELECTOR, book_author_selector)
# for idx, book_author in enumerate(book_authors):
#     print(idx, book_author.text[0:5])

# 출판사


# 책 가격 (실물 & E북)
# book_prices = browser.find_elements(By.CLASS_NAME, 'book_price')
# ebook_prices = browser.find_elements(By.CLASS_NAME, 'ebook_price')

# for idx, price in enumerate(book_price):
#     print(idx, price.text)

# ebook_price = None
#
# for i in range(len(book_titles)):
#
#     book_title = book_titles[i].text
#     book_author = book_authors[i].text
#     book_price = book_prices[i].text
#     # if ebook_prices == None:
#     #     ebook_price = 'No ebook'
#     # ebook_price = ebook_prices[i].text
#
#     print(f'title : {book_title}')
#     print(f'book_author : {book_author}')
#     print(f'book_price : {book_price}')
#
#
# # move page
# # 2페이지 이동
# pageSelector = '#main_contents > div:nth-child(8) > div.list_paging > ul > li:nth-child(2) > a'
# next_page = browser.find_element(By.CSS_SELECTOR, pageSelector)
# next_page.click()
#
# # 3페이지 이동
# pageSelector = '#main_contents > div:nth-child(8) > div.list_paging > ul > li:nth-child(3) > a'
# next_page = browser.find_element(By.CSS_SELECTOR, pageSelector)
# next_page.click()
#
# # 4페이지 이동
# pageSelector = '#main_contents > div:nth-child(8) > div.list_paging > ul > li:nth-child(4) > a'
# next_page = browser.find_element(By.CSS_SELECTOR, pageSelector)
# next_page.click()




