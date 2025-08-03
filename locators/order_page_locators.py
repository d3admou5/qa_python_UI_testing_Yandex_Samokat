from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Первая форма заказа
    TITLE_HEADER_FORM1 = (By.XPATH, "//div[contains(text(), 'Для кого самокат')]")
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LASTNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_DROPDOWN_OPTIONS = (By.XPATH, "//*[contains(@class, 'select-search__row')]")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(), 'Далее')]")

    # Вторая форма заказа
    TITLE_HEADER_FORM2 = (By.XPATH, "//div[contains(text(), 'Про аренду')]")
    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    CALENDAR = (By.XPATH, "//div[contains(@class, 'react-datepicker_popper')]")
    CALENDAR_ITEM = (By.XPATH, "//div[contains(@class, 'react-datepicker')]")
    RENT_DAYS_DROPDOWN = (By.XPATH, "//*[contains(@class, 'Dropdown-root')]")
    RENT_DAYS_OPTIONS = (By.XPATH, "//div[contains(@class, 'Dropdown-option')]")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    ORDER_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")
    CONFIRM_BUTTON_YES = (By.XPATH, "//button[contains(text(), 'Да')]")
    CONFIRM_BUTTON_NO = (By.XPATH, "//button[contains(text(), 'Нет')]")
    CHECK_STATUS_OF_ORDER = (By.XPATH, "//*[contains(text(), 'Посмотреть статус')]")
