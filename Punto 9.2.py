def producto_punto(primer_arreglo: list, segundo_arreglo: list)-> float:
  if len(primer_arreglo) == len(segundo_arreglo):
    producto_punto : float = 0
    for elemento in range(0, len(primer_arreglo)):
      producto = primer_arreglo[elemento] * segundo_arreglo[elemento]
      producto_punto += producto
  else:
    print("Los arreglos no son del mismo tamaño")
  return producto_punto

if __name__ == "__main__":
  primer_arreglo : list = [4, 3, 5, 7, 8.5, 6]
  segundo_arreglo : list = [1.2, 9, 8, 4.8, 2, 3]
  print(producto_punto(primer_arreglo, segundo_arreglo))