from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "http://example.com"
def test_happy_upload():
    driver = webdriver.Edge()  # or Chrome
    driver.get(URL)
    driver.find_element(By.ID, "username").send_keys("testuser")
    driver.find_element(By.ID, "password").send_keys("password")
    driver.find_element(By.ID, "loginBtn").click()
    driver.find_element(By.ID, "uploadInput").send_keys("test_data/sample_video.mp4")
    driver.find_element(By.ID, "uploadBtn").click()
    time.sleep(5) 
    thumbnail = driver.find_element(By.ID, "videoThumbnail")
    assert thumbnail.is_displayed()

    driver.quit()
