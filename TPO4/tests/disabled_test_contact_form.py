from pages.contact_page import ContactPage

VALID_NAME = "test"
VALID_EMAIL = "test@example.com"
VALID_MESSAGE = "Hello world!"
EMPTY = ""

def test_positive_contact_form(driver):
    page = ContactPage(driver)
    page.open_fill_submit_form(VALID_EMAIL, VALID_NAME, VALID_MESSAGE)

    success_text = page.get_success_message()
    assert "Спасибо" in success_text, "Сообщение об успешной отправке не найдено"
    
def test_negative_empty_email(driver):
    page = ContactPage(driver)
    page.open_fill_submit_form(EMPTY, VALID_NAME, VALID_MESSAGE)

    error_text = page.get_error_message()
    assert "Требуется" in error_text, "Сообщение об ошибке не отображается"
    