#The wikipedia webpage https://en.wikipedia.org/wiki/List_of_largest_banks provides information about largest banks in the world by various parameters. 
# Scrape the data from the table 'By market capitalization' and store it in a JSON file

from bs4 import BeautifulSoup
import html5lib
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_largest_banks"
html_data  = requests.get(url).text 

soup=BeautifulSoup(html_data,"html.parser")

#create dataframe
data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])

#append dataframe
for row in soup.find_all('tbody')[3].find_all('tr'):
    col = row.find_all('td')
    if (col != []):
        name = col[0].string 
        market_cap = col[1].string 
        data = data.append({"Name":name, "Market Cap (US$ Billion)":market_cap}, ignore_index=True)
data

#save as json file
data.to_json(r'bank_market_cap.json')