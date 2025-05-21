import requests
from bs4 import BeautifulSoup
import pandas as pd 

url = 'http://books.toscrape.com/catalogue/page-1.html'

response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

titles = []
prices = []

books = soup.find_all('article',class_='product_pod')

for book in books:
    titles = libro.h3.a['title']
    prices = libro.find('p', class_='price_color').text
    titles.append(titles)
    prices.append(prices)
  
df= pd.DataFrame({'Title': titles, 'price': prices})
df.to_excel('libri_estratti.xlsx' , index=False)    
print ("dati salvati in 'libri_estratti.xlsx'")
