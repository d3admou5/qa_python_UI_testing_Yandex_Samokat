import pytest
import allure
from pages.main_page import MainPage
from data.faq_data import FaqData
from data.url_data import MAIN_PAGE_URL

@allure.feature("FAQ")
@allure.story("Проверка раскрытия ответов на вопросы")
@pytest.mark.parametrize("index, expected_answer", FaqData.faq_items)
def test_faq_answer(driver, index, expected_answer):
    page = MainPage(driver)

    with allure.step("Открываем главную страницу"):
        page.open_main_page(MAIN_PAGE_URL)

    with allure.step("Прокручиваем до секции FAQ"):
        page.scroll_to_faq()

    with allure.step(f"Кликаем на вопрос с индексом {index}"):
        page.click_faq_question(index)

    with allure.step("Получаем текст ответа"):
        actual_text = page.get_faq_answer_text(index)

    with allure.step("Проверяем, что ответ содержит ожидаемый текст"):
        assert expected_answer in actual_text
