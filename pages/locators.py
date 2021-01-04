from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators:
    LOGIN_FIELD = (By.CSS_SELECTOR, "input#id_login-username")
    REGISTRATION_FIELD = (By.CSS_SELECTOR, "input#id_registration-email")
    
