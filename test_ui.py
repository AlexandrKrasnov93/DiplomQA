import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Поиск фильма по названию на кириллице")
@allure.description("Тест проверяет поиск фильма по названию на кириллице")
@allure.severity("критический")
def test_by_valid_сyrillic(chrome_browser):
    with allure.step("Заходим на сайт"):
        chrome_browser.get("https://www.kinopoisk.ru/")
    with allure.step("Если появляется капча пытаемся её нажать, иначе продолжаем следующие шаги"):
        try:
            chrome_browser.find_element(By.CSS_SELECTOR, ".CheckboxCaptcha-Button").click()
        except NoSuchElementException:
            pass
    with allure.step("Если появляется информационное письмо, закрываем его, иначе продолжаем следующие шаги"):
        try:
            chrome_browser.find_element(By.CSS_SELECTOR, ".styles_closeIcon__Zvc5W").click()
        except NoSuchElementException:
            pass
    with allure.step("Нажимаем по полю поиска"):
        chrome_browser.find_element(By.NAME, "kp_query").click()
    with allure.step("Вводим название фильма"):
        chrome_browser.find_element(By.NAME, "kp_query").send_keys("Падение лондона")
    with allure.step("Выбираем найденный фильм"):
        chrome_browser.find_element(By.ID, "suggest-item-film-806977").click()
    with allure.step("Проверяем является ли заданное условие истинным "):
        assert chrome_browser.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "Падение Лондона (2015)"


@allure.title("Поиск фильма по названию на латинице")
@allure.description("Тест проверяет поиск фильма по названию на латинице")
@allure.severity("критический")
def test_by_valid_latin(chrome_browser):
    with allure.step("Заходим на сайт"):
        chrome_browser.get("https://www.kinopoisk.ru/")
    with allure.step("Если появляется капча пытаемся её нажать, иначе продолжаем следующие шаги"):
        try:
            chrome_browser.find_element(By.CSS_SELECTOR, ".CheckboxCaptcha-Button").click()
        except NoSuchElementException:
            pass
    with allure.step("Если появляется информационное письмо, закрываем его, иначе продолжаем следующие шаги"):
        try:
            chrome_browser.find_element(By.CSS_SELECTOR, ".styles_closeIcon__Zvc5W").click()
        except NoSuchElementException:
            pass
    with allure.step("Нажимаем по полю поиска"):
        chrome_browser.find_element(By.NAME, "kp_query").click()
    with allure.step("Вводим название фильма"):
        chrome_browser.find_element(By.NAME, "kp_query").send_keys("X-Men")
    with allure.step("Выбираем найденный фильм"):
        chrome_browser.find_element(By.ID, "suggest-item-film-886").click()
    with allure.step("Проверяем является ли заданное условие истинным "):
        assert chrome_browser.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "Люди Икс (2000)"


@allure.title("Поиск фильма по названию c цифрами")
@allure.description("Тест проверяет поиск фильма по названию состоящему из цифр и символа")
@allure.severity("критический")
def test_by_valid_symbol(chrome_browser):
    with allure.step("Заходим на сайт"):
        chrome_browser.get("https://www.kinopoisk.ru/")
    with allure.step("Если появляется капча пытаемся её нажать, иначе продолжаем следующие шаги"):
        try:
            chrome_browser.find_element(By.CSS_SELECTOR, ".CheckboxCaptcha-Button").click()
        except NoSuchElementException:
            pass
    with allure.step("Если появляется информационное письмо, закрываем его, иначе продолжаем следующие шаги"):
        try:
            chrome_browser.find_element(By.CSS_SELECTOR, ".styles_closeIcon__Zvc5W").click()
        except NoSuchElementException:
            pass
    with allure.step("Нажимаем по полю поиска"):
        chrome_browser.find_element(By.NAME, "kp_query").click()
    with allure.step("Вводим название фильма"):
        chrome_browser.find_element(By.NAME, "kp_query").send_keys("2+1")
    with allure.step("Выбираем найденный фильм"):
        chrome_browser.find_element(By.ID, "suggest-item-film-934130").click()
    with allure.step("Проверяем является ли заданное условие истинным "):
        assert chrome_browser.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "2+1 (2016)"


@allure.title("Негативный тест на ввод некорретных данных в поле название фильма")
@allure.description("Негативный тест по поиску фильма по названию состоящему из символов")
@allure.severity("критический")
def test_by_invalid_symbol(chrome_browser):
    with allure.step("Заходим на сайт"):
        chrome_browser.get("https://www.kinopoisk.ru/")
    with allure.step("Если появляется капча пытаемся её нажать, иначе продолжаем следующие шаги"):
        try:
            chrome_browser.find_element(By.CSS_SELECTOR, ".CheckboxCaptcha-Button").click()
        except NoSuchElementException:
            pass
    with allure.step("Если появляется информационное письмо, закрываем его, иначе продолжаем следующие шаги"):
        try:
            chrome_browser.find_element(By.CSS_SELECTOR, ".styles_closeIcon__Zvc5W").click()
        except NoSuchElementException:
            pass
    with allure.step("Нажимаем по полю поиска"):
        chrome_browser.find_element(By.NAME, "kp_query").click()
    with allure.step("Вводим в поле поиска символ"):
        chrome_browser.find_element(By.NAME, "kp_query").send_keys("#")
    with allure.step("Проверяем заданное условие"):
        assert chrome_browser.find_element(By.XPATH, "//*[contains(@class, 'emptySuggest')]").text == "По вашему запросу ничего не найдено"


@allure.title("Негативный тест на ввод некорретных данных в поле название фильма")
@allure.description("Негативный тест на ввод несуществующего фильма в поле название фильма")
@allure.severity("критический")
def test_by_invalid_does_not_exist(chrome_browser):
    with allure.step("Заходим на сайт"):
        chrome_browser.get("https://www.kinopoisk.ru/")
    with allure.step("Если появляется капча пытаемся её нажать, иначе продолжаем следующие шаги"):
        try:
            chrome_browser.find_element(By.CSS_SELECTOR, ".CheckboxCaptcha-Button").click()
        except NoSuchElementException:
            pass
    with allure.step("Если появляется информационное письмо, закрываем его, иначе продолжаем следующие шаги"):
        try:
            chrome_browser.find_element(By.CSS_SELECTOR, ".styles_closeIcon__Zvc5W").click()
        except NoSuchElementException:
            pass
    with allure.step("Нажимаем по полю поиска"):
        chrome_browser.find_element(By.NAME, "kp_query").click()
    with allure.step("Вводим в поле поиска несуществующий фильм"):
        chrome_browser.find_element(By.NAME, "kp_query").send_keys("ауцук")
    with allure.step("Проверяем аданное условие"):
        assert chrome_browser.find_element(By.XPATH, "//*[contains(@class, 'emptySuggest')]").text == "По вашему запросу ничего не найдено"
