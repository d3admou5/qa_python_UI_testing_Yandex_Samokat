import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Ожидание видимости элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание кликабельности элемента")
    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Кликнуть на элемент")
    def click(self, locator, timeout=10):
        element = self.wait_for_clickable(locator, timeout)
        element.click()

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_tab(self):
        current_tabs = self.driver.window_handles
        self.driver.switch_to.window(current_tabs[-1])

    @allure.step("Получить текст элемента")
    def get_text(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step("Получить заголовок страницы")
    def get_page_title(self):
        return self.driver.title

    @allure.step("Нажать клавишу {key} в элементе")
    def send_key_to_element(self, locator, key, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.send_keys(key)

    @allure.step("Выбрать значение '{target_text}' из выпадающего списка")
    def select_option_from_dropdown(self, dropdown_locator, options_locator, target_text, timeout=10):
        self.click(dropdown_locator)
        options = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(options_locator))
        for option in options:
            if target_text.lower() in option.text.lower():
                option.click()
                return
        raise Exception(f"Опция '{target_text}' не найдена в списке")

    @allure.step("Нажать клавишу Escape")
    def press_escape(self):
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
