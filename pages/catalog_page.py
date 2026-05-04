from pages.base_page import BasePage
import allure

class CatalogPage(BasePage):
    
    # Локаторы (исправленные)
    PRODUCT_CARD = ".product-card"
    BTN_SELECT_SIZE = "button:has-text('Выбрать размер')"  # кнопка "Выбрать размер"
    SIZE_BUTTON = ".size-btn"  # кнопка размера (например, "42 (43)")
    BTN_ADD_CART = "button:has-text('Добавить в корзину')"  # кнопка добавления
    
    
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
    
    @allure.step("Выбор товара по имени {name_product}")
    def checkoutProduct(self, name_product):
        # Находим карточку товара с нужным названием (ищем по всему тексту карточки)
        product_card = self.page.locator(f".product-card:has-text('{name_product}')")
        # Внутри карточки ищем кнопку "Выбрать размер"
        product_card.locator(self.BTN_SELECT_SIZE).click()
        return self
    

    
    @allure.step("Выбор размера {size}")
    def clickSize(self, size):
        # Ждём появления модального окна
        self.page.wait_for_selector(".sizes", timeout=5000)
        # Выбираем нужный размер
        self.page.locator(f"{self.SIZE_BUTTON}:has-text('{size}')").click()
        return self
    
    @allure.step("Добавить в корзину")
    def clickAddCart(self):
        self.page.locator(self.BTN_ADD_CART).click()
        return self
    