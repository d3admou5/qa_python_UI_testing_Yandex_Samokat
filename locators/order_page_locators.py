from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Первая форма заказа
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_DROPDOWN_OPTIONS = (By.CLASS_NAME, "select-search__options")
    METRO_OPTION_BY_TEXT = lambda text: (By.XPATH, f"//div[text()='{text}']")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Вторая форма заказа
    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_DAYS_DROPDOWN = (By.CLASS_NAME, "Dropdown-root")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать']")
    CONFIRM_BUTTON_YES = (By.XPATH, "//button[text()='Да']")
    CONFIRM_BUTTON_NO = (By.XPATH, "//button[text()='Нет']")
    CHECK_STATUS_OF_ORDER = (By.XPATH, "//*[text()='Посмотреть статус']")

    # Динамика
    @staticmethod
    def metro_option(station_name):
        return By.XPATH, f"//div[text()='{station_name}']"

    @staticmethod
    def rent_day_option(days_text):
        return By.XPATH, f"//div[@class='Dropdown-menu']/div[text()='{days_text}']"
