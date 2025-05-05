import pytest
from selenium.webdriver.common.by import By


class TestLogin:

    @pytest.mark.parametrize('link', [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207",
    ])
    def test_guest_should_see_login_link(self, browser, link):
        browser.get(link)

        # Использовал find_elements, чтобы тест доходил до assert, если элемент не найден
        elements = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")

        assert len(elements) == 1, "Should be found one element"
