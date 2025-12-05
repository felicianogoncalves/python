meses=['Janeiro','fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

listatemp=[]

for mes in meses:
    temp=float(input(f'{mes}:'))
    listatemp.append(temp)

mediaanual=sum(listatemp)/ len(meses)
print(f'Média anual de temperatura:{mediaanual:.2f}ºC')

for i in range(len(meses)):
    if listatemp[i] > mediaanual:
        print(f'{meses[i]}:{listatemp[i]}ºC')

