from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

#extra 1 minute for safety
#time.sleep(60)

driver.set_page_load_timeout(30)
#Establish Waiting Strategy
driver.implicitly_wait(1)

def vote(username):

    # Take action on browser
    driver.get("https://maplekey.net/?page=vote")

    #Find an element
    elem = driver.find_element(By.XPATH, '//input[@name="name"]')
    elem.send_keys(username)
    button = driver.find_element(By.XPATH, '//input[@name="doVote"]')
    button.click()

    WebDriverWait(driver, 60).until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='copyright col-12']"),'GTOP100'))
    print("Finished voting for: " + username)

failed_usernames = set()

# Vote Skys
for i in range(1,20):
    username = "Sky" + str(i)
    try:
        vote(username)
    except:
        failed_usernames.add(username)
 
# Vote Opsdezs (F*ck resuable code =) )
for i in range(0,16):
    if i == 0:
        username = "opsidezi"
    else:
        username = "opsidezi"+str(i)
    try:
        vote(username)
    except:
        failed_usernames.add(username)

# Vote Yahavs
for i in range(0,16):
    username = "Yahav" + str(i)
    try:
        vote(username)
    except:
        failed_usernames.add(username)

# Failed users re-tries
# for username in failed_usernames:
#     try:
#         vote(username)
#     except:
#         pass

#end driver session
driver.quit()
