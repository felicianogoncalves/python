import requests # permite enviar pedidos HTML e receber conteudo
import csv # escrita e leitura de ficheiros csv
from bs4 import BeautifulSoup # facilitar a analise de HTML extração de dados ainda não são estruturados

todas_citacoes=[]
page=1

#criar um loop para aceder às paginas sequencialmente
#criterio paragem: quando não tiver conteudo

while True:
    url=f'https://quotes.toscrape.com/page/{page}/'
    response = requests.get(url)

    if response.status_code !=200:
        break #sai do loop se não existir pagina

    soup = BeautifulSoup(response.text,'html.parser')
    quotes = soup.find_all('div',class_='quote')

    if not quotes:
        break

    for quote in quotes:
        texto=quote.find('span',class_='text').text
        autor=quote.find('small', class_='author').text
        todas_citacoes.append([texto,autor])

    print(f'\n A processar pagina {page}')

    page+=1

    #guardar dados csv
    with open('citacoes.csv','w',newline='',encoding='utf-8') as ficheiro:
        writer=csv.writer(ficheiro)
        writer.writerows(todas_citacoes)
    
