from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import tkinter


def site_login():
    driver.get("https://www.facebook.com/")
    driver.find_element_by_id("email").send_keys("xxxxxxxxx")
    driver.find_element_by_id("pass").send_keys("xxxxxxxx")
    driver.find_element_by_name("login").click()


def site_logout():
    # wait for the account button
    try:
        # get account button
        account = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label=Account]")))
        account.click()
        # get logout button
        logout = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[text()='Esci']")))
        # logout
        logout.click()

    except:
        print("error!")

def wikipedia():
    driver.get("https://it.wikipedia.org/wiki/Pagina_principale")
    driver.find_element_by_id("searchInput").send_keys("Firenze")
    driver.find_element_by_id("searchButton").click()


def close():
    driver.close()
    sys.exit(1)

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)

root = tkinter.Tk()
myButton = tkinter.Button(root, text="try me", padx=50, pady=30, command=wikipedia)
myButton2 = tkinter.Button(root, text="login", padx=50, pady=30, command=site_login)
myButton3 = tkinter.Button(root, text="logout", padx=50, pady=30, command=site_logout)
myButton4 = tkinter.Button(root, text="close", padx=50, pady=30, command=close)


myButton.grid(row=0, column=0)
myButton2.grid(row=0, column=1)
myButton3.grid(row=0, column=2)
myButton4.grid(row=1, column=1)

tkinter.mainloop()

#site_login()
#time.sleep(10)

#site_logout()

driver.quit()
