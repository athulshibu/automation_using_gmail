from selenium import webdriver
from time import sleep
from pyautogui import press

vidname = input("Enter Search Query: ")

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.youtube.com/")
searchbar = driver.find_element_by_name("search_query")
searchbar.send_keys(vidname)
press("enter")
sleep(5)
video = driver.find_element_by_id('video-title')
video.click()

