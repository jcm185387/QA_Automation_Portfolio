
### `test_login.py`
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button.radius").click()

success_message = driver.find_element(By.ID, "flash").text
assert "You logged into a secure area!" in success_message

print("Prueba de login exitosa ✅")
time.sleep(3)
driver.quit()
