
cont=1
with open('myDocument.txt','a+') as conteudo:
    conteudo.write("\nsou novo conteudo\n")
    cont+=1
    ##print(conteudo.read())


#print(ficheiro)