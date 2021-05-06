nota1 = float(input("Informe nota 1: "))
nota2 = float(input("Informe nota 2: "))

#Definimos o que é "Verificar uma Aprovação"
def verificar_aprovacao():
  media = calcular_media([nota1, nota2])

  if media >= 6:
    print("O Aluno Foi Aprovado!")
  else:
    print("O Aluno Foi Reprovado")

#Definimos o que é "Calcular a Média"
def calcular_media(notas):
  quantidade = len(notas)

  soma = 0
  for nota in notas:
    soma = soma + nota

  media = soma / quantidade

  return media

# Chamamos (executamos) a função de Verificar Aprovação
verificar_aprovacao()
