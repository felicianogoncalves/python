#EX3

assi=float(input('Insira a assiduidade do anulo:'))
nota=float(input('Insira a nota do teste:'))

if assi<75 or (assi>75 and nota<=5):
    print('Reprovado')
elif assi>75 and nota>=10:
    print('Aprovado')
else:
    print('exame')