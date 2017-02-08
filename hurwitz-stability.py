#!/usr/bin/env python3

"""This program takes a linear system's characteristic equation (its coefficients)
and checks the system's stability against the Hurwitz stability criterion."""

__author__ = "Adam Kosuń"

import numpy as np
import sys

def create_hurwitz_matrix(coefficients):
    k = 0
    matrix = []
    for _ in range(0, len(coefficients)-1):
        column = []
        for d in range(0, len(coefficients)-1):
            if 2*d+1-k < 0:
                column.append(0)
            else:
                try:
                    column.append(coefficients[2*d+1-k])
                except IndexError:
                    column.append(0)
            d += 1
        matrix.append(column)
        k += 1
    return np.array(matrix)

def check_stability(hurwitz_matrix, coefficients):
    a=0
    for _ in range(0, len(coefficients)-2):
        x,y = hurwitz_matrix.shape
        hurwitz_matrix= create_minor(np.array(hurwitz_matrix), x-1, y-1)
        print(hurwitz_matrix)
        print("Determinant of this matrix is equal: " +
              str(np.linalg.det(hurwitz_matrix)))
        if np.linalg.det(hurwitz_matrix) > 0:
            continue
        elif np.linalg.det(hurwitz_matrix) == 0:
            print("System is marginally stable")
            continue
        else:
            print("System is unstable")
            sys.exit()
    print("System is stable")

def create_minor(matrix, row, column):
    # usuwa i-ty wiersz i j-ta kolumne
    return matrix[np.array(list(range(row))+list(range(row+1, matrix.shape[0])))[:,np.newaxis],
               np.array(list(range(column))+list(range(column+1, matrix.shape[1])))]

print("Jezeli wielomian mianownika jest zapisany jako: ")
print("a0*s^n + a1*s^(n-1) + ... + a(n-1)*s + an")
print("Podaj stopien mianownika")
stopien = int(input('Stopien: '))
coefficients = []
for x in range (0, stopien+1):
    wspolczynnik = int(input(str('Podaj wspolczynnik '+ 'a' + str(x) + ": ")))
    coefficients.append(int(wspolczynnik))
print(coefficients)
print("\nAby uklad mogl byc stabilny, wszystkie wspolczynniki rownania charakterystycznego musza byc wieksze od zera")
matrix=create_hurwitz_matrix(coefficients)

print('Macierz Hurwitza: \n')
print(matrix)
print("Wyznacznik tej macierzy jest rowny: " +
      str(np.linalg.det(np.array(matrix))))
if np.linalg.det(np.array(matrix)) < 0:
    print("Uklad jest niestabilny.")
    sys.exit()
if np.linalg.det(np.array(matrix)) == 0:
    print("Uklad na granicy stabilnosci.")

a=0
newmatrix=np.array(matrix)
for _ in range(0, len(coefficients)-2):
    x,y = newmatrix.shape
    newmatrix= create_minor(np.array(newmatrix), x-1, y-1)
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


