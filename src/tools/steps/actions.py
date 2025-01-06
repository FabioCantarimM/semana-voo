from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def goto(browser, url):
    return browser.get(url)

def click_button(browser, att):
    tag = att["element"]
    button = browser.find_element(By.XPATH, tag)
    return button.click()

def input(browser, att):
    element = att["element"]
    value = att["value"]
    input_field =  browser.find_element(By.XPATH, element)
    input_field.send_keys(value)

def press_button(browser, att):
    element = att["element"]
    value = att["value"]

    tag = browser.find_element(By.XPATH, element)
    if value == 'return':
        return tag.send_keys(Keys.RETURN)
    if value == 'enter':
        return tag.send_keys(Keys.ENTER)
    raise("Botao não implementado")

def wait(browser, att):
    time.sleep(att)
    return print(f'waiting for {att}')

action_dict = {}

action_dict['goto'] = goto
action_dict['input'] = input
action_dict['press_button'] = press_button
action_dict['click_button'] = click_button
action_dict['wait'] = wait