from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    
    def run_test_product(self):
        self.should_be_add_to_basket()
        self.do_click_add_to_basket()
        #Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
        self.check_product_is_added()
        #Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара. 
        self.check_basket_price()

    def should_be_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button 'Add to basket' is not presented"
    
    def do_click_add_to_basket(self):
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        button_add = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add.click()
        self.solve_quiz_and_get_code()

    def check_product_is_added(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_BASKET), "No message about product added to basket"
        
        added_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert added_product == self.product_name, "Product name in basket is not correct"
        
    def check_basket_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET), "No message about basket price"

        added_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
        assert added_price == self.product_price, "Product Price in basket is not correct"
