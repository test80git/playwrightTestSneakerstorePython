from pages.base_page import BasePage
from config import config

class LoginPage(BasePage):
    # Локаторы
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "button:has-text('Войти')"

    def open(self):
        self.page.goto(config.BASE_URL)
        return self

    def fill_username(self, username):
        self.page.fill(self.USERNAME_INPUT, username)
        return self

    def fill_password(self, password):
        self.page.fill(self.PASSWORD_INPUT, password)
        return self

    def click_login(self):
        with self.page.expect_navigation():
            self.page.click(self.LOGIN_BUTTON)
        from pages.catalog_page import CatalogPage
        return CatalogPage(self.page)

    def select_user(self, username):
        self.page.locator(".user-card", has_text=username).click()
        return self

    def get_title(self):
        return self.page.title()
    
    def get_header_text(self) -> str:
        """Возвращает текст видимого заголовка (если есть h1/h2)"""
        return self.page.locator("h2").text_content()      

    def verify_title(self, expected_title):
        assert self.get_title() == expected_title
        return self

    def get_username_value(self):
        return self.page.input_value(self.USERNAME_INPUT)

    def verify_username_value(self, expected):
        assert self.get_username_value() == expected
        return self