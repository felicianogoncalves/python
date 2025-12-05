import requests # permite enviar pedidos HTML e receber conteudo
import csv # escrita e leitura de ficheiros csv
from bs4 import BeautifulSoup # facilitar a analise de HTML extração de dados ainda não são estruturados

# #Pedido envia uma requesição à pagina web  e retorna um objeto para a variavel do =
# # Este obj response contem o conteudo de toda a pagina
# response = requests.get('https://quotes.toscrape.com/')

# #Extração do conteudo HTML como um string
# html=response.text

# # Criar o obj beautifulsoup
# # Converter um html estruturado que o python consegue percorrer facilmente
# soup=BeautifulSoup(html,'html.parser')

# # criar um lista vazia para guardar as citações
# quotes=[]

# #encontrar todas as tags <spam class = "text">

# for citacao in soup.find_all('span',class_="text"):
#     quotes.append(citacao.text)

# #mostrar as citações no ecra
# for q in quotes:
#     print(q)

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
    quotes = soup.find_all('span',class_='text')

    if not quotes:
        break # sai do loop se não houver mais citações

    for quote in quotes:
        todas_citacoes.append(quote.text)
    print(f'A processar a pagina {page}')

    for q in todas_citacoes:
        print(q)

    page += 1
