from pages.base_page import BasePage
import allure

class CatalogPage(BasePage):
    pass

    def __init__(self, page):
        super().__init__(page)

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
    
    