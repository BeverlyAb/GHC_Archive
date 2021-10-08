'''sponsor_gen.py 
 gets sponsor list from https://hopin.com/events/vghc-21
'''

from bs4 import BeautifulSoup as bs
import re as re
import requests
import csv

url = 'https://hopin.com/events/vghc-21'
res = requests.get(url)
soup = bs(res.text,'html.parser')
companies= soup.find_all("div",class_="card-content")
sponsor_list =[]

for company in companies:
    for name in company.find("h3"): # change bs4.tag to string
        sponsor_list.append(name)


# write to sponsor_file
filename = "sponsor.csv"

with open(filename, 'w') as f:
    f = csv.writer(f)
    for sponsor in sponsor_list:
        f.writerow([sponsor])