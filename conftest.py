import allure
import pytest
from playwright.sync_api import sync_playwright
from pathlib import Path
import time
import os

HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"

@pytest.fixture
def page(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=HEADLESS
            ,slow_mo=750  if not HEADLESS else 0    # 750 мс между действиями
            )
        context = browser.new_context(
            record_video_dir="build/testvideo/"
        )
        page = context.new_page()
        request.node._page = page
        request.node._context = context
        
        yield page
        
        # Закрываем контекст и даём время на сохранение видео
        context.close()
        time.sleep(2)
        browser.close()
        
        # ПРИКРЕПЛЯЕМ ВИДЕО ПОСЛЕ ЗАКРЫТИЯ КОНТЕКСТА
        if hasattr(request.node, '_failed') and request.node._failed:
            video_path = page.video.path()
            if video_path and os.path.exists(video_path):
                allure.attach(
                    open(video_path, "rb").read(),
                    name=f"VIDEO - {request.node.name}",
                    attachment_type=allure.attachment_type.WEBM
                )

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        item._failed = True
        page = getattr(item, "_page", None)
        if page:
            allure.attach(
                page.screenshot(),
                name=f"FAILED - {item.name}",
                attachment_type=allure.attachment_type.PNG
            )
            
            