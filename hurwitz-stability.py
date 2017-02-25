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

#def check_matrix_determinant(matrix):
#   check if the matrix denominator renders the system unstable or marginally
#   stable

def create_minor(matrix, row, column):
    # removes the i-th row and the j-th column
    return matrix[
        np.array(list(range(row)) +
                 list(range(row+1, matrix.shape[0])))[:,np.newaxis],
        np.array(list(range(column)) +
                 list(range(column+1, matrix.shape[1])))]

def check_stability(hurwitz_matrix, coefficients):
    print(hurwitz_matrix)
    print("Determinant of this matrix is equal: "+
          str(np.linalg.det(hurwitz_matrix)))
    if np.linalg.det(hurwitz_matrix) > 0:
        print("Determinant of the hurwitz matrix is greater than zero")
    elif np.linalg.det(hurwitz_matrix) == 0:
        print("System is marginally stable")
    else:
        return("System is unstable")

    for _ in range(0, len(coefficients)-2):
        x,y = hurwitz_matrix.shape
        hurwitz_matrix= create_minor(hurwitz_matrix, x-1, y-1)
        print(hurwitz_matrix)
        print("Determinant of this matrix is equal: " +
              str(np.linalg.det(hurwitz_matrix)))
        if np.linalg.det(hurwitz_matrix) > 0:
            continue
        elif np.linalg.det(hurwitz_matrix) == 0:
            print("System is marginally stable")
            continue
        else:
            return("System is unstable")
    return("System is stable")

print("If the polynomial of the denominator of the system's characteristic "
      "equation (transfer function is given as: ")
print("a0*s^n + a1*s^(n-1) + ... + a(n-1)*s + an")
print("Enter the degree of the denominator polynomial")
degree = int(input('Degree: '))
coefficients = []
for x in range (0, degree+1):
    coefficient = int(input(str('Enter coefficient '+ 'a' + str(x) + ": ")))
    coefficients.append(int(coefficient))
print(coefficients)
print("To be stable, all of the system's denominator polynomial coefficients "
      "must be greater than zero")
matrix=create_hurwitz_matrix(coefficients)

print('Hurwitz Matrix: \n')
newmatrix=matrix
print(check_stability(newmatrix, coefficients))
