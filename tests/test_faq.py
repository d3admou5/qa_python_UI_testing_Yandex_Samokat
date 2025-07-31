import pytest
from pages.main_page import MainPage
from data.faq_data import FaqData
from data.url_data import MAIN_PAGE_URL


@pytest.mark.parametrize("index, expected_answer", FaqData.faq_items)
def test_faq_answer(driver, index, expected_answer):
    page = MainPage(driver)
    page.open_main_page(MAIN_PAGE_URL)
    page.scroll_to_faq()
    page.click_faq_question(index)
    actual_text = page.get_faq_answer_text(index)
    assert expected_answer in actual_text
