import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators as MainLoc
from data.order_data import User1Data, User2Data
from data.url_data import MAIN_PAGE_URL

@allure.feature("Оформление заказа")
@allure.title("Позитивный тест оформления заказа с кнопки '{order_button_name}'")
@allure.description("Тест проверяет успешное оформление заказа через верхнюю и нижнюю кнопку 'Заказать'")
@pytest.mark.parametrize("user_data, order_button_locator, order_button_name", [
    (User1Data.data, MainLoc.ORDER_BUTTON_TOP, "верхняя"),
    (User2Data.data, MainLoc.ORDER_BUTTON_BOTTOM, "нижняя")
])
def test_positive_order_flow(driver, user_data, order_button_locator, order_button_name):
    with allure.step(f"Открытие главной страницы {MAIN_PAGE_URL}"):
        main_page = MainPage(driver)
        main_page.open(MAIN_PAGE_URL)

    with allure.step(f"Скролл и клик по {order_button_name} кнопке 'Заказать'"):
        main_page.scroll_to_element(order_button_locator)
        main_page.click(order_button_locator)

    order_page = OrderPage(driver)

    with allure.step("Заполнение первой формы заказа"):
        order_page.fill_first_form(user_data)

    with allure.step("Заполнение второй формы заказа"):
        order_page.fill_second_form(user_data)

    with allure.step("Проверка появления окна подтверждения заказа"):
        assert order_page.is_order_successful(), (
            f"Окно подтверждения заказа не появилось "
            f"({user_data['name']} + {order_button_name} кнопка)"
        )
