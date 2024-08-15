from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import html
import pandas as pd
import re

query = input("Search for...")

print(f"Searching for {query}")
# Initialize the WebDriver
driver = webdriver.Chrome()
driver.get(f"https://www.flipkart.com/search?q={query}")

# getting the number of pages
pages = driver.find_element(By.CLASS_NAME,"_1G0WLw")
pages = pages.text
pages = pages.split(" ")
pages = pages[3]
pages.split('\n')
pages = f'{pages[0]}{pages[1]}'
pages = int(pages)+1


print(f"Total pages: {pages}")

for page in range(pages):
    driver.get(f"https://www.flipkart.com/search?q={query}&page={page+1}")
    elems = driver.find_elements(By.CLASS_NAME, "CGtC98")
    if(len(elems) == 0):
        print("No more results!.")
        break;
    print(f'Total results on page {page+1}: {len(elems)}')
    
    for elem in elems:
        with open(f"data/{query}.html", "a", encoding="utf-8") as f:
            f.write(elem.get_attribute("outerHTML"))
            f.write("\n")

driver.quit()

print("Reading file...")
with open(f'data/{query}.html', encoding='utf-8') as f:
    html_doc = f.read()

print("Prettifying...")
soup = BeautifulSoup(html_doc, 'html.parser')

print("Writing back...")
with open(f'data/{query}.html', "w", encoding="utf-8") as f:
    f.write(soup.prettify())

print("Starting the analysis...")
t = soup.find_all('div', attrs={'class': 'KzDlHZ'})
p = soup.find_all('div', attrs={'class': 'Nx9bqj _4b5DiR'})
l = soup.find_all('a')

d = {'title': [],'price':[],'link':[]}
print("adding all to dataframe...")
for price in p:
    price = price.get_text()
    price = price.strip()
    price = re.sub(r'[^\d,]', '', price)
    d['price'].append(price)
    
for title in t:
    title = title.get_text()
    title = title.strip()
    d['title'].append(title)
    
for link in l:
    link = link['href']
    d['link'].append(f'https://flipkart.com/{link}')

# Fill missing values in the dictionary
max_length = max(len(d['title']), len(d['price']), len(d['link']))
for key in d.keys():
    if len(d[key]) < max_length:
        d[key].extend([None] * (max_length - len(d[key])))

print("converting to CSV...")
df = pd.DataFrame(data=d)
df.to_csv(f'data/{query}.csv')

print("DONE!")
