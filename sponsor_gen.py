'''sponsor_gen.py 
 - gets sponsor list from https://hopin.com/events/vghc-21
 - generates sponsors' mission statement, vision statement, and values 
'''

from bs4 import BeautifulSoup as bs
import requests
import csv

# url = 'https://hopin.com/events/vghc-21'
# res = requests.get(url)
# soup = bs(res.text,'html.parser')
# companies= soup.find_all("div",class_="card-content")

# sponsor_list =[]
# for company in companies:
#     for name in company.find("h3"): # change bs4.tag to string
#         sponsor_list.append(str(name))

# # write to sponsor_file
# filename = "sponsor.csv"

# with open(filename, 'w') as f:
#     f = csv.writer(f)
#     for sponsor in sponsor_list:
#         f.writerow([sponsor])

# gen mission statements

# for sponsor in sponsor_list[1:2]:
sponsor = 'bank of america'
url = f'https://mission-statement.com/{sponsor.lower().replace(" ","-")}'
print(url)
res = requests.get(url)
soup = bs(res.content,'html.parser')
container = soup.find("div", class_="post-single-content box mark-links")
vision = [c.text for c in container.find_all("strong")]
exclude = vision.index('Core\nValues')
vision = vision[exclude+1:-1]
vision = [v.replace('\n', ' ')[:-2] for v in vision]
vision = ", ".join(vision)
print(vision)

filename = 'core_values.csv'
with open(filename, 'w') as f:
    f = csv.writer(f)
    pair = [sponsor, vision]
    f.writerow(pair)