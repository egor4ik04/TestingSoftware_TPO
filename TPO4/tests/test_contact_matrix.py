from pages.contact_page import ContactPage

VALID_NAME = "test"
VALID_EMAIL = "test@example.com"
VALID_MESSAGE = "Hello world!"
EMPTY = ""

def matrix_test_contact_form_template(driver, case, email, name, message, expected):
    page = ContactPage(driver)
    page.open_fill_submit_form(email, name, message)
    success = page.get_success_message()
    error = page.get_error_message()
    result_text = success or error

    assert expected in result_text, f"Кейс {case} не пройден: ожидалось '{expected}', получено '{result_text}'"

def test_case_1(driver):
    matrix_test_contact_form_template(driver, 1, VALID_EMAIL, VALID_NAME, VALID_MESSAGE, "Спасибо")
def test_case_2(driver):
    matrix_test_contact_form_template(driver, 2, VALID_EMAIL, VALID_NAME, EMPTY, "Требуется сообщение")
def test_case_3(driver):
    matrix_test_contact_form_template(driver, 3, VALID_EMAIL, EMPTY, VALID_MESSAGE, "Спасибо")
def test_case_4(driver):
    matrix_test_contact_form_template(driver, 4, VALID_EMAIL, EMPTY, EMPTY, "Требуется сообщение")
def test_case_5(driver):
    matrix_test_contact_form_template(driver, 5, EMPTY, VALID_NAME, VALID_MESSAGE, "Требуется email")
def test_case_6(driver):
    matrix_test_contact_form_template(driver, 6, EMPTY, VALID_NAME, EMPTY, "Требуется email")
def test_case_7(driver):
    matrix_test_contact_form_template(driver, 7, EMPTY, EMPTY, VALID_MESSAGE, "Требуется email")
def test_case_8(driver):
    matrix_test_contact_form_template(driver, 8, EMPTY, EMPTY, EMPTY, "Требуется email")
