import math

# Somma di due vettori
def vector_add(v1, v2):
    return [ x + y for x, y in zip(v1, v2)]

# Differenza di due vettori
def vector_subtract(v1, v2):
    return [ x - y for x, y in zip(v1, v2)]

# Prodotto scalare di due vettori
def dot(v1, v2):
    return sum([ x*y for x, y in zip(v1, v2)])

# Prodotto scalare di un vettore per sé stesso
def sum_of_squares(v):
    return dot(v,v)

# Modulo di un vettore
def magnitude(v):
    return math.sqrt(sum_of_squares(v))

# Distanza di due vettori
def distance(v1, v2):
    return magnitude(vector_subtract(v1, v2))

# Somma di tutti i vettori contenuti in una lista di vettori
def vector_sum(vectors_list):
    return reduce(vector_add, vectors_list)

# Prodotto di uno scalare per un vettore
def scalar_multiply(scalar, vector):
    return [ scalar * element for element in vector ]

# Media dei vettori contenuti in una lista di vettori
def vector_mean(vectors_list):
    n = len(vectors_list)
    return scalar_multiply(1/n, vector_sum(vectors_list))

# Dimensioni di una matrice
def shape(matrix):
    rows = len(matrix);
    cols = len(matrix[0]) if matrix else 0
    return rows, cols

# Riga iesima di una matrice
def get_row(matrix, rindex):
    return matrix[rindex]

# Colonna iesima di una matrice
def get_column(matrix, cindex):
    return [ matrix_element[cindex] for matrix_element in matrix ]

# Costruisce una matrice delle dimensioni indicate utilizzando una funzione generatrice 
def make_matrix(nrows, ncols, valuegen_fn):
    return [ [valuegen_fn(i,j) for i in range(nrows)] for j in range(ncols) ]

# Restituisce la matrice quadrata identità di dimensione n*n
def eye(n):
    return make_matrix(n, n, lambda i,j: 1 if i==j else 0)

