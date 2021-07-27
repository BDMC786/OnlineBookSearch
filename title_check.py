#Import dependencies 
import pandas as pd
from selenium import webdriver
from time import sleep

#import csv
titles_df = pd.read_csv("Gale_List_clean.csv")

#Set up chromedriver
driver = webdriver.Chrome("F:/chromedriver.exe")

#Navigate to Library Catalogue
driver.get("https://montclair.on.worldcat.org/search")

#Do a dummy search to log in 
searchBar = driver.find_element_by_class_name('searchTermValue')
searchBar.send_keys("847526825")
button_1 = driver.find_element_by_id("headersubmit")
button_1.click()
sleep(20) 

#search the titles in WorldCat Discovery
for titles in titles_df["oclc_number"]:
    print("_________________________________")
    print(titles)
    driver.get("https://montclair.on.worldcat.org/search")
    searchBar = driver.find_element_by_class_name('searchTermValue')
    searchBar.send_keys(titles)
    button_1 = driver.find_element_by_id("headersubmit")
    button_1.click()
    sleep(15)

print("FINISHED")
driver.close()  