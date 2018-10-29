import requests
from bs4 import BeautifulSoup

URL="http://www.mca.gov.in/mcafoportal/showCheckCompanyName.do"
payload = {'name1':'Google','checkCompanyName_0':'Search'}
with requests.session() as s:
    s.headers={"User-Agent":"Mozilla/5.0"}
    s.post(URL,data=payload)
    res=s.get(URL,data=payload)
    soup=BeautifulSoup(res.text,"lxml")
    print(soup.prettify())
