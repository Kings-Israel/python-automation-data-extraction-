from bs4 import BeautifulSoup
import requests
import sys
import pandas as pd

url = "http://www.katti.co.ke/index.php/katti-institutions/registered-institutions"
schoolsNo = 0
npo_schools = {}

response = requests.get(url)
if response:
    print("Responded")
else:
    print("No response")
    sys.exit()

data = response.text

soup = BeautifulSoup(data, 'html.parser')

schools = soup.find_all("tr")

for school in schools:
    names = school.find("td", {"style": "width: 155.114px;"})
    schoolName = names.find("p").text
    address = school.find("td", {"style": "width: 122.386px;"}).text.strip()
    address = address.replace("\n", " ")
    location = school.find("td", {"style": "width: 88.75px;"}).text.strip()
    print(schoolName, '\n', address)
    print("\n")
    schoolsNo+=1
    npo_schools[schoolsNo] = [schoolName, address, location]
    
npo_schools_df = pd.DataFrame.from_dict(npo_schools, orient = 'index', columns = ['Institution', 'Address', 'Location'])
npo_schools_df.head()
npo_schools_df.to_csv('Schools.csv')