from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login():
    
    # Arrange
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10) 
    wait = WebDriverWait(driver, 10)   

    driver.get("https://front.serverest.dev/login")

    # Act
    driver.find_element(By.ID, "email").send_keys("automation@email.com")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.XPATH, "//button[@data-testid='entrar']").click()
    
    # Assert
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="navbarTogglerDemo01"]/form/button'))) # Botão de Logout
    print("Sucesso")
    driver.close()

if __name__ == "__main__":
    test_login()