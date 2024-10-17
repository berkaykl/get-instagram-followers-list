from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
browser.set_window_size(1440,900)

url = "https://www.instagram.com"
browser.get(url)


time.sleep(2)

#giriş yapma
username = browser.find_element(By.NAME, 'username')
password = browser.find_element(By.NAME, 'password')
username.send_keys("") #enter your username
password.send_keys("") #enter your password

loginButton = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
loginButton.click()

time.sleep(6)
privProfileButton = browser.find_element(By.CLASS_NAME, 'x9f619')
privProfileButton.click()

time.sleep(1)

simdi_degil = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
simdi_degil.click()

time.sleep(1)

privProfileButton2 = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[2]/div/div[1]/div/div/div/div/div/div[2]/div/div/div/a')
privProfileButton2.click()

time.sleep(2)

#bio profile button
bioProfileButton = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/h1/a')
bioProfileButton.click()

time.sleep(1)

#main profile follow button
mainProfileFollowing = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]')
mainProfileFollowing.click()


time.sleep(3)

jsCodes = """
let followers = document.querySelector("._aano");
let interval = setInterval(function() {
    followers.scrollTo(0, followers.scrollHeight);
    console.log(followers.scrollHeight)
}, 100);
setTimeout(() => {
    clearInterval(interval)
}, 22000);
"""
browser.execute_script(jsCodes)

time.sleep(23)

followersList = []
followersNames = browser.find_elements(By.CSS_SELECTOR, 'span._ap3a._aaco._aacw._aacx._aad7._aade')

for follower in followersNames:
    followersList.append(follower.text)
    print(follower.text)


time.sleep(2)
with open("following.txt", "w", encoding="utf-8") as following:

    for i in followersList:
        following.write(i + "\n")

time.sleep(15)