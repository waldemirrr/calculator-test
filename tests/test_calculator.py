import allure
from allure import severity, severity_level
from pages.calculator_page import CalculatorPage


@severity(severity_level.BLOCKER)
def test_open(driver):
    calculator_page = CalculatorPage(driver)
    with allure.step('Проверить присутствует ли класс калькулятора'):
        assert calculator_page.get_calculator()


# test id - 2
@severity(severity_level.BLOCKER)
def test_all_numbers(driver):
    calculator_page = CalculatorPage(driver)
    with allure.step('Нажать все кнопки с цифровыми значениями'):
        calculator_page.press_button('1')
        calculator_page.press_button('2')
        calculator_page.press_button('3')
        calculator_page.press_button('4')
        calculator_page.press_button('5')
        calculator_page.press_button('6')
        calculator_page.press_button('7')
        calculator_page.press_button('8')
        calculator_page.press_button('9')
        calculator_page.press_button('0')
        calculator_page.press_button('00')
    with allure.step('Проверить первый операнд на наличие всех цифровых значений кнопок'):
        assert calculator_page.get_first_operand() == '123456789000'


# test id - 3
@severity(severity_level.BLOCKER)
def test_plus_operator(driver):
    calculator_page = CalculatorPage(driver)
    with allure.step('Нажать на кнопку 1'):
        calculator_page.press_button('1')
    with allure.step('Нажать на оператор +'):
        calculator_page.press_button('+')
    with allure.step('Нажать на кнопку 1'):
        calculator_page.press_button('1')
    with allure.step('Нажать на оператор ='):
        calculator_page.press_button('=')
    assert calculator_page.get_result() == '2'


# test id - 4
@severity(severity_level.BLOCKER)
def test_minus_operator(driver):
    calculator_page = CalculatorPage(driver)
    with allure.step('Нажать на кнопку 1'):
        calculator_page.press_button('1')
    with allure.step('Нажать на оператор -'):
        calculator_page.press_button('-')
    with allure.step('Нажать на кнопку 1'):
        calculator_page.press_button('1')
    with allure.step('Нажать на оператор ='):
        calculator_page.press_button('=')
    assert calculator_page.get_result() == '0'


# test id - 5
@severity(severity_level.BLOCKER)
def test_multiply_operator(driver):
    calculator_page = CalculatorPage(driver)
    with allure.step('Нажать на кнопку 2'):
        calculator_page.press_button('2')
    with allure.step('Нажать на оператор *'):
        calculator_page.press_button('*')
    with allure.step('Нажать на кнопку 2'):
        calculator_page.press_button('2')
    with allure.step('Нажать на оператор ='):
        calculator_page.press_button('=')
    assert calculator_page.get_result() == '4'


# test id - 6
@severity(severity_level.BLOCKER)
def test_divide_operator(driver):
    calculator_page = CalculatorPage(driver)
    with allure.step('Нажать на кнопку 2'):
        calculator_page.press_button('2')
    with allure.step('Нажать на оператор /'):
        calculator_page.press_button('/')
    with allure.step('Нажать на кнопку 2'):
        calculator_page.press_button('2')
    with allure.step('Нажать на оператор ='):
        calculator_page.press_button('=')
    assert calculator_page.get_result() == '1'


# test id - 7
@severity(severity_level.CRITICAL)
def test_delete_symbol_operator(driver):
    calculator_page = CalculatorPage(driver)
    with allure.step('Нажать на кнопку 1'):
        calculator_page.press_button('1')
    with allure.step('Нажать на оператор +'):
        calculator_page.press_button('+')
    with allure.step('Нажать на кнопку 1'):
        calculator_page.press_button('1')
    with allure.step('Нажать три раза на оператор ←'):
        for _ in range(3):
            calculator_page.press_button('←')
    with allure.step('Проверить первый операнд, оператор и второй операнд на отсутствие значений'):
        assert calculator_page.get_first_operand() == ''
        assert calculator_page.get_operator() == ''
        assert calculator_page.get_second_operand() == ''


# test id - 8
@severity(severity_level.CRITICAL)
def test_clear_all(driver):
    calculator_page = CalculatorPage(driver)
    with allure.step('Нажать на кнопку 1'):
        calculator_page.press_button('1')
    with allure.step('Нажать на кнопку +'):
        calculator_page.press_button('+')
    with allure.step('Нажать на кнопку 1'):
        calculator_page.press_button('1')
    with allure.step('Нажать на оператор CA'):
        calculator_page.press_button('CA')
    with allure.step('Проверить первый операнд, оператор и второй операнд на отсутствие значений'):
        assert calculator_page.get_first_operand() == ''
        assert calculator_page.get_operator() == ''
        assert calculator_page.get_second_operand() == ''


# test id - 9.1
@severity(severity_level.BLOCKER)
def test_plus_minus_operator_on_first_operand(driver):
    calculator_page = CalculatorPage(driver)
    with allure.step('Нажать на кнопку 1'):
        calculator_page.press_button('1')
    with allure.step('Нажать на оператор +/-, проверить что у первого операнда отрицательное значение'):
        calculator_page.press_button('+/-')
        assert calculator_page.get_first_operand() == '-1'
    with allure.step('Нажать на оператор +/-, проверить что у первого операнда положительное значение'):
        calculator_page.press_button('+/-')
        assert calculator_page.get_first_operand() == '1'



# test id - 9.2
@severity(severity_level.BLOCKER)
def test_plus_minus_operator_on_second_operand(driver):
    calculator_page = CalculatorPage(driver)
    with allure.step('Нажать на кнопку 1'):
        calculator_page.press_button('1')
    with allure.step('Нажать на оператор +'):
        calculator_page.press_button('+')
    with allure.step('Нажать на кнопку 1'):
        calculator_page.press_button('1')
    with allure.step('Нажать на оператор +/-, проверить что у второго операнда отрицательное значение'):
        calculator_page.press_button('+/-')
        assert calculator_page.get_second_operand() == '-1'
    with allure.step('Нажать на оператор +/-, проверить что у второго операнда положительное значение'):
        calculator_page.press_button('+/-')
        assert calculator_page.get_second_operand() == '1'

# test id - 9.3
@severity(severity_level.BLOCKER)
def test_plus_minus_operator_in_operation(driver):
    calculator_page = CalculatorPage(driver)
    with allure.step('Нажать на кнопку 1'):
        calculator_page.press_button('1')
    with allure.step('Нажать на оператор +/-'):
        calculator_page.press_button('+/-')
    with allure.step('Нажать на оператор +'):
        calculator_page.press_button('+')
    with allure.step('Нажать на кнопку 1'):
        calculator_page.press_button('1')
    with allure.step('Нажать на оператор +/-'):
        calculator_page.press_button('+/-')
    with allure.step('Нажать на оператор ='):
        calculator_page.press_button('=')
    assert calculator_page.get_result() == '-2'


# test id - 10
@severity(severity_level.BLOCKER)
def test_float_point_number_operations(driver):
    calculator_page = CalculatorPage(driver)
    with allure.step('Нажать на кнопку 1'):
        calculator_page.press_button('1')
    with allure.step('Нажать на оператор .'):
        calculator_page.press_button('.')
    with allure.step('Нажать на кнопку 1'):
        calculator_page.press_button('1')
    with allure.step('Нажать на оператор +'):
        calculator_page.press_button('+')
    with allure.step('Нажать на кнопку 1'):
        calculator_page.press_button('1')
    with allure.step('Нажать на оператор .'):
        calculator_page.press_button('.')
    with allure.step('Нажать на кнопку 1'):
        calculator_page.press_button('1')
    with allure.step('Нажать на оператор ='):
        calculator_page.press_button('=')
    assert calculator_page.get_result() == '2.2'


# test id - 11
@severity(severity_level.CRITICAL)
def test_operation_with_result(driver):
    calculator_page = CalculatorPage(driver)
    with allure.step('Нажать на кнопку 1'):
        calculator_page.press_button('1')
    with allure.step('Нажать на оператор +'):
        calculator_page.press_button('+')
    with allure.step('Нажать на кнопку 1'):
        calculator_page.press_button('1')
    with allure.step('Нажать на оператор ='):
        calculator_page.press_button('=')
    with allure.step('Нажать на оператор +'):
        calculator_page.press_button('+')
    with allure.step('Нажать на кнопку 1'):
        calculator_page.press_button('1')
    with allure.step('Нажать на оператор ='):
        calculator_page.press_button('=')
    assert calculator_page.get_result() == '3'


# test id - 12
@severity(severity_level.NORMAL)
def test_sum_of_two_empty_floating_points(driver):
    calculator_page = CalculatorPage(driver)
    with allure.step('Нажать на оператор .'):
        calculator_page.press_button('.')
    with allure.step('Нажать на оператор +'):
        calculator_page.press_button('+')
    with allure.step('Нажать на оператор .'):
        calculator_page.press_button('.')
    with allure.step('Нажать на первый операнд, второй операнд, и оператор'):
        assert calculator_page.get_first_operand() == '.'
        assert calculator_page.get_operator() == ''
        assert calculator_page.get_second_operand() == ''


# test id - 13
@severity(severity_level.NORMAL)
def test_plus_minus_operator_on_a_point(driver):
    calculator_page = CalculatorPage(driver)
    with allure.step('Нажать на оператор .'):
        calculator_page.press_button('.')
    with allure.step('Нажать на оператор +/-'):
        calculator_page.press_button('+/-')
    with allure.step('Проверить первый операнд'):
        assert calculator_page.get_first_operand() == '.'


# test id - 14
@severity(severity_level.NORMAL)
def test_plus_minus_operator_on_empty_operand(driver):
    calculator_page = CalculatorPage(driver)
    with allure.step('Нажать на оператор +/-'):
        calculator_page.press_button('+/-')
    with allure.step('Проверить первый операнд'):
        assert calculator_page.get_first_operand() == ''


# test id - 15
@severity(severity_level.NORMAL)
def test_plus_operator_on_an_empty_operand(driver):
    calculator_page = CalculatorPage(driver)
    with allure.step('Нажать на оператор +'):
        calculator_page.press_button('+')
    with allure.step('Нажать оператор'):
        assert calculator_page.get_operator() == ''


# test id - 16
@severity(severity_level.NORMAL)
def test_delete_symbol_operator_on_an_empty_first_operand(driver):
    calculator_page = CalculatorPage(driver)
    with allure.step('Нажать на оператор ←'):
        calculator_page.press_button('←')
    with allure.step('Проверить первый операнд'):
        assert calculator_page.get_first_operand() == ''


# test id - 17
@severity(severity_level.BLOCKER)
def test_plus_minus_operator_on_a_floating_point_number_operand(driver):
    calculator_page = CalculatorPage(driver)
    with allure.step('Нажать на кнопку 1'):
        calculator_page.press_button('1')
    with allure.step('Нажать на оператор .'):
        calculator_page.press_button('.')
    with allure.step('Нажать на кнопку 1'):
        calculator_page.press_button('1')
    with allure.step('Нажать на кнопку +/-'):
        calculator_page.press_button('+/-')
    with allure.step('Проверить первый операнд на отрицательность'):
        assert calculator_page.get_first_operand() == '-1.1'
    with allure.step('Нажать на оператор +/-'):
        calculator_page.press_button('+/-')
    with allure.step('Проверить первый операнд на положительность'):
        assert calculator_page.get_first_operand() == '1.1'
