from selenium import webdriver
from selenium.webdriver.common.by import By
import time
URL = "http://example.com"
def test_unsupported_file_upload():
    driver = webdriver.Edge()
    driver.get(URL)
    driver.find_element(By.ID, "uploadInput").send_keys("test_data/invalid_video.txt")
    driver.find_element(By.ID, "uploadBtn").click()
    time.sleep(2)
    error = driver.find_element(By.ID, "uploadError")
    assert "unsupported" in error.text.lower()

    driver.quit()
