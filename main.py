import sys
import time
from selenium import webdriver

browser = webdriver.Safari()

def createProj():
    folder_name = str(sys.argv[1])
    browser.get("https://github.com/login")
    
    login_button = browser.find_element_by_xpath("//*[@id='login_field']")
    login_button.click()
    login_button.send_keys("helloworld@gmail.com") # Replace with your email

    pass_button = browser.find_element_by_xpath("//*[@id='password']")
    pass_button.click()
    pass_button.send_keys("HelloWorld") # Replace with your password

    submit_button = browser.find_element_by_xpath("//*[@id='login']/form/div[4]/input[9]")
    submit_button.click()

    time.sleep(1)
    browser.get("https://github.com/new")
    
    time.sleep(1)
    repo_name = browser.find_element_by_xpath("//*[@id='repository_name']")
    repo_name.click()
    repo_name.send_keys(folder_name)

    create_button = browser.find_element_by_xpath("//*[@id='new_repository']/div[3]/button")
    create_button.click()

    browser.close()

if __name__ == "__main__":
    createProj()

