import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# Add your post url (if any) to your posts here for others to like them : https://docs.google.com/document/d/1YiPKlYkzGMO08HfpZuOZ-S4B-t6KrA7-Xe1x1ElFmnk/edit?usp=sharing

# step 1 change this from : https://docs.google.com/document/d/1YiPKlYkzGMO08HfpZuOZ-S4B-t6KrA7-Xe1x1ElFmnk/edit?usp=sharing
links = [
    "https://www.linkedin.com/feed/update/urn:li:activity:6785441555596492800/",
    "https://www.linkedin.com/feed/update/urn:li:activity:6794077580908744704/"
]


options = webdriver.ChromeOptions()
options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("https://linkedin.com")
# sleep(5)
# delete this after every month

try:
    # auto login in case the user is not logged in
    userid = '' # fill the userid
    password = '' # fill the password 
    checklink = driver.find_element_by_class_name("sign-in-form__form-input-container")
    driver.find_element_by_xpath('//*[@id="session_key"]').send_keys(userid)
    password = driver.find_element_by_xpath('//*[@id="session_password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/div[2]/form/button').click()
    sleep(2)
    
except Exception as e:
    print("error processing link\n" , "\nerror",  e)

for link in links:
    try:
        print("accessing link ", link)
        driver.get(link)
        sleep(2)
        el = driver.find_element_by_class_name("react-button__trigger")
        if "false" == el.get_attribute("aria-pressed"):
            print("liking")
            el.click()
            print("liked")
            sleep(1)
        else:
            print("already processed link ", link)
    except Exception as e:
        print("error processing link\nlink: ", link, "\nerror",  e)

driver.close()


