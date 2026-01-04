class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        row = [1]
        for i in range(0, numRows):
            triangle.append(row[:])
            row.append(1)
            for j in range(len(row) - 2, 0, -1):
                row[j] = row[j] + row[j-1]
        return triangle
