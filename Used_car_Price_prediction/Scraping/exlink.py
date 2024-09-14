from bs4 import BeautifulSoup
import pandas as pd

# Load your HTML content (from the file you saved earlier)
with open('output.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <a> tags that are direct children of the specified class
links = []
for element in soup.select('._2ujGx > a'):  
    href = element.get('href')
    if href:
        links.append(href)

# Create a DataFrame using Pandas
df = pd.DataFrame(links, columns=['Link'])

# Save the DataFrame to a CSV file
df.to_csv('extracted_links.csv', index=False)

print("Links have been extracted and saved to extracted_links.csv")
