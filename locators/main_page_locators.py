from selenium.webdriver.common.by import By

class MainPageLocators:
    # Логотипы
    SCOOTER_LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
    YANDEX_LOGO = (By.XPATH, "//a[@href='//yandex.ru']")

    # Кнопки заказа
    ORDER_BUTTON_TOP = (By.XPATH, "//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[text()='Заказать'])[2]")

    # FAQ
    FAQ_SECTION = (By.XPATH, "//div[contains(@class, 'Home_FAQ')]")

    # Вопросы
    FAQ_QUESTIONS = [(By.ID, f"accordion__heading-{i}") for i in range(8)]

    # FAQ - ответы
    FAQ_ANSWERS = [(By.ID, f"accordion__panel-{i}") for i in range(8)]