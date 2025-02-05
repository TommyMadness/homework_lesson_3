import pytest
from selene import browser

@pytest.fixture
def adjust_window_size():
    print("Установка разрешения браузера")
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    print("Закрываем браузер")