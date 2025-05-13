import requests
from bs4 import BeautifulSoup
import csv

# URL alvo
url ='https://books.toscrape.com/'

resposta = requests.get (url) 
resposta.encoding = 'UTF-8'

print(resposta.status_code)

soup = BeautifulSoup(resposta.text, 'html.parser')
livros = soup.find_all('article', class_='product_pod')

with open('relatorio.csv', 'w', newline='', encoding='UTF-8') as csv_file:
    escritor = csv.writer(csv_file)
    escritor.writerow(['titulo,preco,link'])

        
    for  livros in livros:
        titulo = livros.h3.a['title']
        link = livros.h3.a['href']
        preco = livros.find('p', class_='price_color').text
        print('----T----')
        print(titulo)
        print(url+link)
        print(preco)
        escritor.writerow([titulo,preco,url+link])

