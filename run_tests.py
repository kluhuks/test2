import unittest
from test_wiki_edit import TestWikiEdit
import time
import driver_config
import config
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_unittests(report_file):
    """
    Выполняет юнит-тесты с использованием unittest и записывает результаты в файл отчета.
    
    Аргументы:
        report_file (file-like object): Файл, в который будет записан отчет о выполнении тестов.
        
    Возвращает:
        result (unittest.result.TestResult): Результат выполнения тестов.
    """
    # Создаем тестовый набор и запускаем его
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWikiEdit)
    runner = unittest.TextTestRunner(stream=report_file, verbosity=2)
    result = runner.run(suite)
    return result

def run_selenium_tests(report_file):
    """
    Выполняет тесты с использованием Selenium и записывает результаты в файл отчета.
    
    Аргументы:
        report_file (file-like object): Файл, в который будет записан отчет о выполнении тестов.
        
    Эта функция выполняет тестирование редактирования страницы Wikipedia с использованием Selenium.
    Тест включает в себя открытие страницы, редактирование и сохранение изменений.
    Если тест проходит успешно, записывается время его выполнения, иначе - сообщение об ошибке.
    """
    report_file.write("\nSelenium Tests Output:\n")
    try:
        # Запуск Selenium теста
        start_time = time.time()

        # Инициализация веб-драйвера и переход на страницу Wikipedia
        driver = driver_config.get_driver()
        driver.get(config.URL)
        driver.maximize_window()
        
        # Ожидание кнопки редактирования и кликаем по ней
        edit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ca-edit"))
        )
        edit_button.click()
        
        # Ожидание появления поля ввода текста
        text_area = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "wpTextbox1"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", text_area)
        text_area.send_keys("\n\nДополнительная информация о планетах.")
        
        # Ввод комментария
        reason_field = driver.find_element(By.ID, "wpSummary")
        reason_field.send_keys("Добавлена информация о планетах.")
        
        # Сохранение изменений
        save_button = driver.find_element(By.ID, "wpSave")
        save_button.click()
        
        time.sleep(2)
        
        # Измерение времени выполнения теста
        end_time = time.time()
        execution_time = end_time - start_time
        report_file.write(f"Время выполнения теста Selenium: {execution_time:.2f} секунд\n")
        
        # Завершение работы с драйвером
        driver.quit()
        
    except Exception as e:
        # Запись ошибки, если тест не прошел
        report_file.write(f"Ошибка при выполнении Selenium-тестов: {e}\n")

# Главная функция для запуска всех тестов
if __name__ == '__main__':
    """
    Главная функция для запуска юнит-тестов и Selenium-тестов, с записью результатов в файл отчета.
    Этот метод выполняет два типа тестов: юнит-тесты с использованием unittest и тесты с использованием Selenium.
    Результаты выполнения каждого из тестов записываются в файл test_report.txt.
    """
    with open("test_report.txt", "w", encoding="utf-8") as report_file:
        report_file.write("=== Юнит-тесты ===\n")
        run_unittests(report_file)
        report_file.write("\n=== Selenium-тесты ===\n")
        run_selenium_tests(report_file)
