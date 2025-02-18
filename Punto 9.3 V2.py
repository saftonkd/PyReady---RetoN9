def ceros_final(lista: list)-> list:
  for numero in range(0, len(lista)):
    if lista[numero] == 0:
      lista.append(0)
      lista.pop(numero)
    else:
      continue
  return lista

if __name__ == "__main__":
  lista_uno : list = [1, 2, 3, 4, 5]
  lista_dos : list = [0, 1, 2, 3, 4, 0, 5]
  lista_tres: list = [0, 1, 2, 3, 0, 4, 5]
  print(ceros_final(lista_uno))
  print(ceros_final(lista_dos))
  print(ceros_final(lista_tres))