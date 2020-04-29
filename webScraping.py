import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from pprint import pprint
import random
import database
# Set URL
URL = "https://www.theguardian.com/news/datablog/2009/sep/08/baby-names-children-jack-olivia-mohammed"

# Connect Url
page = requests.get(URL)
# Check Url
# print(page)

girlNameList = []
boyNameList = []
# Parse HTML to save to BeautifulSoup object
soup = BeautifulSoup(page.content, "html.parser")



for x in range(100):
    randNum = random.randint(17, 30)
    girlTag = soup.find(id = 'table-cell-2474-'+str(x+1)+'-1').get_text("/", strip = True)
    boyTag = soup.find(id = 'table-cell-2475-'+str(x+1)+'-1').get_text("/", strip = True)
    print(girlTag + " " + str(randNum))
    database.inputDB(girlTag, randNum)
    database.inputDB(boyTag, randNum)