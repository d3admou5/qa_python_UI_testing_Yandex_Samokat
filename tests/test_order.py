import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators as MainLoc
from data.order_data import User1Data, User2Data
from data.url_data import MAIN_PAGE_URL

@pytest.mark.parametrize("user_data, order_button_locator", [
    (User1Data.data, MainLoc.ORDER_BUTTON_TOP),
    (User2Data.data, MainLoc.ORDER_BUTTON_BOTTOM)
])
def test_positive_order_flow(driver, user_data, order_button_locator):
    main_page = MainPage(driver)
    main_page.open(MAIN_PAGE_URL)
    main_page.scroll_to_element(order_button_locator)
    main_page.click(order_button_locator)

    order_page = OrderPage(driver)
    order_page.fill_first_form(user_data)
    order_page.fill_second_form(user_data)

    assert order_page.is_order_successful(), (
        f"Окно подтверждения заказа не появилось "
        f"({user_data['name']} + {'верхняя' if order_button_locator == MainLoc.ORDER_BUTTON_TOP else 'нижняя'} кнопка)"
    )
