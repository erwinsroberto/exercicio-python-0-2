cores = []

for i in range (10):
  cores.append(str(input("Digite uma cor: ")))
busca = str(input("Digite uma cor para a busca: "))
while busca.upper() != "FIM":
  if busca in cores:
    idx = cores.index(busca)
    print("A cor", cores[idx], "está armazenada no indice ", cores.index(busca))
  else:
    print("Cor não encontrada!")
  busca = str(input("Digite uma cor para a busca: "))
    