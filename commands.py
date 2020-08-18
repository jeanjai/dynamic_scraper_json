from selenium import webdriver
import requests


class base():

    chrome_path = "webdrivers/chromedriver"

    def __init__(self):
        self.driver = webdriver.Chrome(self.chrome_path)
    
    def getHttpCode(self, url):
        try:
            r = requests.head(url)
            return r.status_code
        except requests.ConnectionError:
            return False

    def isUrlValid(self, url):
        httpCode = self.getHttpCode(url)
        if httpCode == 200:
            return True
        else:
            return False

    def visit(self, url):
        self.driver.get(url)

    def end(self):
        self.driver.close()

    def isSelectorVisible(self, selector):
        for i in range(100):
            try:
                self.driver.find_element_by_css_selector(selector)
                return True
            except Exception as e:
                continue
        print ("Couldn't find selector " + selector + " in " + self.driver.current_url)
        return False

    def findElem(self, selector):
        if self.isSelectorVisible(selector):
            return self.driver.find_element_by_css_selector(selector)
        else:
            return False

    def findElems(self, selector):
        if self.isSelectorVisible(selector):
            return self.driver.find_elements_by_css_selector(selector)
        else:
            return False

    def click(self, selector):
        elem = self.findElem(selector)
        if elem:
            elem.click()

    def write(self, selector, text):
        elem = self.findElem(selector)
        if elem:
            elem.send_keys(text)

    def getValue(self, selector):
        elem = self.findElem(selector)
        if elem:
            return [elem.text]
        else:
            return ['']

    def getValues(self, selector):
        elems = self.findElems(selector)
        if elems:
            data = []
            for elem in elems:
                data.append(elem.text)
            return data
        else:
            return ['']

    def getAttribute(self, selector, attribute):
        elem = self.findElem(selector)
        if elem:
            return elem.get_attribute(attribute)

    def getAttributes(self, selector, attribute):
        elems = self.findElems(selector)
        if elems:
            data = []
            for elem in elems:
                data.append(elem.get_attribute(attribute))
            return data

    def getLink(self, selector):
        return self.getAttribute(selector, "href")

    def getLinks(self, selector):
        return self.getAttributes(selector, "href")
