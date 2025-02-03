from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Music():
    def __init__(self):
       chrome_options = Options()
       chrome_options.add_experimental_option("detach", True)  # Keeps the browser open
        
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    def play(self, query):
        self.query = query
       
        self.driver.get("http://www.youtube.com/results?search_query=" + query)

        video = self.driver.find_element(By.XPATH, '//*[@id="dismissable"]')
        video.click()

if __name__ == "__main__":
    assist = Music()
    assist.play("vini production")

       