from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
query = "modi"
driver.get(f"https://en.wikipedia.org/w/index.php?search={query}")
ele = driver.find_elements(By.TAG_NAME, "body")
for subele in ele:
    d = subele.get_attribute("outerHTML")
    with open(f"data/{query}.html","w",encoding="utf-8") as f:
        f.write(d)
driver.close()