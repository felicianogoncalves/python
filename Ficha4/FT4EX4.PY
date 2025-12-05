#EX4

signos=['Macaco','galo','Cão',
        'Porco','Rato','Boi',
        'Tigre','Coelho','Dragão',
        'Serpente','Cavalo','Carneiro'
   ]
    
while True:
    
    ano=int(input('Digite o seu ano'))
    if ano==0:
       print('programa a encerrar...')
       break
    indice= ano%12
    signo=signos[indice]
    print(f'O seu signo do zodiaco chines é: {signo}')
print("fora bloco")