from bs4 import BeautifulSoup
import requests, openpyxl

try:
    response= requests.get("https://www.swansea.gov.uk/primaryschools?lang=en")
    soup=BeautifulSoup(response.text,'html.parser')
    
    schools=soup.find('div', class_="grid grid--list grid--2col").find_all('div', class_="item item--article")

    for school in schools:
        #print(school)
        school_name=school.find('dl',class_="contact contact--listitem").dd.text
        job_title=school.find('dd',class_="contact__value contact__value--job").text
        school_email=school.find('dd',class_="contact__value contact__value--email").a.text
        telephone_no=school.find('dd',class_="contact__value contact__value--tel").a.text
        print("School name = ",school_name)
        print("Job title =",job_title)
        print("Email ID = ",school_email)
        print("Telephone No = ",telephone_no)

except Exception as e:
    print(e)





