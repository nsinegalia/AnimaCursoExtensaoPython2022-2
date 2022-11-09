print("Início da aula 3 (09/11/2022)")

contador = 1

# Exibi de 1 até 10 repetidamente
while(contador <= 10):
  print(contador)
  contador = contador+1 # contador += 1

  
#Laço for (python for = for each)
fruta = "morango"
print(fruta)

#Lista
frutas = ["morango","laranja","pêra"]

#Quero exibir apenas a terceira fruta (pêra)
print(frutas[2])

#Exibir quantas frutas tem na minha lista? 
print(len(frutas)) #len = tamanho

#Quero incluir uma fruta nova
frutas.append("manga")

print(len(frutas)) 

print(frutas)

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])

print("Exemplo das frutas com while..")

i=0
while(i<len(frutas)):
  print(frutas[i])
  i = i + 1