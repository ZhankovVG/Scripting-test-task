from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()


try:
    # I go to the website start
    driver.get('https://getpass.civic.com/status?chain=polygon')
    time.sleep(10)
    # I go to the website end

    # Selecting captcha start
    klick_captcha = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[@class='listbox-button-title' and text()='CAPTCHA Verification']"))
    )

    klick_captcha.click()
    time.sleep(3)

    captcha_element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@class='listbox-option' and .//span[text()='CAPTCHA Verification']]"))
    )

    captcha_element.click()
    time.sleep(3)

    # Find the button start
    klick_connect = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Connect']"))
    )

    klick_connect.click()
    time.sleep(3)

    # Metamask select start
    klick_metamask = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='iekbcc0' and text()='MetaMask']"))
    )

    klick_metamask.click()
    time.sleep(3)

    # Next_button
    next_button = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='page-container-footer-next']"))
    )
    next_button.click()
    time.sleep(3)

    # Next_button_connect
    button_connect = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-textid='page-container-footer-next' and text()'Подключиться']"))
    )

    button_connect.click()
    time.sleep(3)

    # Next_button_approve
    button_approve = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='confirmation-submit-button' and text()='Одобрить']"))
    )

    button_approve.click()
    time.sleep(3)

    # Change network
    change_network = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='confirmation-submit-button' and text()='Сменить сеть']"))
    )

    change_network.click()
    time.sleep(3)

    # Get Pass
    get_pass = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'status-button') and contains(., 'GET PASS')]"))
    )

    get_pass.click()
    time.sleep(3)



except Exception as ex:
    print(ex)    
finally:
    driver.close()
    driver.quit()