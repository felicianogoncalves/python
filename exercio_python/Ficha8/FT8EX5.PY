import json

with open('meteorologia.json','r',encoding='utf-8') as file:
    dados=json.load(file)
    print(dados)
    print(json.dumps(dados,indent=4, ensure_ascii=False))
    for dia in dados['previsao']:
        if dia['dia'] == 'Terça-feira':
            temp_max=dia['temperatura']['max']
            print(f'A temperatura maxima de terça feira é {temp_max}ºC')
            break


with open('meteorologia.json','r',encoding='utf-8') as file:
    dados=json.load(file)
    for dado in dados['previsao']:
        if dado["condicoes"]== "Ensolarado":
            dia=dado["dia"]
            print(f'O dia da semana em que vai estar ensolarado é {dia}')
previsao=dados['previsao']
print(f'SEM A QUINTA-FEITA:\n',previsao)
previsao.append({"dia":"Quinta-feira","temperatura":{"min":18,"max":26},"condicoes":"Nublado","Vento":{"direcao":"leste","velocidade_kmh":"12"}})

print(f'Com Quinta-feira:\n',previsao)

previsao[2]["vento"]["velocidade_kmh"]=25

print('-----------FINAL STEP----------------')
print(dados)

with open('meteorologia.json','w',encoding='utf-8') as file:
    json.dump(dados,file,indent=4,ensure_ascii=False)