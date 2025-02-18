# **Universidad Nacional de Colombia**
## **Programación de Computadores (Código 2015734)**
### **Repositorio elaborado por:** Santiago Romero Mejía
___

>**Objetivo**: Solucionar los problemas planteados en el Reto #9 (Repositorio de la clase #13)

**Desarrollo**: Para cada punto se desarrolló un programa individual. Los primeros tres (3) puntos son documentos de Visual Studio Code y están anexos a este repositorio individualmente de igual manera.

Actividad 4: Consultar sobre el método de sorteo Bubble Sort.
### **Bubble Sort**  
Es un algoritmo de ordenamiento de comparación que intercambia elementos adyacentes si están en el orden incorrecto. Es un método estable, ya que no altera el orden relativo de elementos iguales.  

### **Funcionamiento**  
1. Se comparan dos elementos adyacentes; si están en el orden incorrecto, se intercambian.  
2. Después de cada iteración, el elemento más grande se posiciona correctamente al final.  
3. Si en una pasada no hubo intercambios, significa que la lista ya está ordenada y el algoritmo puede detenerse antes de completar todas las iteraciones.  

### **Complejidad Temporal**  
- **Peor caso y caso promedio**: O(n²) (cuando la lista está completamente desordenada).  
- **Mejor caso**: O(n) (cuando la lista ya está levemente ordenada, usando la optimización de detección de cambios).  

### **Ventajas**  
- Fácil de entender e implementar.  
- No altera el orden de elementos iguales.  
- **Útil para listas pequeñas o casi ordenadas**.  

### **Desventajas**  
- Ineficiente en listas grandes debido a su complejidad cuadrática.  
- Número elevado de comparaciones e intercambios en listas desordenadas.  
