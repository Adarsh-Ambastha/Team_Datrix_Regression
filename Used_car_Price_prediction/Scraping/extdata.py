from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import csv
import re

# Read the URLs from the CSV file
input_file = 'extracted_links.csv'
df = pd.read_csv(input_file)

# Assuming the URLs are in a column named 'URL'
urls = df['Link'].tolist()

# ls = ["https://www.cars24.com/buy-used-maruti-eeco-2022-cars-gurgaon-11053739739/","https://www.cars24.com/buy-used-maruti-xl6-2019-cars-gurgaon-11019931789/"]

# File where you want to add the data
output_file = 'output.csv'

for link in urls:
        
    # Set up the WebDriver (e.g., Chrome)
    driver = webdriver.Chrome()

    # Open the dynamic page
    # driver.get("https://www.cars24.com/buy-used-maruti-eeco-2022-cars-gurgaon-11053739739/")
    # driver.get("https://www.cars24.com/buy-used-maruti-xl6-2019-cars-gurgaon-11019931789/")
    driver.get(link)


    # Get the total height of the page
    total_height = driver.execute_script("return document.body.scrollHeight")

    # Calculate the halfway point
    half_height = total_height / 2.5

    # Scroll to half the page
    driver.execute_script(f"window.scrollTo(0, {half_height});")

    time.sleep(3)

    texts = []
    nhMiJ_elements = driver.execute_script("return document.getElementsByClassName('nhMiJ');")

    class_3gHeV_elements = driver.find_elements(By.CLASS_NAME, "_3gHeV")
    car_name = driver.find_element(By.CLASS_NAME,"_2Ximl")
    car_price = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div/strong")
    texts.append(car_name.text)
    texts.append(car_price.text)
    

    

    # Extract text from _3gHeV elements
    for elem in class_3gHeV_elements:
        texts.append(elem.text)
    

    for elem in nhMiJ_elements:
        texts.append(elem.text)

    for txt in texts:
        print(txt)

    # Close the WebDriver
    driver.quit()

    

    # Write the data to a single row in the CSV file
    with open(output_file, mode='a', newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(texts)
    # Convert the data to a DataFrame
    # df = pd.DataFrame(texts)

    # Save the DataFrame to a CSV file
    # df.to_csv('extracted_texts.csv', index=False)

    # print("Text data from classes nhMiJ and _3gHeV has been extracted and saved to extracted_texts.csv")


