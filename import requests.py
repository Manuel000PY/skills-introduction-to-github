import requests
from bs4 import BeautifulSoup
import pandas as pd 

url = 'http://books.toscrape.com/catalogue/page-1.html'

response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

titoli = []
prezzi = []

libri = soup.find_all('article',class_='product_pod')

for libro in libri:
    titolo = libro.h3.a['title']
    prezzo = libro.find('p', class_='price_color').text
    titoli.append(titolo)
    prezzi.append(prezzo)
  
df= pd.DataFrame({'Titolo': titoli, 'prezzo': prezzi})
df.to_excel('libri_estratti.xlsx' , index=False)    
print ("dati salvati in 'libri_estratti.xlsx'")