import json

with open('info_aluno.json','r',encoding='utf-8') as file:
    dados=json.load(file)
    print(dados)
    print('O nome do aluno é:',dados["nome"],'e o seu curso é',dados['curso'])
    dados['idade']=22
    dados['ano']=2
    print(dados)
with open('info_aluno.json','w',encoding='utf-8') as file:
    json.dump(dados,file, indent=4, ensure_ascii=False)



