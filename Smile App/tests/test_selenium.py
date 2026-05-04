import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from time import sleep

# User fixure - 1
@pytest.fixture
def user1():
    return  {'username':'arslanay', 'email':'arslanay@wsu.edu', 'password':'strongpassword'}

# User fixure - 2
@pytest.fixture
def user2():
    return  {'username':'john', 'email':'john@wsu.edu', 'password':'alsostrongpassword'}

 # Post fixure - 1
@pytest.fixture
def post1():
    return {'title': 'My cat Cookie', 
            'body': 'My cat Cookie and his girlfriend Chia watch the sunset together everyday. I need to go home before sunset to let her out. Sometimes when I get home, I find Chia outside of our front window staring at Cookie at the window.' , 
            'happiness_level': "Happy"}

 # Post fixure - 2
@pytest.fixture
def post2():
    return {'title': 'Stolen book', 
            'body': 'Today, while I was browsing in a secondhand bookshop, I found a copy of a book that had been stolen from me when I was a kid. I opened it and saw, on the first page, in familiar hand writing, my own name. It had been a gift from my (now late) grandfather. Next to my name my grandfather wrote, “I hope you rediscover this book someday when you’re older, and it makes you think about the important things in life.' , 
            'happiness_level': "Really happy"}

 # Post fixure
@pytest.fixture
def post3():
    return {'title': 'People chain', 
            'body': """While hiking in Muir woods a car suddenly drove off the road into a river. Immediately three separate groups of strangers stopped and began sprinting to the scene. The first three to arrive were from different groups and immediately made a human chain to allow the first person to repel down the hill. The group pulled all four people from the black sedan. After the ordeal, there was a moment when all the strangers made eye contact and realized how special it was that without saying a word everyone raced to the scene and worked together.
                       While hiking in Muir woods a car suddenly drove off the road into a river. Immediately three separate groups of strangers stopped and began sprinting to the scene. The first three to arrive were from different groups and immediately made a human chain to allow the first person to repel down the hill. The group pulled all four people from the black sedan. After the ordeal, there was a moment when all the strangers made eye contact and realized how special it was that without saying a word everyone raced to the scene and worked together.
                       While hiking in Muir woods a car suddenly drove off the road into a river. Immediately three separate groups of strangers stopped and began sprinting to the scene. The first three to arrive were from different groups and immediately made a human chain to allow the first person to repel down the hill. The group pulled all four people from the black sedan. After the ordeal, there was a moment when all the strangers made eye contact and realized how special it was that without saying a word everyone raced to the scene and worked together.
                       While hiking in Muir woods a car suddenly drove off the road into a river. Immediately three separate groups of strangers stopped and began sprinting to the scene. The first three to arrive were from different groups and immediately made a human chain to allow the first person to repel down the hill. The group pulled all four people from the black sedan. After the ordeal, there was a moment when all the strangers made eye contact and realized how special it was that without saying a word everyone raced to the scene and worked together.
                       While hiking in Muir woods a car suddenly drove off the road into a river. Immediately three separate groups of strangers stopped and began sprinting to the scene. The first three to arrive were from different groups and immediately made a human chain to allow the first person to repel down the hill. The group pulled all four people from the black sedan. After the ordeal, there was a moment when all the strangers made eye contact and realized how special it was that without saying a word everyone raced to the scene and worked together.
                       While hiking in Muir woods a car suddenly drove off the road into a river. Immediately three separate groups of strangers stopped and began sprinting to the scene. The first three to arrive were from different groups and immediately made a human chain to allow the first person to repel down the hill. The group pulled all four people from the black sedan. After the ordeal, there was a moment when all the strangers made eye contact and realized how special it was that without saying a word everyone raced to the scene and worked together.
                       While hiking in Muir woods a car suddenly drove off the road into a river. Immediately three separate groups of strangers stopped and began sprinting to the scene. The first three to arrive were from different groups and immediately made a human chain to allow the first person to repel down the hill. The group pulled all four people from the black sedan. After the ordeal, there was a moment when all the strangers made eye contact and realized how special it was that without saying a word everyone raced to the scene and worked together.
                       While hiking in Muir woods a car suddenly drove off the road into a river. Immediately three separate groups of strangers stopped and began sprinting to the scene. The first three to arrive were from different groups and immediately made a human chain to allow the first person to repel down the hill. The group pulled all four people from the black sedan. After the ordeal, there was a moment when all the strangers made eye contact and realized how special it was that without saying a word everyone raced to the scene and worked together.
                       While hiking in Muir woods a car suddenly drove off the road into a river. Immediately three separate groups of strangers stopped and began sprinting to the scene. The first three to arrive were from different groups and immediately made a human chain to allow the first person to repel down the hill. The group pulled all four people from the black sedan. After the ordeal, there was a moment when all the strangers made eye contact and realized how special it was that without saying a word everyone raced to the scene and worked together.
                       While hiking in Muir woods a car suddenly drove off the road into a river. Immediately three separate groups of strangers stopped and began sprinting to the scene. The first three to arrive were from different groups and immediately made a human chain to allow the first person to repel down the hill. The group pulled all four people from the black sedan. After the ordeal, there was a moment when all the strangers made eye contact and realized how special it was that without saying a word everyone raced to the scene and worked together.
                       While hiking in Muir woods a car suddenly drove off the road into a river. Immediately three separate groups of strangers stopped and began sprinting to the scene. The first three to arrive were from different groups and immediately made a human chain to allow the first person to repel down the hill. The group pulled all four people from the black sedan. After the ordeal, there was a moment when all the strangers made eye contact and realized how special it was that without saying a word everyone raced to the scene and worked together.
                       While hiking in Muir woods a car suddenly drove off the road into a river. Immediately three separate groups of strangers stopped and began sprinting to the scene. The first three to arrive were from different groups and immediately made a human chain to allow the first person to repel down the hill. The group pulled all four people from the black sedan. After the ordeal, there was a moment when all the strangers made eye contact and realized how special it was that without saying a word everyone raced to the scene and worked together.""" , 
            'happiness_level': 'I can\'t stop smiling'}


"""
Download the chrome driver and make sure you have chromedriver executable in your PATH variable. 
To download the ChromeDriver to your system navigate to its download page. 
https://chromedriver.chromium.org/downloads  
"""

@pytest.fixture
def browser():
    CHROME_PATH = "C:\\Webdriver\\chromedriver-win64"
    print(CHROME_PATH)

    service = Service(executable_path = CHROME_PATH + '\\chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(8)
    
    yield driver

    # For cleanup, quit the driver
    driver.quit()


def test_register_form(browser,user2):

    browser.get('http://localhost:5000/user/register')
    # Enable this to maximize the window
    # browser.maximize_window()
    browser.find_element(By.NAME, "username").send_keys(user2['username'])
    sleep(2)
    browser.find_element(By.NAME, "email").send_keys(user2['email'])
    sleep(2)
    browser.find_element(By.NAME, "password").send_keys(user2['password'])
    sleep(2)
    browser.find_element(By.NAME, "password2").send_keys(user2['password'])    
    sleep(2)
    browser.find_element(By.NAME, "submit").click()
    sleep(2)
    #verification
    content = browser.page_source
    # print(content)
    assert 'Congratulations, you are now a registered user!' in content

def test_register_error(browser,user2):
    browser.get('http://localhost:5000/user/register')
    browser.find_element(By.NAME, "username").send_keys(user2['username'])
    sleep(2)
    browser.find_element(By.NAME, "email").send_keys(user2['email'])
    sleep(2)
    browser.find_element(By.NAME, "password").send_keys(user2['password'])
    sleep(2)
    browser.find_element(By.NAME, "password2").send_keys(user2['password'])    
    sleep(2)
    browser.find_element(By.NAME, "submit").click()
    sleep(2)
    #verification
    content = browser.page_source
    assert 'Register' in content
    assert '[Please use a different username.]' in content

def test_login_form(browser,user2):
    browser.get('http://localhost:5000/user/login')
    browser.find_element(By.NAME, "username").send_keys(user2['username'])
    sleep(2)
    browser.find_element(By.NAME, "password").send_keys(user2['password'])
    sleep(2)
    browser.find_element(By.NAME, "remember_me").click()
    sleep(2)
    button = browser.find_element(By.NAME, "submit").click()
    sleep(2)
    #verification
    content = browser.page_source
    assert 'Welcome to Smile Portal!' in content
    assert user2['username'] in content

def test_invalidlogin(browser,user2):
    browser.get('http://localhost:5000/user/login')
    browser.find_element(By.NAME, "username").send_keys(user2['username'])
    sleep(2)
    browser.find_element(By.NAME, "password").send_keys('wrongpassword')
    sleep(2)
    browser.find_element(By.NAME, "remember_me").click()
    sleep(2)
    browser.find_element(By.NAME, "submit").click()
    sleep(2)
    #verification
    content = browser.page_source
    assert 'Invalid username or password' in content
    assert 'Sign In' in content

def test_post_smile(browser,user2,post1):
    #first login
    browser.get('http://localhost:5000/user/login')
    browser.find_element(By.NAME, "username").send_keys(user2['username'])
    browser.find_element(By.NAME, "password").send_keys(user2['password'])
    browser.find_element(By.NAME, "remember_me").click()
    browser.find_element(By.NAME, "submit").click()

    browser.get('http://localhost:5000/post')
    browser.find_element(By.NAME, "title").send_keys(post1['title'])
    sleep(2)
    browser.find_element(By.NAME, "body").send_keys(post1['body'])
    sleep(2)
    Select(browser.find_element(By.NAME, "happiness_level")).select_by_visible_text(post1['happiness_level'])
    sleep(2)
    tags = browser.find_element(By.NAME, "tag").click()
    sleep(2)
    browser.find_element(By.NAME, "submit").click()
    sleep(2)
    #verification
    content = browser.page_source
    assert post1['title'] in content
    assert post1['body'] in content

def post_smile2(browser,user2,post2):
    #first login
    browser.get('http://localhost:5000/user/login')
    browser.find_element(By.NAME, "username").send_keys(user2['username'])
    browser.find_element(By.NAME, "password").send_keys(user2['password'])
    browser.find_element(By.NAME, "remember_me").click()
    browser.find_element(By.NAME, "submit").click()

    browser.get('http://localhost:5000/post')
    browser.find_element(By.NAME, "title").send_keys(post2['title'])
    sleep(2)
    browser.find_element(By.NAME, "body").send_keys(post2['body'])
    sleep(2)
    Select(browser.find_element(By.NAME, "happiness_level")).select_by_visible_text(post2['happiness_level'])
    sleep(2)
    tags = browser.find_element(By.NAME, "tag").click()
    sleep(2)
    browser.find_element(By.NAME, "submit").click()
    sleep(2)
    #verification
    content = browser.page_source
    assert post2['title'] in content
    assert post2['body'] in content

def test_post_smile_error(browser,user2,post3):
    #first login
    browser.get('http://localhost:5000/user/login')
    browser.find_element(By.NAME, "username").send_keys(user2['username'])
    browser.find_element(By.NAME, "password").send_keys(user2['password'])
    browser.find_element(By.NAME, "remember_me").click()
    browser.find_element(By.NAME, "submit").click()

    browser.get('http://localhost:5000/post')
    browser.find_element(By.NAME, "title").send_keys(post3['title'])
    sleep(2)
    browser.find_element(By.NAME, "body").send_keys(post3['body'])
    sleep(2)
    Select(browser.find_element(By.NAME, "happiness_level")).select_by_visible_text(post3['happiness_level'])
    sleep(2)
    tags = browser.find_element(By.NAME, "tag").click()
    sleep(2)
    browser.find_element(By.NAME, "submit").click()
    sleep(10)
    #verification
    content = browser.page_source
    assert "Field must be between 1 and 1500 characters long." in content


if __name__ == "__main__":
    retcode = pytest.main(verbose=2)