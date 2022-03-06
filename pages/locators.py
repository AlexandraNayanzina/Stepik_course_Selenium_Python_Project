from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_LINK = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info  > .alertinner > p strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main > p.price_color")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon > .alertinner  >  strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")



