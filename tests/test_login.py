import pytest
from pages.login_page import LoginPage

def test_login(page):
    login_page = LoginPage(page)
    
    login_page.open().select_user("FedyaMel")
    login_page.verify_username_value("FedyaMel")
    catalog_page = login_page.click_login()
    
    assert catalog_page is not None
    assert catalog_page.get_title() == "Каталог кроссовок"
    assert catalog_page.get_header_text() == "Каталог кроссовок"

def test_title(page):
    login_page = LoginPage(page)
    
    login_page.open()    

    assert login_page.get_title() == "Вход в магазин кроссовок"
    assert login_page.get_header_text() == "🍃 Sneaker Store"
    
    