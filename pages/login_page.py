import allure
from pages.base_page import BasePage
from config import config

class LoginPage(BasePage):
    # Локаторы
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "button:has-text('Войти')"
    DISCOUNT = ".discount-settings"
    DISCOUNT_QUANTITY = "#discountQuantity"
    DISCOUNT_SUM = "#discountSum"
    DISCOUNT_PROMO = "#discountPromo"

    @allure.step("Открытие страницы авторизации")
    def open(self):
        self.page.goto(config.BASE_URL)
        return self

    @allure.step("Ввод логина {username}")  # {username} подставится автоматически
    def fill_username(self, username):
        self.page.fill(self.USERNAME_INPUT, username)
        return self

    @allure.step("Ввод пароля")  # без параметров
    def fill_password(self, password):
        self.page.fill(self.PASSWORD_INPUT, password)
        return self

    @allure.step("Нажатие кнопки 'Войти' и переход в каталог")    
    def click_login(self):
        with self.page.expect_navigation():
            self.page.click(self.LOGIN_BUTTON)
        from pages.catalog_page import CatalogPage
        return CatalogPage(self.page)

    @allure.step("Выбор тестового пользователя {username}")
    def select_user(self, username):
        self.page.locator(".user-card", has_text=username).click()
        return self
    
    @allure.step("Получение заголовка страницы")
    def get_title(self):
        return self.page.title()
    
    @allure.step("Получение текста видимого заголовка H2")
    def get_header_text(self) -> str:
        """Возвращает текст видимого заголовка (если есть h1/h2)"""
        return self.page.locator("h2").text_content()      

    @allure.step("Проверка заголовка страницы: ожидается '{expected_title}'")
    def verify_title(self, expected_title):
        assert self.get_title() == expected_title
        return self
    
    @allure.step("Получение значения поля логина")
    def get_username_value(self):
        return self.page.input_value(self.USERNAME_INPUT)

    @allure.step("Проверка поля логина: ожидается '{expected}'")
    def verify_username_value(self, expected):
        # Ждём, пока значение в поле не станет равным expected
        self.page.wait_for_function(
            f"document.querySelector('{self.USERNAME_INPUT}').value === '{expected}'",
            timeout=10000
        )
        assert self.get_username_value() == expected
        return self
    
    
    @allure.step("Выбор скидки {discount}")
    def select_discount(self, discount):
        self.page.locator("id="+discount).click()
        return self
    
    