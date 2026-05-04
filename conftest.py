import pytest
from playwright.sync_api import sync_playwright
from config import config

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser_type = getattr(p, config.BROWSER)
        browser = browser_type.launch(headless=config.HEADLESS, slow_mo=config.SLOW_MO)
        context = browser.new_context(
            record_video_dir=config.VIDEO_PATH if config.VIDEO else None
        )
        page = context.new_page()
        page.set_default_timeout(config.TIMEOUT)
        yield page
        context.close()
        browser.close()
        
