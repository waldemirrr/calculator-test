from selenium.webdriver.common.by import By


class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://waldemirrr.github.io/calculator/'
        self.open()

    def open(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.quit()

    def press_button(self, button_value):
        button_locator = self.driver.find_element(By.XPATH, f'//button[text()="{button_value}"]')
        button_locator.click()

    def get_calculator(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.calculator')

    def get_first_operand(self):
        first_operand = self.driver.find_element(By.CSS_SELECTOR, '.display__firstOperand')
        return first_operand.text

    def get_operator(self):
        operator = self.driver.find_element(By.CSS_SELECTOR, '.display__operator')
        return operator.text

    def get_second_operand(self):
        second_operand = self.driver.find_element(By.CSS_SELECTOR, '.display__secondOperand')
        return second_operand.text

    def get_result(self):
        result = self.driver.find_element(By.CSS_SELECTOR, '.display__result')
        return result.text
