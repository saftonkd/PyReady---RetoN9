def promedio(lista : list)-> float:
  suma = 0
  if len(lista) != 0:
    elementos = len(lista)
  else:
    return "El arreglo está vacío"
  for real in lista:
    suma += real
  return (suma / elementos)

if __name__ == "__main__":
  lista : list = []
  a = float(input("Ingrese un primer número: "))
  b = float(input("Ingrese un segundo número: "))
  c = float(input("Ingrese un tercer número: "))
  lista.append(a)
  lista.append(b)
  lista.append(c)
  print("El promedio de los números es: " + str(promedio(lista)))

  