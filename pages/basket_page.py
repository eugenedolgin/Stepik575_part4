from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_NOT_EMPTY_FORM), "Basket not empty,  shoul be empty"
            
    def should_be_text_basket_is_empty(self):
        message = (("ru","Ваша корзина пуста"), ("en-gb","Your basket is empty"))
        
        assert self.is_element_present(*BasketPageLocators.TEXT_BASKET_EMPTY), "No text about Basket empty,  shoul be this text"
        basket_text = self.browser.find_element(*BasketPageLocators.TEXT_BASKET_EMPTY).text
        for mess in message:
            if self.browser.current_url.endswith(f"/{mess[0]}/basket/"):
                assert mess[1] in basket_text, f"No text '{mess[1]}'({mess[0]}) about Basket empty,  shoul be this text"
                break
        else:
            assert False, f"Not defined text '{basket_text}' on page '{self.browser.current_url}'"