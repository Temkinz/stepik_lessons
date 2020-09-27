from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from Main_project import _locators as _locator




#Pages
main_page = "http://selenium1py.pythonanywhere.com/ru"
catalogue = "http://selenium1py.pythonanywhere.com/ru/catalogue/"
basket = "http://selenium1py.pythonanywhere.com/ru/basket"


def find(parent, locator):
    return parent.find_element_by_css_selector(locator)

#1.Поиск товара по наименованию 

def test_search(browser):
    #Data
    search_text = "The shellcoder's handbook"

    #Arrange
    browser.get(main_page)

    #Act
    search_input = find(browser, _locator.search_input)
    search_input.clear()
    search_input.send_keys(search_text)
        
    find(browser, _locator.search_button).click()

    search_result = browser.find_element_by_link_text(search_text)
    search_title = browser.find_element_by_tag_name(_locator.search_title)
    search_title = search_title.text

    #Asserts    
    assert "The shellcoder's handbook" in search_title, \
    "Search doesn't contain The shellcoder's handbook"
    
#2. Авторизация

def test_login(browser):

    #Data
    login = "test30082020@gmail.com"
    password = "Test202020"

    #Arrange
    browser.get(main_page)

    #Act
    find(browser, _locator.login_link).click()
    find(browser, _locator.login_input_email).send_keys(login)
    find(browser, _locator.login_input_password).send_keys(password)
    find(browser, _locator.login_submit).click()

    message_auth = browser.find_element_by_class_name(_locator.login_message)

    #Asserts    
    assert "Рады видеть вас снова" in message_auth.text, \
    "The user is not logged in"

#3. Регистрация 

def test_registration(browser):

    #Data
    password = "Test202020"    

    def emails():
        email = ''
        for x in range(12):
            email = email + random.choice(list('1234567890qwertyuiopASDFGHJKLZXCVBMNMNM'))
        email = email + '@gmail.com'
        return email

    #Arrange
    browser.get(main_page)

    #Act
    find(browser, _locator.login_link).click()
    find(browser, _locator.reg_input_email).send_keys(emails())
    find(browser, _locator.reg_input_password1).send_keys(password)
    find(browser, _locator.reg_input_password2).send_keys(password)
    find(browser, _locator.reg_submit).click()

    message_reg = browser.find_element_by_class_name(_locator.login_message)

    #Asserts
    assert "Спасибо за регистрацию" in message_reg.text, \
    "The user is not registered"

#4. Смена языка интерфейса

def test_language(browser):

    #Arrange
    browser.get(main_page)

    #Act
    find(browser, _locator.language_selector).click()
    find(browser, _locator.language_option).click()
    find(browser, _locator.language_button).click()
        
    login_link = find(browser, _locator.login_link)
    goods_selector = find(browser, _locator.goods_selector)
        
    #Asserts
    assert "Einloggen" in login_link.text, "Login link text isn't translated"
    assert "Webshop" in goods_selector.text, "Goods selector text isn't translated"


#5. Добавление товаров в корзину

def test_add_to_the_cart(browser):

    #Arrange
    browser.get(catalogue)

    #Act
    browser.find_element_by_xpath(_locator.book1_choose_button).click()
    book_one_t = find(browser, _locator.book1_title).text

    browser.find_element_by_xpath(_locator.book2_choose_button).click()
    book_two_t = find(browser, _locator.book2_title).text
        
    browser.get(basket)
    book_one_title = browser.find_element_by_xpath(_locator.book1_title_basket)
    book_two_title = browser.find_element_by_xpath(_locator.book2_title_basket)

    #Asserts
    assert book_one_t in book_one_title.text, "The first book is not in the basket"
    assert book_two_t in book_two_title.text, "The second book is not in the basket"


#6. Изменение языка и проверка страницы продукта

#Data
check_language_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_page_language(browser):
    # Action
    browser.get(check_language_link)
    time.sleep(10)
    button_exist = len(browser.find_elements_by_css_selector(_locator.add_to_cart))

    # Assert
    assert button_exist > 0, 'There is no AddtoTheCart button'
