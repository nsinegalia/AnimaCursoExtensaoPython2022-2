#criação de funções

preco = 1999.90

# Calcular 5% de imposto, guardar na variavel imposto e exibir na tela
imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

#Criar uma função calcular_imposto() que calcular um imposto de 5% e retorna quem pediu

def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto


#Aqui é o uso.. aqui é imposto a calcular..
preco = 299
imposto = calcular_imposto(preco)
print(imposto)