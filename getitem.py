from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep, time
from random import choice

def getitem(name):
    ts = time()
    opts = Options()
    opts.add_argument("--headless")
    driver = Chrome(options=opts)

    driver.get("https://www.bing.com/")

    WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, r"/html/body/div[3]/div[2]/div[2]/form/input[1]")))
    search = driver.find_element_by_xpath(r"/html/body/div[3]/div[2]/div[2]/form/input[1]")
    search.send_keys(name+" meme")
    search.submit()

    WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, r"/html/body/header/nav/ul/li[2]/a")))
    driver.find_element_by_xpath(r"/html/body/header/nav/ul/li[2]/a").click()
    sleep(2)
    
    h = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        nh = driver.execute_script("return document.body.scrollHeight")
        if nh == h:
            break
        h = nh
    WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, r"/html/body/div[3]/div[5]/div[3]/div[1]/ul[1]/li[1]/div/div/a/div/img")))
    content = driver.find_elements_by_class_name("mimg")
    image = choice(content).get_attribute("src")
    driver.close()
    return [image, str(time()-ts)+" s"]
