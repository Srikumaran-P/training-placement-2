def rotate(matrix):
    matrix[:] = zip(*matrix[::-1])
