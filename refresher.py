from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, WebDriverException
import time

def buyBot(URL):
    driver = webdriver.Chrome()
    messageFlag = 0
    refreshTimer = -1
    rChoice = "y"
    aChoice = "add"
    if URL[0:8] == 'https://':
        driver.get(URL)
    else:
        URL = "https://" + URL
        driver.get(URL)
    while 1:
        try:
            driver.find_element_by_name(aChoice).click()
            print("\nItem is in cart!!!")
            break
        except ElementClickInterceptedException: #NoSuchElementException:
            if messageFlag == 0:
                print("The item is currently not in stock")
                rChoice = input("Would you like to refresh?(y/n)")
            if rChoice == "y":
                if messageFlag == 0:
                    refreshTimer = input("Enter how many seconds for each refresh: ")
                    print("The program will refresh every " + refreshTimer + " seconds")
                time.sleep(int(refreshTimer))
                driver.refresh()
                messageFlag = 1
            elif rChoice == "n":
                break
        except NoSuchElementException:
            aChoice = input("The css for adding was not found, Please enter the css for the add button: ")
        # except finally:
        #     mChoice = input("You closed the window!\n Would you like to reopen?(y/n)")
        #     if mChoice == "y":
        #         driver.get(URL)
        #     elif mChoice == "n":
        #         break
    input("\nPress Enter to return...")
