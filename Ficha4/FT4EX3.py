notas= [7.5,15.3,14.9,13.5]

print(notas)
print(sum(notas),'Soma do valores')
media=(sum(notas)/len(notas))
print(media,'media dos valores')

notas.append(3)
print(notas)
print(sum(notas),'Soma do valores com a nova nota')
media=(sum(notas)/len(notas))
print(media,'media dos valores com a nova nota')
