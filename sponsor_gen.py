'''sponsor_gen.py 
 - gets sponsor list from https://hopin.com/events/vghc-21
 - generates sponsors' mission statement, vision statement, and values 
'''

from bs4 import BeautifulSoup as bs
import requests
import csv

url = 'https://hopin.com/events/vghc-21'
res = requests.get(url)
soup = bs(res.text,'html.parser')
companies= soup.find_all("div",class_="card-content")

sponsor_list =[]
for company in companies:
    for name in company.find("h3"): # change bs4.tag to string
        sponsor_list.append(str(name))

# # write to sponsor_file
# filename = "sponsor.csv"

# with open(filename, 'w') as f:
#     f = csv.writer(f)
#     for sponsor in sponsor_list:
#         f.writerow([sponsor])

# gen mission statements
for sponsor in sponsor_list[1:2]:
    url = f'https://www.comparably.com/companies/{sponsor.lower().replace(" ","-")}/mission'
    print(url)
    res = requests.get(url)
    print(res.status_code)
    # soup = bs(res.text,'html.parser')
    # container = soup.find_all("div",class_="organization_details")
    # print(soup)

