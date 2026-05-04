# base_page.py
from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        # from your config
        self.page.set_default_timeout(10000)

    def init_components(self):
        pass
    
