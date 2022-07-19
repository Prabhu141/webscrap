from bs4 import BeautifulSoup
import requests
from csv import writer

url= "https://www.swansea.gov.uk/secondaryschools?p=1"
page = requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')
lists = soup.find_all('div',class_="grid__cell grid__cell--listitem grid__cell--cols1")
#print(lists)

with open('housing.csv','w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Name','Job Title','Email ID','Telephone']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('dd',class_="contact__value contact__value--name").text
        job = list.find('dd',class_="contact__value contact__value--job").text
        mail = list.find('dd',class_="contact__value contact__value--email").a.text
        phone = list.find('dd',class_="contact__value contact__value--tel").a.text    

        info = [title, job,mail,phone]
        thewriter.writerow(info)
        