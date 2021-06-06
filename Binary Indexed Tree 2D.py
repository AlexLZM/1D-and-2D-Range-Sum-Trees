import itertools

class BIT2D:

    def __init__(self, matrix):
        '''
        initiate the tree with a matrix(list of lists)
        '''
        self.matrix = matrix
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.trees = [[0] * (self.m + 1) for _ in range(self.n+1)]
        for y, x in itertools.product(range(self.n), range(self.m)):
            self._update(y, x, matrix[y][x])
        
        
        

    def update(self, row: int, col: int, val: int) -> None:
        '''
        update a valeu in matrix at (row, col) coord
        '''
        prev = self.matrix[row][col]
        self.matrix[row][col] = val
        diff = val - prev
        self._update(row, col, diff)
        
    def _update(self, row, col, diff):
        '''
        BIT updates based on diff
        '''
        row += 1; col += 1
        while row <= self.n:
            col_ = col
            while col_ <= self.m:
                self.trees[row][col_] += diff
                col_ += (col_ & (-col_))
            row += (row & (-row))

    def query(self, y, x): 
        '''
        get sum over region (0, 0) to (y, x)
        '''
        y += 1; x += 1
        # sum over all cols in all rows
        s = 0
        while y > 0:
            x_ = x
            while x_ > 0:
                s += self.trees[y][x_]
                x_ -= (x_ & (-x_))
            y -= (y & (-y))

        return s 


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        '''
        4 queries are needed for a rectangle not involving (0,0)
        '''
        
        a = self.query(row2, col2)
        b = self.query(row1-1, col1-1)
        c = self.query(row2, col1-1)
        d = self.query(row1-1, col2)

        return a + b - c - d
