import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait

URL="http://127.0.0.1:5001"

@pytest.fixture
def driver():
    driver=webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_print_customers_table(driver, self=None):
    driver.get(URL)

    # click login in home page
    driver.find_element(By.LINK_TEXT,"Login").click()

    # enter login credentials and navigate to customers poge
    driver.find_element(By.XPATH,"//input[@name='username']").send_keys("admin")
    driver.find_element(By.NAME,"password").send_keys("Password123")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()

    # print customers table

    WebDriverWait(driver,10).until(EC.title_contains("Customers"))

    # find table, rows columns
    table=driver.find_element(By.TAG_NAME,"table")
    rows=table.find_elements(By.TAG_NAME,"tr")
    print ("\n Customers Table---")
    i=0
    for row in rows:
        if i==0:
            cols = row.find_elements(By.TAG_NAME, "th")
        else:
            cols = row.find_elements(By.TAG_NAME, "td")
        i = i + 1
        print([col.text for col in cols])

    print("--- End of Table ---\n")

