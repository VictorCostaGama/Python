import requests, re, time
from bs4 import BeautifulSoup

def coletar_url(re_gex, regex):
    
    for i in range(0, len(re_gex)):
        response = requests.get(url=re_gex[i])
        r = re.findall(r'/servico/[\w-]+', response.text, re.I)
        time.sleep(1)
        
    for i in range(0, len(r)):
        if r[i] in regex:
            pass
        else:
            regex.append(r[i])
    
    return regex


def raspagem(regex, lista, dicionario):
    
    for i in range(0, len(regex)):
        
        dicionario['url'] = str(regex[i])
        resp = requests.get(url=regex[i])
        soup = BeautifulSoup(resp.text, 'lxml')
        
        d = soup.find_all('div', class_='field-items')
        e = soup.find('h1', class_='page-header')
        servico = e.get_text()

        for i in range(0, len(d)):
            if i == 2:
                descricao = d[2].get_text()
                apagar = '\n\xa0.'

                for i in range(0,len(apagar)):
                    descricao = descricao.replace(apagar[i], '')
                    
            elif i == 3:    
                documentos = d[3].get_text()
                apagar = '\n\xa0.'

                for i in range(0,len(apagar)):
                    documentos = documentos.replace(apagar[i], '')
                
            elif i == 4:
                valor = d[4].get_text()
                apagar = '\n\xa0.'

                for i in range(0,len(apagar)):
                    valor = valor.replace(apagar[i], '')
            
            elif i == 5:
                orgaos_responsaveis = d[5].get_text()
                apagar = '\n\xa0.'

                for i in range(0,len(apagar)):
                    orgaos_responsaveis = orgaos_responsaveis.replace(apagar[i], '')
        
        
        dicionario['servico'] = str(servico)
        dicionario['descricao'] = str(descricao)
        dicionario['documentos'] = str(documentos)
        dicionario['valor'] = str(valor)
        dicionario['orgaos_responsavel'] = str(orgaos_responsaveis)

        lista.append(dicionario)
            
        time.sleep(1)
        
    return lista
        

url = 'http://mg.gov.br/cidadao'

response = requests.get(url=url)

regex = re.findall(r'/servico/[\w-]+', response.text, re.I)
re_gex = re.findall(r'/cidadao/[0-9]+', response.text, re.I)
time.sleep(1)

url_parcial = 'http://mg.gov.br'

lista = []
dicionario = {}

for i in range(0, len(re_gex)):
    re_gex[i] = url_parcial + re_gex[i]

coletar_url(re_gex, regex)

for i in range(0, len(regex)):
    regex[i] = url_parcial + regex[i]

raspagem(regex, lista, dicionario)
        
print(lista)