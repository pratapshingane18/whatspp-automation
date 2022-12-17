from selenium import webdriver

# browser = webdriver.Chrome(
#     executable_path='C:Users\Santosh\Downloads\chromedriver_win32'
# )

# browser.maximize_window() 

# browser.get('https://web.whatsapp.com/')

#opening groups file reading content from it line by line
#using list comprehension to remove \n using strip()
with open('groups.txt', 'r', encoding='utf8') as f:
    groups = [group.strip() for group in f.readlines()] 

# print(groups)

#similarly opening and reading message file
with open('message.txt', 'r', encoding='utf8') as f:
    message = f.read()

print(message)