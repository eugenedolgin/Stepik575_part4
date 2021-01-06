from .base_page import BasePage
# from .locators import MainPageLocators
# from selenium.webdriver.common.by import By
# from .login_page import LoginPage

class MainPage(BasePage): 
    
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
        # Конструктор с ключевым словом super вызывает конструктор класса предка 
        # и передает ему все те аргументы, которые мы передали в конструктор MainPage
        