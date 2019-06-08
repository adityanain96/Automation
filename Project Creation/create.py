import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


def main():
    
    github()    

def github():    
    driver = webdriver.Chrome('C:\Scripts\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.maximize_window()
    
    driver.get('https://github.com/login')

    username_field = driver.find_element_by_name("login")
    username_field.send_keys('adityanain96')

    password_field = driver.find_element_by_name("password")
    password_field.send_keys('Cod.11136')

    password_field.submit()   

    driver.get('https://github.com/new')

    repo_field = driver.find_element_by_name('repository[name]')
    repo_field.send_keys(sys.argv[1])    
    try:
        repository_exist_or_not = driver.find_element_by_css_selector(".form-control.js-repo-name.js-repo-name-auto-check.short.is-autocheck-successful")
        repo_field.submit()
        driver.get(f"https://github.com/adityanain96/{sys.argv[1]}")
        driver.quit()
        with open('success.txt','w') as file:
            file.write('success')
        print(file)
    except NoSuchElementException:
        driver.quit()
        print(" ")
        
        
    

    

if __name__ == "__main__":
    main()
