import numpy as np
import sys

print("Jezeli wielomian mianownika jest zapisany jako: ")
print("a0*s^n + a1*s^(n-1) + ... + a(n-1)*s + an")
print("Podaj stopien mianownika")
stopien = int(input('Stopien: '))
A = []
for x in range (0, stopien+1):
    wspolczynnik = int(input(str('Podaj wspolczynnik '+ 'a' + str(x) + ": ")))
    A.append(int(wspolczynnik))
print(A)
print("\nAby uklad mogl byc stabilny, wszystkie wspolczynniki rownania charakterystycznego musza byc wieksze od zera")
matrix=[]
k = 0

for _ in range(0, len(A)-1):
    column = []
    d = 0
    for _ in range(0, len(A)-1):
        if 2*d+1-k < 0:
            column.append(0)
        else:
            try:
                column.append(A[2*d+1-k])
            except IndexError:
                column.append(0)
        d += 1
    matrix.append(column)
    k += 1

print('Macierz Hurwitza: \n')
print(np.array(matrix))
print("Wyznacznik tej macierzy jest rowny: " +
      str(np.linalg.det(np.array(matrix))))
if np.linalg.det(np.array(matrix)) < 0:
    print("Uklad jest niestabilny.")
    sys.exit()
if np.linalg.det(np.array(matrix)) == 0:
    print("Uklad na granicy stabilnosci.")

def minor(arr, i, j):
    # usuwa i-ty wiersz i j-ta kolumne
    return arr[np.array(list(range(i))+list(range(i+1, arr.shape[0])))[:,np.newaxis],
               np.array(list(range(j))+list(range(j+1, arr.shape[1])))]
a=0
newmatrix=np.array(matrix)
for _ in range(0, len(A)-2):
    x,y = newmatrix.shape
    newmatrix= minor(np.array(newmatrix), x-1, y-1)
    print(newmatrix)
    print("Wyznacznik tej macierzy jest rowny: " +
          str(np.linalg.det(newmatrix)))
    if np.linalg.det(newmatrix) > 0:
        continue
    elif np.linalg.det(newmatrix) == 0:
        print("Uklad na granicy stabilnosci")
        continue
    else:
        print("Uklad jest niestabilny")
        sys.exit()
print("Uklad jest stabilny.")


