class BasePage():

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        # url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/category/books_2/"
        self.browser.get(self.url)
