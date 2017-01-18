""" Question 1.7 """


def rotate_matrix(matrix):
    """  Rotate a NxN matrix by 90 degrees """
    N = len(matrix[0])
    row = 0
    edge = N - 1
    while row <= N/2-1:
        for col in range(row, row+edge):
            # row = 1, edge = 1 col = 1
            temp = matrix[row][col]
            # 0,1 = 2,0
            matrix[row][col] = matrix[N-1-col][row]
            # 2,0 = 3,2
            matrix[N-1-col][row] = matrix[N-1-row][N-1-col]
            # 3,2 = 1,3
            matrix[N-1-row][N-1-col] = matrix[col][N-1-row]
            # 1,3 = 0,0
            matrix[col][N-1-row] = temp
        row += 1
        edge -= 2
    return matrix

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
matrix_after_rotate = [[13, 9, 5, 1],
                       [14, 10, 6, 2],
                       [15, 11, 7, 3],
                       [16, 12, 8, 4]]

matrix1 = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]]
matrix1_after_rotate = [[21, 16, 11, 6, 1],
                        [22, 17, 12, 7, 2],
                        [23, 18, 13, 8, 3],
                        [24, 19, 14, 9, 4],
                        [25, 20, 15, 10, 5]]

assert rotate_matrix(matrix) == matrix_after_rotate
assert rotate_matrix(matrix1) == matrix1_after_rotate
