from selenium import webdriver
import time
import pyautogui

epiname = input("Enter Episode Name: ")
epinum = input("Enter Episode Number: ")
epinum = "Episode " + epinum


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://animepahe.com/")
searchbar = driver.find_element_by_name("q")
searchbar.send_keys(epiname)
time.sleep(2)
pyautogui.press('down')
time.sleep(2)
pyautogui.press('enter')
time.sleep(7)
episode = driver.find_element_by_link_text("Watch Detective Conan - 917 Online")
episode.click()
episodeno = driver.find_element_by_id("episodeMenu")
episodeno.click()
episode = driver.find_element_by_link_text(epinum)
episode.click()
provider = driver.find_element_by_id("providerMenu")
provider.click()
provider = driver.find_element_by_xpath("//button[@data-provider='mp4upload']")
provider.click()
episodedets = driver.find_elements_by_xpath("//button[@data-resolution='720p']")
episodedets.click()

