import pytest
from selenium.webdriver.common.by import By


class TestLocale:

    @pytest.mark.parametrize('link', [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207",
    ])
    def test_add_to_basket_button_exists_on_page(self, browser, link):
        browser.get(link)

        # Использовал find_elements, чтобы тест доходил до assert, если элемент не найден
        elements = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")

        assert len(elements) == 1, "Should be found one element"
