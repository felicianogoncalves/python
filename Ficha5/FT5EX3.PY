# alunos={'rui':[10,15,20],
#       'maria':[11,13,20],
#       'jose':[9,20,20],
#       }

# for nome,notas in alunos.items():
#     media=sum(notas)/len(notas)
#     print(f'{nome} - Média:{media:.2f}')


alunos={}
for i in range(3):
    nome=input('Digite o nome do aluno:')
    nota1=float(input('Digite nota 1:'))
    nota2=float(input('Digite nota 2:'))
    alunos[nome]=[nota1,nota2]
print('\n Media dos alunos \n')

for nome,notas in alunos.items():
    media=sum(notas)/len(notas)
    print(f'{nome} - Média:{media:.2f}')


