class Solution:
    def matrixReshape(self, mat, r, c):
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat

        result = []
        temp = []

        for row in mat:
            for value in row:
                temp.append(value)

        for i in range(r):
            result.append(temp[i * c:(i + 1) * c])

        return result