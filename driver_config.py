
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import config 
def get_driver():
    """Создание и настройка драйвера для Chrome"""
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    
    service = Service(config.CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    
    return driver
