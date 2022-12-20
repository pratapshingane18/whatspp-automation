# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.keys import Keys
# import pyperclip
# import time



# s = Service("C:Users\Santosh\Downloads\chromedriver_win32")
# browser = webdriver.Chrome("service=s")

# browser.maximize_window()

# browser.get('https://web.whatsapp.com/')

# with open('groups.txt', 'r', encoding='utf8') as f:
#     groups = [group.strip() for group in f.readlines()]

# with open('message.txt', 'r', encoding='utf8') as f:
#     message = f.read()

# for group in groups:
#     #search_xpath = '//div[@contenteditable="true"][@data-tab="3"]' #refactor into seprate variable xpath

#     search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'

#     search_box = WebDriverWait(browser, 500).until(
#           EC.presence_of_element_located((By.XPATH, "search_xpath")) #it will wait until this presence of element is located
#     )

#     search_box.clear()

#     time.sleep(1)

#     pyperclip.copy(group)

#     search_box.send_keys(Keys.SHIFT, Keys.INSERT)  # Keys.CONTROL + "v"

#     time.sleep(2)

#     group_xpath = f'//span[@title="{group}"]'
#     group_title = browser.find_element_by_xpath(group_xpath)

#     group_title.click()

#     time.sleep(1)

#     input_xpath = '//div[@contenteditable="true"][@data-tab="1"]'
#     input_box = browser.find_element_by_xpath(input_xpath)

#     pyperclip.copy(msg)
#     # input_box.send_keys(Keys.SHIFT, Keys.INSERT)  # Keys.CONTROL + "v"
#     input_box.send_keys(Keys.CONTROL + "v")
#     input_box.send_keys(Keys.ENTER)

#     time.sleep(2)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyperclip

def message(to,message=''):
    d = webdriver.Chrome(r'C:\Program Files\Google\GoogleUpdater')		# directory to chromedriver
    d.get('https://web.whatsapp.com/')					# URL to open whatsapp web
    wait = WebDriverWait(driver = d, timeout = 900)			# inscrease or decrease the timeout according to your net connection

    message += '\nthis is a system generated message'			# additional text to with your message to identify that it is send via software
    
    name_argument = f'//span[contains(@title,\'{to}\')]'		# HTML parse code to identify your reciever
    title = wait.until(EC.presence_of_element_located((By.XPATH,name_argument)))
    title.click()							# to open the receiver messages page in the browser
	
	# many a times class name or other HTML properties changes so keep a track of current class name for input box by using inspect elements
    input_path = '//div[@class="pluggable-input-body copyable-text selectable-text"][@dir="auto"][@data-tab="1"]'
    box = wait.until(EC.presence_of_element_located((By.XPATH,input_path)))

    box.send_keys(message + Keys.ENTER)					# send your message followed by an Enter


# s = Service("C:\Program Files\Google\GoogleUpdater")


# driver= webdriver.Chrome("service=s")

# driver.maximize_window()
# driver.implicitly_wait(200) 

# driver.get('https://web.whatsapp.com/')

# #opening groups file reading content from it line by line
# #using list comprehension to remove \n using strip()
# with open('groups.txt', 'r', encoding='utf8') as f:
#     groups = [group.strip() for group in f.readlines()] 

# # print(groups)

# #similarly opening and reading message file
# with open('message.txt', 'r', encoding='utf8') as f:
#     message = f.read()

# # print(message)

# # Algo: Search the group in search bar Message will be delivered to the top finding in the search bar that is the same group in which we want to find message 

# for group in groups:
#     search_xpath = '//div[@contenteditable="true"][@data-tab="3"]' #refactor into seprate variable xpath

    
    
#     search_box = WebDriverWait(driver, 195).until(
#         EC.presence_of_element_located((By.XPATH, "search_xpath")) #it will wait until this presence of element is located
#     )

#     search_box.clear()

#     time.sleep(1)

#     pyperclip.copy(group)

#     search_box.send_keys(Keys.SHIFT, Keys.INSERT)  # Keys.CONTROL + "v"

#     time.sleep(2)

#     group_xpath = f'//span[@title="{group}"]'
#     group_title = browser.find_element_by_xpath(group_xpath)

#     group_title.click()

#     time.sleep(1)

#     input_xpath = '//div[@contenteditable="true"][@data-tab="1"]'
#     input_box = browser.find_element_by_xpath(input_xpath)

#     pyperclip.copy(msg)
#     # input_box.send_keys(Keys.SHIFT, Keys.INSERT)  # Keys.CONTROL + "v"
#     input_box.send_keys(Keys.CONTROL + "v")
#     input_box.send_keys(Keys.ENTER)

#     time.sleep(2)



# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

# def message(to,message=''):
# 	"""this a simple function to send a whatsapp message to your friends
# 	and group using python and selenium an automated tool to parse the HTML 
# 	content and to change the properties. 
	
# 	paramters:
# 	to - enter a name from your contacts it can be friend's name or a group's title.
# 	message - message to be deliever"""
#     d = webdriver.Chrome(r'F:/chrome driver/chromedriver.exe')		# directory to chromedriver
#     d.get('https://web.whatsapp.com/')					# URL to open whatsapp web
#     wait = WebDriverWait(driver = d, timeout = 900)			# inscrease or decrease the timeout according to your net connection

#     message += '\nthis is a system generated message'			# additional text to with your message to identify that it is send via software
    
#     name_argument = f'//span[contains(@title,\'{to}\')]'		# HTML parse code to identify your reciever
#     title = wait.until(EC.presence_of_element_located((By.XPATH,name_argument)))
#     title.click()							# to open the receiver messages page in the browser
	
# 	# many a times class name or other HTML properties changes so keep a track of current class name for input box by using inspect elements
#     input_path = '//div[@class="pluggable-input-body copyable-text selectable-text"][@dir="auto"][@data-tab="1"]'
#     box = wait.until(EC.presence_of_element_located((By.XPATH,input_path)))

#     box.send_keys(message + Keys.ENTER)					# send your message followed by an Enter