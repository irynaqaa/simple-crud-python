class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *args):
        return self.driver.find_element(*args)

    def click(self, *args):
        self.find_element(*args).click()

    def input_text(self, *args, text):
        element = self.find_element(*args)
        element.clear()
        element.send_keys(text)
