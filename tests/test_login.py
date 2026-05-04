import allure
import pytest
from pages.login_page import LoginPage

@allure.feature("Авторизация")
@allure.story("Вход через выбор пользователя")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Пользователь выбирает тестового пользователя и входит в каталог")
class TestLogin:
    
    @allure.title("Тест входа в корзину")
    @allure.tag( "regression", "login")
    @allure.link("https://jira.company.com/browse/TEST-1", name="Требование по логину")
    @allure.story("Позитивные сценарии")
    def test_login(self, page):
        login_page = LoginPage(page)
    
        login_page.open().select_user("FedyaMel")
        login_page.verify_username_value("FedyaMel")
        catalog_page = login_page.click_login()
    
        assert catalog_page is not None
        assert catalog_page.get_title() == "Каталог кроссовок"
        assert catalog_page.get_header_text() == "Каталог кроссовок"
        catalog_page.verify_title("Каталог кроссовок")


    @allure.title("Тест заголовока Входа")
    @allure.tag("smoke", "regression", "login")
    @allure.link("https://jira.company.com/browse/TEST-2", name="Требование по логину")
    @allure.issue("BUG-1", "Не отображается Заголовок")
    @allure.story("Позитивные сценарии")
    def test_title(self, page):
        login_page = LoginPage(page)
    
        login_page.open()    

        assert login_page.get_title() == "Вход в магазин кроссовок"
        assert login_page.get_header_text() == "🍃 Sneaker Store"
    
    
    @allure.title("Тест проверки скидок")
    @allure.tag("smoke", "regression", "login")
    @allure.link("https://jira.company.com/browse/TEST-3", name="Требование по логину")
    @allure.issue("BUG-2", "Не отображается Заголовок")
    @allure.story("Негативный сценарии")
    def test_discount(self, page):
        login_page = LoginPage(page)
    
        login_page.open() 
           
        login_page.select_user("FedyaMel")
        login_page.verify_username_value("FedyaMel")
        login_page.select_discount("discountQuantity")
        login_page.select_discount("discountSum")
        login_page.select_discount("discountPromo")
        catalog_page = login_page.click_login()
        
        assert catalog_page is not None
        assert catalog_page.get_title() == "Каталог кроссовок"
        assert catalog_page.get_header_text() == "Каталог кроссовок"
        
        
    @allure.title("Тест входа для всех пользователей")
    @allure.tag( "regression", "login")
    @allure.link("https://jira.company.com/browse/TEST-4", name="Требование по логину")
    @allure.story("Позитивные сценарии")
    def test_all_login(self, page):
        login_page = LoginPage(page)
    
        login_page.open().select_user("Toma1990")
        login_page.verify_username_value("Toma1990")
        
        login_page.open().select_user("Andrey88")
        login_page.verify_username_value("Andrey88")
        
        login_page.open().select_user("FedyaMel")
        login_page.verify_username_value("FedyaMel")
        
        login_page.open().select_user("Pushkin")
        login_page.verify_username_value("Pushkin")
        
        login_page.open().select_user("AdaLovelace")
        login_page.verify_username_value("AdaLovelace")
        
        catalog_page = login_page.click_login()
    
        assert catalog_page is not None
        assert catalog_page.get_title() == "Каталог кроссовок"
        assert catalog_page.get_header_text() == "Каталог кроссовок"      

