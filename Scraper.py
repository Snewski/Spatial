from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

# Define the path to the downloaded WebDriver
service = Service("C:/Users/peter/Desktop/Spatial/Exam/edgedriver_arm64/msedgedriver.exe") # Absolute path 
# Set Edge options and specify a unique user data directory
options = Options()
options.add_argument("user-data-dir=C:/Users/peter/Desktop/Spatial/Exam/EdgeProfile")  # Absolute path

# Initialize Edge WebDriver with the service and options
driver = webdriver.Edge(service=service, options=options)
driver.get("https://www.google.com/maps")

# Search for locations
search_word = "Rema 1000 8000 Aarhus"

search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@role="combobox" and @id="searchboxinput"]'))
)
search_box.send_keys(search_word)
search_box.send_keys(Keys.RETURN)

time.sleep(10)

# Get links and place names for multiple search results
result_links = driver.find_elements(By.CLASS_NAME, "hfpxzc")
hrefs = [link.get_attribute("href") for link in result_links]
place_names = [link.get_attribute("aria-label") for link in result_links]

driver.quit()

## Only run this once to create a CSV file ##

# csv_file = "C:/Users/peter/Desktop/Spatial/Exam/Data/places_and_links.csv"
# with open(csv_file, mode="w", newline="", encoding="WINDOWS-1252") as file:
#     writer = csv.writer(file)

#     # Write headers
#     writer.writerow(["search_word", "place_name", "href"])

#     # Write data
#     for place_name, href in zip(place_names, hrefs):
#         writer.writerow([search_word, place_name, href])

## Now run this to append new searches to the existing CSV file ##

csv_file = "Data/places_and_links.csv"
with open(csv_file, mode="a", newline="", encoding="WINDOWS-1252") as file:  # Use "a" mode for appending
   writer = csv.writer(file)

   # Append data
   for place_name, href in zip(place_names, hrefs):
       writer.writerow([search_word, place_name, href])