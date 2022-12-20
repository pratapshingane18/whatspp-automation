#importing Libaries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pyautogui
import time

#whatsapp web link
Link = "https://web.whatsapp.com/"

#need not login again to Whatsapp web
chrome_options = Options()
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)


chrome_options.add_argument('--user-data-dir=./User_Data')

#path of chrome driver
# browser = webdriver.Chrome("E:\growupp\chromedriver.exe")
browser = webdriver.Chrome(executable_path=r"E:\growupp\chromedriver.exe") # to open the chromebrowser 

#open link
browser.get(Link)

#wait until browser load
time.sleep(200)

#function to send message 

#importing group names
names = []
with open('groups.txt') as namesfile:
    for name in namesfile:
        names.append(names.rstrip())

#to visit search bar
pyautogui.press(['tab','tab','tab','tab','tab'])

def send_message(name):
    time.sleep(2) #if something is there in the search box
    #target search bar
    search_bar = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]')
    search_bar.click()
    #if something is already written in it then remove using JS
    browser.execute_script('''
    document.querySelector("#side > div.uwk68 > div > div > div._16C8p > div > div._13NKt.copyable-text.selectable-text").innerText = '';
    ''')
    #search name by writing it 
    pyautogui.write(name)
    time.sleep(2)

    #to click on selected name
    user = browser.find_element_by_xpath(
        '//span[@title = "{}"]'.format(name)
    )
    user.click()

    #click on write message section
    msg_box = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    msg_box.click()

    pyautogui.write('hey, everyone how are you all doing ')

    #click on send
    button = browser.find_element_by_xpath('//span[@data-icon="send"]')
    button.click()


for name in names:
    send_message(name)





