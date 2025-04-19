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
service = Service("C:/Users/peter/Desktop/Spatial/Exam/edgedriver_arm64/msedgedriver.exe")

# Set Edge options and specify a unique user data directory
options = Options()
options.add_argument("user-data-dir=C:/Users/peter/Desktop/Spatial/Exam/EdgeProfile")  # Replace with any unique path

# Initialize Edge WebDriver with the service
driver = webdriver.Edge(service=service, options=options)
driver.get("https://www.google.com/maps")

# Search for locations
search_word = 'Rema 1000 8000 Aarhus'

search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@role="combobox" and @id="searchboxinput"]'))
)
search_box.send_keys(search_word)
search_box.send_keys(Keys.RETURN)

time.sleep(10)

# Get links for multiple search results
result_links = driver.find_elements(By.CLASS_NAME, "hfpxzc")
hrefs = [link.get_attribute("href") for link in result_links]

addresses = []
place_names = []

for href in hrefs:
    driver.get(href)
    # Wait for the page to load
    place_name_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'DUwDvf'))
    )
    address_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "Io6YTe"))  # Adjust if needed
    )
    place_names.append(place_name_element.text)
    addresses.append(address_element.text)

# Print extracted place names and addresses to ensure nothing is missing
print(place_names)
print(addresses)


## Little code snippet for search with 1 result ##

# Collect addresses (adjust selectors for your specific use case)
#address_elements = driver.find_elements(By.XPATH, '//div[contains(@class, "Io6YTe") and contains(., "8000")]') # change for the specific instance
#addresses = [result.text for result in address_elements]


driver.quit()

## Only run this once to create a CSV file ##

#csv_file = "C:/Users/peter/Desktop/Spatial/Exam/Data/places_and_addresses.csv"
#with open(csv_file, mode="w", newline="", encoding="WINDOWS-1252") as file:
#    writer = csv.writer(file)
#
#    # Write headers
#    writer.writerow(["search_word", "place_name", "address"])
#
#    # Write data
#    for place_name, address in zip(place_names, addresses):
#        writer.writerow([search_word, place_name, address])

## Now run this to append new searches to the existing CSV file ##

csv_file = "C:/Users/peter/Desktop/Spatial/Exam/Data/places_and_addresses.csv"
with open(csv_file, mode="a", newline="", encoding="WINDOWS-1252") as file:  # Use "a" mode for appending
    writer = csv.writer(file)

    # Append data
    for place_name, address in zip(place_names, addresses):
        writer.writerow([search_word, place_name, address])