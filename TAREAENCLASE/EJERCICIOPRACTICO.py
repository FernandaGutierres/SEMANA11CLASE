# Matriz inicial
gutierres = [[9, 8, 7],
          [6, 5, 4],
          [3, 2, 1]]

# Mostrar matriz desordenada
print("Matriz desordenada:")
for row in gutierres:
    print(row)

# Ordenar la matriz
for row in gutierres:
    row.sort()

# Mostrar matriz ordenada
print("\nMatriz ordenada:")
for row in gutierres:
    print(row)