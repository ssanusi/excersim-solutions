class Matrix(object):
    def __init__(self, matrix_string):
        row_operation = matrix_string.split("\n")
        self.matrix = [x.split(' ') for x in row_operation]

    def row(self, index):
        matrix_str = self.matrix[index - 1]
        return [int(x) for x in matrix_str]

    def column(self, index):
        return  [int(x[index - 1]) for x in self.matrix]

