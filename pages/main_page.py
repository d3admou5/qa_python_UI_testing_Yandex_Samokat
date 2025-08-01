import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_main_page(self, url):
        self.open(url)

    @allure.step("Прокрутить до секции FAQ")
    def scroll_to_faq(self):
        self.scroll_to_element(MainPageLocators.FAQ_SECTION)

    @allure.step("Клик по вопросу FAQ №{index}")
    def click_faq_question(self, index: int):
        locator = getattr(MainPageLocators, f"FAQ_QUESTION_{index}")
        self.scroll_to_element(locator)
        self.click(locator)

    @allure.step("Получить текст ответа FAQ №{index}")
    def get_faq_answer_text(self, index: int):
        locator = getattr(MainPageLocators, f"FAQ_ANSWER_{index}")
        return self.get_text(locator)

    @allure.step("Кликнуть по логотипу Самоката")
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Кликнуть по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)
