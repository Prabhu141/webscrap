from bs4 import BeautifulSoup
import requests
from csv import writer

url= "https://www.swansea.gov.uk/welshmediumprimaryschools"
page = requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')
schools = soup.find_all('div',class_="grid__cell grid__cell--listitem grid__cell--cols1")
#print(lists)

with open('schools.csv','w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Name','Job Title','Email ID','Telephone']
    thewriter.writerow(header)

    for school in schools:
        title = school.find('dd',class_="contact__value contact__value--name").text
        job = school.find('dd',class_="contact__value contact__value--job").text
        mail = school.find('dd',class_="contact__value contact__value--email").a.text
        phone = school.find('dd',class_="contact__value contact__value--tel").a.text    

        info = [title, job,mail,phone]
        thewriter.writerow(info)