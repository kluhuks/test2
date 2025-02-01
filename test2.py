import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import driver_config
import config

class TestWikiEdit(unittest.TestCase):
    def setUp(self):

        self.driver = driver_config.get_driver()
    
    def test_edit_wiki_page(self):

        start_time = time.time()
        
        self.driver.get(config.URL)
        self.driver.maximize_window()
        time.sleep(2)
        
        edit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ca-edit"))
        )
        edit_button.click()
        
        time.sleep(2)
        
        text_area = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "wpTextbox1"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", text_area)
        text_area.send_keys("\n\nДополнительная информация о планетах.")
        
        reason_field = self.driver.find_element(By.ID, "wpSummary")
        reason_field.send_keys("Добавлена информация о планетах.")
        
        save_button = self.driver.find_element(By.ID, "wpSave")
        save_button.click()
        
        time.sleep(2)
        
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения теста: {execution_time:.2f} секунд")
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
