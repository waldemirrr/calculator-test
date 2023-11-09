from pages.calculator_page import CalculatorPage


def test_open(driver):
    calculator_page = CalculatorPage(driver)
    assert calculator_page.get_calculator()


# test id - 2
def test_all_numbers(driver):
    calculator_page = CalculatorPage(driver)
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
    assert calculator_page.get_first_operand() == '123456789000'


# test id - 3
def test_plus_operator(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.press_button('1')
    calculator_page.press_button('+')
    calculator_page.press_button('1')
    calculator_page.press_button('=')
    assert calculator_page.get_result() == '2'


# test id - 4
def test_minus_operator(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.press_button('1')
    calculator_page.press_button('-')
    calculator_page.press_button('1')
    calculator_page.press_button('=')
    assert calculator_page.get_result() == '0'


# test id - 5
def test_multiply_operator(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.press_button('2')
    calculator_page.press_button('*')
    calculator_page.press_button('2')
    calculator_page.press_button('=')
    assert calculator_page.get_result() == '4'


# test id - 6
def test_divide_operator(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.press_button('2')
    calculator_page.press_button('/')
    calculator_page.press_button('2')
    calculator_page.press_button('=')
    assert calculator_page.get_result() == '1'


# test id - 7
def test_delete_symbol_operator(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.press_button('1')
    calculator_page.press_button('+')
    calculator_page.press_button('1')
    for _ in range(3):
        calculator_page.press_button('←')
    assert calculator_page.get_first_operand() == ''
    assert calculator_page.get_operator() == ''
    assert calculator_page.get_second_operand() == ''


# test id - 8
def test_clear_all(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.press_button('1')
    calculator_page.press_button('+')
    calculator_page.press_button('1')
    calculator_page.press_button('CA')
    assert calculator_page.get_first_operand() == ''
    assert calculator_page.get_operator() == ''
    assert calculator_page.get_second_operand() == ''


# test id - 9
def test_plus_minus_operator(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.press_button('1')
    calculator_page.press_button('+/-')
    calculator_page.press_button('+/-')
    calculator_page.press_button('+')
    calculator_page.press_button('1')
    calculator_page.press_button('+/-')
    calculator_page.press_button('+/-')
    assert calculator_page.get_first_operand() == '1'
    assert calculator_page.get_operator() == '+'
    assert calculator_page.get_second_operand() == '1'


# test id - 10
def test_float_point_number_operations(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.press_button('1')
    calculator_page.press_button('.')
    calculator_page.press_button('1')
    calculator_page.press_button('+')
    calculator_page.press_button('1')
    calculator_page.press_button('.')
    calculator_page.press_button('1')
    calculator_page.press_button('=')
    assert calculator_page.get_result() == '2.2'


# test id - 11
def test_operation_with_result(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.press_button('1')
    calculator_page.press_button('+')
    calculator_page.press_button('1')
    calculator_page.press_button('=')
    calculator_page.press_button('+')
    calculator_page.press_button('1')
    calculator_page.press_button('=')
    assert calculator_page.get_result() == '3'


# test id - 12
def test_sum_of_two_empty_floating_points(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.press_button('.')
    calculator_page.press_button('+')
    calculator_page.press_button('.')
    assert calculator_page.get_result() == ''


# test id - 13
def test_plus_minus_operator_on_a_point(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.press_button('.')
    calculator_page.press_button('+/-')
    assert calculator_page.get_first_operand() == '.'


# test id - 14
def test_plus_minus_operator_on_empty_operand(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.press_button('+/-')
    assert calculator_page.get_first_operand() == ''


# test id - 15
def test_plus_operator_on_an_empty_operand(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.press_button('+')
    assert calculator_page.get_operator() == ''


# test id - 16
def test_delete_symbol_operator_on_an_empty_operand(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.press_button('←')
    assert calculator_page.get_first_operand() == ''


# test id - 17
def test_plus_minus_operator_on_a_floating_point_number_operand(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.press_button('1')
    calculator_page.press_button('.')
    calculator_page.press_button('1')
    calculator_page.press_button('+/-')
    assert calculator_page.get_first_operand() == '-1.1'
    calculator_page.press_button('+/-')
    assert calculator_page.get_first_operand() == '1.1'
