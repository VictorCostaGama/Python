import requests
from bs4 import BeautifulSoup

def raspagens (lista_url_produto, lis_ta):
    
    d = {}
    i = 0
    lista_faces = []
    lista_vs_amb = []
    lista_extras = []


    for i in range(0, len(lista_url_produto)):

        url_prod = lista_url_produto[i]
        r = requests.get(url_prod)
        soup = BeautifulSoup(r.text, 'lxml')

        nome_produto = soup.h2.get_text()
        nome_produto = nome_produto.replace('            ', '')
        nome_produto = nome_produto.replace('             Voltar', '')
        nome_produto = nome_produto.replace(' Voltar', '')
        nome_produto =nome_produto.replace('\n', '')

        ref= soup.find_all('div', class_='descricao')
        
        for refer in ref:
            referencia = refer.div.h3.text
            superf = refer.div.find_next_sibling()
            superf = superf.find_next_sibling()
            superf = superf.find_next_sibling()
            superf = superf.find_next_sibling()

            imag = soup.find_all('div', class_='imagem')

        for img in imag:
            imagem = img.div.get('ref')

        for form in ref:
            forma = form.find_all('div', class_='half')
        
        for formate in forma:
            formato = formate.find('h3')
            formato = formato.text
            formato = formato.replace(' cm', 'cm')
            break

        pei = forma[1].h3.get_text()

        box_informacao = soup.find_all('div', class_='boxes')

        for box in box_informacao:
            local_uso = box.button.get_text()
            local_uso = local_uso.replace('                                ', '')
            local_uso = local_uso.replace('                            ', '')
            local_uso = local_uso.replace('\n', '')
            caracteristica_uso = box.button.get('data-title')
            
            classificacao_tonal = box.button.next_element.next_element.next_element.get_text()
            classificacao_tonal = classificacao_tonal.replace('                                ', '')
            classificacao_tonal = classificacao_tonal.replace('                            ', '')
            classificacao_tonal = classificacao_tonal.replace('\n', '')
            caracteristica_tonal = box.button.next_element.next_element.next_element.get('data-title')
            
            impressao = box.button.next_element.next_element.next_element.next_element.next_element.next_element.get_text()
            impressao = impressao.replace('                                ', '')
            impressao = impressao.replace('                            ', '')
            impressao = impressao.replace('\n', '')
            
            if impressao == '':
                impressao = 'None'
                i = i + 1
            elif impressao == 'HD':
                pass
                i = i + 1
            else:
                impressao = 'None'
                i = i + 1
            caracteristica_impressao = box.button.next_element.next_element.next_element.next_element.next_element.next_element.get('data-content')
            
            if caracteristica_impressao != 'Produto com impressão em alta definição em tecnologia digital':
                caracteristica_impressao = 'None'

            resistencia = box.button.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
 
            if resistencia == '\n':
                teste = box.button.next_element.next_element.next_element.next_element.next_element.next_element.get('data-title')
                if teste == "Maior resistência a marca d'água":
                    resistencia = teste
                else:
                    resistencia = 'None'
            else:
                resistencia = resistencia.get('data-title')

            sentido_assentamento = box.find('i', class_="fa fa-arrow-down")
            if sentido_assentamento != None:
                sentido_assentamento = '↓'
            
            quantidades_faces = box.find('button', title='Quantidade de faces')
            caracteristica_faces = quantidades_faces
            if quantidades_faces != None:
                quantidades_faces = quantidades_faces.get_text()
                quantidades_faces = quantidades_faces.replace('                                ', '')
                quantidades_faces = quantidades_faces.replace('                            ', '')
                quantidades_faces = quantidades_faces.replace('\n', '')

            if caracteristica_faces != None:
                caracteristica_faces = caracteristica_faces.get('data-content')
            else:
                caracteristica_faces = 'None'
            
            imagem_faces = soup.find_all('div', class_='fotos')

            for img_f in imagem_faces:
                imf = img_f.find_all('a')
                for ifc in imf:
                    if ifc != None:
                        imagens_faces = ifc.get('href')
                        lista_faces.append(imagens_faces)
                    else:
                        ifc = 'None'
                        imagens_faces = ifc
                        lista_faces.append(imagens_faces)
            if lista_faces == None:
                lista_faces.append('None')
                lista_faces.append('None')
                lista_faces.append('None')
                lista_faces.append('None')
                lista_faces.append('None')
                lista_faces.append('None')
            else:
                while(len(lista_faces) != 6):
                    lista_faces.append('None')
            for i in range(0, len(lista_faces)):
                if i == 0:
                    imagem_face_1 = lista_faces[i]
                if i == 1:
                    imagem_face_2 = lista_faces[i]
                if i == 2:
                    imagem_face_3 = lista_faces[i]
                if i == 3:
                    imagem_face_4 = lista_faces[i]
                if i == 4:
                    imagem_face_5 = lista_faces[i]
                if i == 5:
                    imagem_face_6 = lista_faces[i]
            
            vs_amb = soup.find_all('button', class_='fancyclick big')

            for vs in vs_amb:
                vsc = vs.get('ref')
                lista_vs_amb.append(vsc)

            while (len(lista_vs_amb) != 2):
                lista_vs_amb.append('None')
            
            visualizador_ambiente = lista_vs_amb[1]

            inform_ext = soup.find_all('div', class_='modal-body')
            for inf in inform_ext:
                informacoes = inf.find_all('p')
            for inf_e in informacoes:
                inform = inf_e.get_text()
                inform = inform.replace('\n', '')
                inform = inform.replace('                            ', '')
                inform = inform.replace('                                                            ', '')
                inform = inform.replace(' ', '')
                inform = inform.replace('    ', '')
                inform = inform.replace('Áreaporcaixa:', '')
                inform = inform.replace('Nºdepeçasporcaixa:', '')
                inform = inform.replace('Espessuradapeça:', '')
                inform = inform.replace('Pesobrutoporcaixa:', '')
                inform = inform.replace('Metrosquadradosporpallet:', '')
                inform = inform.replace('Metrosquadradosporpallet(especial/exportação):', '')
                inform = inform.replace('Caixasporpallet:', '')
                inform = inform.replace('Caixasporpallet(especial/exportação):', '')
                inform = inform.replace('Pesobrutopallet:', '')
                inform = inform.replace('Pesobrutopallet(especial/exportação):', '')
                inform = inform.replace('Metrosquadradosporcontainer:', '')
                inform = inform.replace('Palletsporcontainer:', '')
                inform = inform.replace('unidades', ' unidades')
                
                lista_extras.append(inform)

            area_caixa = lista_extras[0]
            numero_pecas_caixa = lista_extras[1]
            espessura_pecas = lista_extras[2]
            peso_bruto_caixa = lista_extras[3]
            metros_quadrados_pallet = lista_extras[4]
            metros_quadrados_pallet_epecial_exportacao = lista_extras[5]
            caixas_pallet = lista_extras[6]
            caixas_pallet_especial_exportacao = lista_extras[7]
            peso_bruto_pallet = lista_extras[8]
            peso_bruto_pallet_especial_exportacao = lista_extras[9]
            metros_quadrados_container = lista_extras[10]
            pallets_container = lista_extras[11]

            superficie = superf.h3.get_text()
            superficie = superficie.replace('                                ', '')
            superficie = superficie.replace('                            ', '')
            superficie = superficie.replace('\n', '')
            superficie = superficie.replace('                        ', '')

            lista_faces.clear()
            lista_vs_amb.clear()
            lista_extras.clear()
            d['url_produto'] = str(url_prod)
            d['imagem'] = str(imagem)
            d['nome_produto'] = str(nome_produto)
            d['referencia'] = str(referencia)
            d['formato'] = str(formato)
            d['pei'] = str(pei)
            d['local_uso'] = str(local_uso)
            d['caracteristica_uso'] = str(caracteristica_uso)
            d['classificacao_tonal'] = str(classificacao_tonal)
            d['caracteristica_tonal'] = str(caracteristica_tonal)
            d['impressao'] = str(impressao)
            d['caracteristica_impressao'] = str(caracteristica_impressao)
            d['resistencia'] = str(resistencia)
            d['sentido_assentamento'] = str(sentido_assentamento)
            d['quantidades_faces'] = str(quantidades_faces)
            d['caracteristica_faces'] = str(caracteristica_faces)
            d['superficie'] = str(superficie)
            d['imagem_face_1'] = str(imagem_face_1)
            d['imagem_face_2'] = str(imagem_face_2)
            d['imagem_face_3'] = str(imagem_face_3)
            d['imagem_face_4'] = str(imagem_face_4)
            d['imagem_face_5'] = str(imagem_face_5)
            d['imagem_face_6'] = str(imagem_face_6)
            d['visualizador_ambiente'] = str(visualizador_ambiente)
            d['area_caixa'] = str(area_caixa)
            d['numero_pecas_caixa'] = str(numero_pecas_caixa)
            d['espessura_pecas'] = str(espessura_pecas)
            d['peso_bruto_caixa'] = str(peso_bruto_caixa)
            d['metros_quadrados_pallet'] = str(metros_quadrados_pallet)
            d['metros_quadrados_pallet_epecial_exportacao'] = str(metros_quadrados_pallet_epecial_exportacao)
            d['caixas_pallet'] = str(caixas_pallet)
            d['caixas_pallet_especial_exportacao'] = str(caixas_pallet_especial_exportacao)
            d['peso_bruto_pallet'] = str(peso_bruto_pallet)
            d['peso_bruto_pallet_especial_exportacao'] = str(peso_bruto_pallet_especial_exportacao)
            d['metros_quadrados_container'] = str(metros_quadrados_container)
            d['pallets_container'] = str(pallets_container)
            lis_ta.append(str(d))
            break
         
    return lis_ta