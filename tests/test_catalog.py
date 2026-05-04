import allure
import pytest
from pages.login_page import LoginPage

@allure.feature("Catalog")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Пользователь выбирает в каталоге")
class TestCatalog:
    
    @allure.title("Тест выбора в корзине")
    @allure.tag( "regression", "catalog")
    @allure.link("https://jira.company.com/browse/TEST-21", name="Требование по корзине")
    @allure.story("Позитивные сценарии")
    def test_add_cart(self, page):
        login_page = LoginPage(page)
            
        login_page.open().select_user("FedyaMel")
        login_page.verify_username_value("FedyaMel")
        catalog_page = login_page.click_login()
    
        assert catalog_page is not None
        assert catalog_page.get_title() == "Каталог кроссовок"
        assert catalog_page.get_header_text() == "Каталог кроссовок"
        catalog_page.verify_title("Каталог кроссовок")
        
        (catalog_page
            .checkoutProduct("Кроссовки беговые Adidas Ultraboost 22")
            .clickSize("42 (43)")
            .clickAddCart())
        
        
        