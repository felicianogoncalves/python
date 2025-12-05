
nome=(input('Digite o seu nome:'))



def mediaAluno():
    nota1=int(input('Digite a primeira nota:'))
    nota2=int(input('Digite a segunda nota:'))
    nota3=int(input('Digite a terceira nota:'))
    return (nota1+nota2+nota3)/3

media=mediaAluno()

def classificacaoAluno():
    if media>=10:
        print(f'O aluno {nome} tem a {media:.2f} Aprovado')
    else:
        print(f'O aluno {nome} tem a {media:.2f} Reprovado')
    

classificacaoAluno()

