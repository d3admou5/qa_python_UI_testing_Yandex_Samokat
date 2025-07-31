from selenium.webdriver.common.by import By

class MainPageLocators:
    # Логотипы
    SCOOTER_LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@href, 'yandex.ru')]")

    # Кнопки заказа
    ORDER_BUTTON_TOP = (By.XPATH, "//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[text()='Заказать'])[2]")

    # FAQ секция
    FAQ_SECTION = (By.XPATH, "//div[contains(@class, 'Home_FAQ')]")

    # Вопросы и ответы по индексу
    @staticmethod
    def faq_question(index: int):
        return By.ID, f"accordion__heading-{index}"

    @staticmethod
    def faq_answer(index: int):
        return By.ID, f"accordion__panel-{index}"
