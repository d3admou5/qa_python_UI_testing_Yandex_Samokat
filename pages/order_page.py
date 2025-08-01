from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators as Loc
from selenium.webdriver.common.keys import Keys
import allure

class OrderPage(BasePage):

    @allure.step("Заполнить первую форму заказа")
    def fill_first_form(self, user_data):
        with allure.step(f"Ввод имени: {user_data['name']}"):
            self.send_keys_to_input(Loc.NAME, user_data["name"])
        with allure.step(f"Ввод фамилии: {user_data['surname']}"):
            self.send_keys_to_input(Loc.LASTNAME, user_data["surname"])
        with allure.step(f"Ввод адреса: {user_data['address']}"):
            self.send_keys_to_input(Loc.ADDRESS, user_data["address"])
        with allure.step(f"Выбор станции метро: {user_data['metro']}"):
            self.send_keys_to_input(Loc.METRO_INPUT, user_data["metro"])
            self.click(Loc.METRO_DROPDOWN_OPTIONS)
        with allure.step(f"Ввод номера телефона: {user_data['phone']}"):
            self.send_keys_to_input(Loc.PHONE, user_data["phone"])
        with allure.step("Клик на кнопку 'Далее'"):
            self.click(Loc.NEXT_BUTTON)

    @allure.step("Заполнить вторую форму заказа")
    def fill_second_form(self, user_data):
        with allure.step(f"Выбор даты: {user_data['date']}"):
            self.send_keys_to_input(Loc.DATE, user_data["date"])
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ESCAPE).perform()

        with allure.step(f"Выбор срока аренды: {user_data['rent_days']}"):
            self.click(Loc.RENT_DAYS_DROPDOWN)
            rent_options = self.driver.find_elements(*Loc.RENT_DAYS_OPTIONS)
            for option in rent_options:
                if user_data["rent_days"].lower() in option.text.lower():
                    option.click()
                    break

        with allure.step(f"Выбор цвета: {user_data['color']}"):
            if user_data["color"].lower() == "grey":
                self.click(Loc.COLOR_GREY)
            elif user_data["color"].lower() == "black":
                self.click(Loc.COLOR_BLACK)

        with allure.step(f"Добавление комментария: {user_data['comment']}"):
            self.send_keys_to_input(Loc.COMMENT, user_data["comment"])

        with allure.step("Подтверждение заказа"):
            self.click(Loc.ORDER_BUTTON)
            self.click(Loc.CONFIRM_BUTTON_YES)

    @allure.step("Проверка, что заказ успешно оформлен")
    def is_order_successful(self):
        return self.wait_for_element(Loc.CHECK_STATUS_OF_ORDER)
