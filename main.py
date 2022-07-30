import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys

# Use your own email and password of twitter here
EMAIl = "..."
PASS = "..."

DRIVER_PATH = "C://Selenium/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://speedtest.net/")
go = driver.find_element(By.CLASS_NAME, "start-text")
go.click()
time.sleep(50)
download_speed = driver.find_element(By.CSS_SELECTOR,
                                     '#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-center > div > div.result-data.u-align-left > span').text
upload_speed = driver.find_element(By.CSS_SELECTOR,
                                   '#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-left > div > div.result-data.u-align-left > span').text
print(download_speed)
print(upload_speed)
driver.get("https://twitter.com/i/flow/login")
time.sleep(15)
email_form = driver.find_element(By.XPATH,
                                 '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')

email_form.send_keys(EMAIl)
email_form.send_keys(Keys.ENTER)
time.sleep(2)
try:
    phone_username = driver.find_element(By.XPATH,
                                         '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')

except selenium.common.exceptions.NoSuchElementException:
    pass
else:
    phone_username.send_keys("@SafaAsgar")
    phone_username.send_keys(Keys.ENTER)
finally:
    time.sleep(2)
    pass_form = driver.find_element(By.XPATH,
                                    '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    pass_form.send_keys(PASS)
    pass_form.send_keys(Keys.ENTER)
time.sleep(10)
driver.get("https://twitter.com/compose/tweet")
time.sleep(5)
tweet_box = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div')
tweet_box.send_keys(
    f"This is bot Tweet. My current Download Speed is {download_speed}Mbps & Upload Speed is {upload_speed}Mbps")
time.sleep(3)
tweet_button = driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span')
tweet_button.click()
