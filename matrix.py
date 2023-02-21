import numpy as np

matrix2x3 = [[3, 1, 3], [6, 5, 5]]
matrix3x2 = [[100, 50], [50, 100], [50, 50]]

matrixmult = np.dot(matrix2x3, matrix3x2)
resultmaio = matrixmult[0][0] + matrixmult[1][0]
resultjunho = matrixmult[1][1] + matrixmult[0][1]

print("==Maio Junho==")
print(matrixmult)
print("=========================================")
print("O total de botões em Maio sera de {}".format(resultmaio))
print("O total de botões em Junho sera de {}".format(resultjunho))
print("=========================================")


