from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class InfoW:
    def __init__(self):
        # Set up Chrome options to keep the browser open
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)  # Keeps the browser open
        
        # Initialize WebDriver with the detach option
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def get_info(self, query):
        self.query = query
        # Open Wikipedia's homepage
        self.driver.get("http://www.wikipedia.org")

        # Locate search input field and search button using By.XPATH
        search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)

        enter = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
        enter.click()

# Instantiate and use the class
if __name__ == "__main__":
    assist = InfoW()
    assist.get_info("java")
