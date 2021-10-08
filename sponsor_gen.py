'''sponsor_gen.py 
 - gets sponsor list from https://hopin.com/events/vghc-21
 - generates sponsors' mission statement, vision statement, and values 
'''

from bs4 import BeautifulSoup as bs
import requests
import csv
import time

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
# sponsor_list = ["bank of america", "google"]
vision_list = []
for sponsor in sponsor_list:
    url = f'https://mission-statement.com/{sponsor.lower().replace(" ","-")}'
    print(url)
    res = requests.get(url)
    soup = bs(res.content,'html.parser')
    container = soup.find("div", class_="post-single-content box mark-links")
    try:
        vision = [c.text for c in container.find_all("strong")]
        try:
            exclude = vision.index('Core\nValues')
        except:
            exclude = vision.index('Core Values')
        vision = vision[exclude+1:-1]
        vision = [v.replace('\n', ' ')for v in vision]
        vision = ", ".join(vision)
        vision_list.append(vision)
    except:
        vision_list.append("")


filename = 'core_values.csv'
with open(filename, 'w') as f:
    f = csv.writer(f)
    print(len(sponsor_list),len(vision_list))
    print(sponsor_list,vision_list)
    for spons, vis in zip(sponsor_list,vision_list):
        pair = [spons, vis]
        f.writerow(pair)