#----------------------------------------------------------------------------
# Ambrose Ryan Xavier
#----------------------------------------------------------------------------
# Data Generation Template
#----------------------------------------------------------------------------
# 3 4
# 2 2 5
# 1 2 4
# 0 1 2
# 0 0 1
# 1 1 3
# 2 3 6
# stop
# 0 1 1
# 0 2 2
# 1 2 3
# 1 3 4
# 2 0 6
# 2 3 -6
# stop
#----------------------------------------------------------------------------

def print_matrix(matrix, rows, columns, label):
    print(label + "\n")
    row = "|"
    for i in range(rows):
        print_header(columns)
        for j in range(columns):
            row += "{n: >3}".format(n = str(matrix.get((i, j), 0))) + "|"
        print(row)
        row = "|"
    print_header(columns)
    print()

def add_matrices(matrix_01, matrix_02, rows, columns):
    matrix_03 = {}
    for i in range(rows):
        for j in range(columns):
            summation = (matrix_01.get((i, j), 0) + matrix_02.get((i, j), 0))
            if summation != 0:
                matrix_03[(i, j)] = summation
    return matrix_03

def print_header(columns):
    line = "+"
    for i in range(columns):
        line += "---+"
    print(line)

def read_matrix(input_file):
    matrix = {}
    line = input_file.readline().split()
    while line[0] != "stop":
        row = int(line[0])
        column = int(line[1])
        value = int(line[2])
        matrix[(row, column)] = value
        line = input_file.readline().split()
    return matrix

def main(file_name):
    input_file = open(file_name, "r")

    line = input_file.readline().split()
    rows = int(line[0])
    columns = int(line[1])

    matrix_01 = read_matrix(input_file)
    print_matrix(matrix_01, rows, columns, "Matrix 01")

    matrix_02 = read_matrix(input_file)
    print_matrix(matrix_02, rows, columns, "Matrix 02")

    matrix_03 = add_matrices(matrix_01, matrix_02, rows, columns)
    print_matrix(matrix_03, rows, columns, "Matrix 01 + Matrix 02")
    print("Matrix 03 = ", matrix_03, "\n")

main("sparse-matrix.txt")
