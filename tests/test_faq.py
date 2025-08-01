import pytest
import allure
from pages.main_page import MainPage
from data.faq_data import FaqData
from data.url_data import MAIN_PAGE_URL


@allure.feature("FAQ")
@allure.story("Проверка отображения ответов на вопросы")
@pytest.mark.parametrize("index, question, expected_answer", FaqData.faq_items)
@allure.title("FAQ: '{question}' — проверка отображения ответа")
def test_faq_question(driver, index, question, expected_answer):
    page = MainPage(driver)
    page.open_main_page(MAIN_PAGE_URL)
    page.scroll_to_faq()
    page.click_faq_question(index)
    actual_answer = page.get_faq_answer_text(index)
    assert actual_answer == expected_answer
