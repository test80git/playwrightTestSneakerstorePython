from pages.base_page import BasePage

class CatalogPage(BasePage):
    pass

    def __init__(self, page):
        super().__init__(page)

    def get_title(self):
        return self.page.title()
    
    def get_header_text(self) -> str:
        """Возвращает текст видимого заголовка (если есть h1/h2)"""
        return self.page.locator("h2").text_content()