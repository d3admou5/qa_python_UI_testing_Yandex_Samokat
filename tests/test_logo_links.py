import allure
from data.url_data import MAIN_PAGE_URL, ORDER_PAGE_URL

@allure.feature("Логотипы")
class TestLogoLinks:

    @allure.story("Клик по логотипу Самоката")
    @allure.title("Проверка редиректа на главную при клике на логотип Самоката")
    @allure.description("""
    Когда пользователь находится на странице заказа и нажимает на логотип 'Самокат',
    должен произойти переход на главную страницу сайта.
    """)
    def test_click_scooter_logo_redirects_to_main(self, main_page):
        main_page.open_main_page(ORDER_PAGE_URL)
        main_page.click_scooter_logo()

        main_page.wait_for_url_to_be(MAIN_PAGE_URL)

        assert main_page.get_current_url() == MAIN_PAGE_URL, \
            "Не произошёл переход на главную страницу после клика на логотип Самоката"

    @allure.story("Клик по логотипу Яндекса")
    @allure.title("Проверка открытия Дзена при клике по логотипу Яндекса")
    @allure.description("""
    Когда пользователь находится на главной странице и нажимает на логотип 'Яндекс',
    в новом окне должен открыться сайт 'Дзен' (https://dzen.ru).
    """)
    def test_click_yandex_logo_opens_dzen_in_new_tab(self, main_page):
        main_page.open_main_page(MAIN_PAGE_URL)
        main_page.click_yandex_logo()
        main_page.switch_to_new_tab()

        main_page.wait_for_url_to_contain("dzen.ru")

        assert "dzen.ru" in main_page.get_current_url(), \
            "После клика на логотип Яндекса не открылся Дзен"
