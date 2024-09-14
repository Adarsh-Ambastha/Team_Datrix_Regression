from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Open the dynamic page
# driver.get("https://www.cars24.com/buy-used-car?f=make%3A%3D%3Amaruti&sort=bestmatch&serveWarrantyCount=true&listingSource=Homepage_Filters&storeCityId=5")

driver.get("https://www.cars24.com/buy-used-car?f=make%3A%3D%3Amaruti&sort=bestmatch&serveWarrantyCount=true&storeCityId=5732")

# Scroll down until no more content is loaded
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to the bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Wait for the page to load new content
    time.sleep(2)  # Adjust time as needed
    
    # Calculate new scroll height and compare with last height
    new_height = driver.execute_script("return document.body.scrollHeight")
    
    if new_height == last_height:
        break
    
    last_height = new_height

# Now that we've scrolled to the bottom, get the HTML of the specific class
elements = driver.find_elements(By.CLASS_NAME, "_2ujGx")
# for element in elements:
#     print(element.get_attribute('outerHTML'))

with open("output.html", "w", encoding="utf-8") as file:
    for element in elements:
        file.write(element.get_attribute('outerHTML'))
        file.write("\n\n")  # Add some space between elements

# Close the WebDriver
driver.quit()
