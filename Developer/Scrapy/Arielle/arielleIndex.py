import requests
from bs4 import BeautifulSoup
from arielleProd import raspagens
import json

url = 'http://www.arielle.com.br/produtos/listar?infinite=true'

lista_url_produto = []
lis_ta = []

arq_json = open('Arielle.json', 'w', encoding='utf-8')

for i in range(0, 7):

    parm = {'pag':str(i)}

    r = requests.get(url, params=parm)

    soup = BeautifulSoup(r.text, 'lxml')

    url_prod = soup.find_all('div', class_='produto')

    for url_p in url_prod:
        url_produto = url_p.a.get('href')
        lista_url_produto.append(url_produto)


responde = raspagens(lista_url_produto, lis_ta)

data_json = json.dumps(responde, ensure_ascii=False)

arq_json = open('Arielle.json', 'a', encoding='utf-8')
arq_json.write(data_json)

arq_json.close()

arq_json.close()