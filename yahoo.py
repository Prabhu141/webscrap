import requests
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/losers?.tsrc=fin-srch&count=100&offset=0'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

table = soup.find('table', class_ ='W(100%)')


for  yahoo in table.find_all('tbody'):
    rows = yahoo.find_all('tr')
    for row in rows:
        
        symbol = row.find('a',class_ ='Fw(600) C($linkColor)').text
        finance = row.find('td',class_ = 'Va(m) Ta(start) Px(10px) Fz(s)').text
        price = row.find('td',class_ ='Va(m) Ta(end) Pstart(20px) Fw(600) Fz(s)').text
        volume = row.find('td',class_ ='Va(m) Ta(end) Pstart(20px) Fz(s)').text
        
    
        info= [symbol, finance, price,volume]
        print(info)