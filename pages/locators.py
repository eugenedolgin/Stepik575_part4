from selenium.webdriver.common.by import By

class BasePageLocators :
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini>span.btn-group>a")

class MainPageLocators:
    pass
    
class LoginPageLocators:
    LOGIN_FIELD = (By.CSS_SELECTOR, "input#id_login-username")
    REGISTRATION_FIELD = (By.CSS_SELECTOR, "input#id_registration-email")
    
class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main>.price_color")
    
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "div#messages>div.alert-success:first-child strong")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, "div#messages>div.alert-info:last-child strong")
    
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#messages>div.alert-success:first-child")
    
class BasketPageLocators:    
    BASKET_NOT_EMPTY_TITLE = (By.CSS_SELECTOR, "div#content_inner>div.basket-title")
    BASKET_NOT_EMPTY_FORM = (By.CSS_SELECTOR, "form#basket_formset")
    TEXT_BASKET_EMPTY = (By.CSS_SELECTOR, "div#content_inner>p:only-of-type")