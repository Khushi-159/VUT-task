from selenium import webdriver
from selenium.webdriver.common.by import By
URL = "http://example.com"
def test_metadata_update():
    driver = webdriver.Edge()
    driver.get(URL)
    driver.find_element(By.ID, "username").send_keys("testuser")
    driver.find_element(By.ID, "password").send_keys("password")
    driver.find_element(By.ID, "loginBtn").click()
    driver.find_element(By.ID, "uploadInput").send_keys("test_data/sample_video.mp4")
    driver.find_element(By.ID, "uploadBtn").click()
    driver.find_element(By.ID, "titleInput").clear()
    driver.find_element(By.ID, "titleInput").send_keys("Updated Title")
    driver.find_element(By.ID, "saveMetadata").click()
    updated_title = driver.find_element(By.ID, "titleInput").get_attribute("value")
    assert updated_title == "Updated Title"

    driver.quit()
