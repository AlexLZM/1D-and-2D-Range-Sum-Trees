class SegTree2D:

    def __init__(self, matrix):
        '''
        initiate the tree with a matrix (list of lists)
        '''
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.trees = [[0] * 2*self.m for i in range(2*self.n)]
        
        # build subtrees from right to left
        for i in range(self.n):
            self.trees[i+self.n][self.m:] = matrix[i]
            for j in range(self.m-1, 0, -1): 
                self.trees[i+self.n][j] = self.trees[i+self.n][j<<1] + self.trees[i+self.n][j<<1|1]
        
        # build total tree upward
        for i in range(self.n-1, 0, -1):
            self.trees[i][1:] = [self.trees[i<<1][j]+self.trees[i<<1|1][j] for j in range(1, 2*self.m)]
            
        
        

    def update(self, row: int, col: int, val: int) -> None:
        '''
        update the matrix at (row, col) coordinate with value val
        '''

        row += self.n; col += self.m
        self.trees[row][col] = val
        
        
        cols = [col]
        while col > 1: # undate all the parent columns and record the col index updated 
            self.trees[row][col>>1] = self.trees[row][col] + self.trees[row][col^1]
            col >>= 1
            cols.append(col)
        
        for col in cols:
            r = row
            # update all the parent rows at all the updated cols vertically
            while r > 1:
                self.trees[r>>1][col] = self.trees[r][col] + self.trees[r^1][col]
                r >>= 1

        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        '''
        sum the rectangle region from [row1, col1] to [row2, col2] 
        (all cells included)
        '''

        rows = []
        # convert to [start,end) range (half inclusive)
        row1 += self.n
        row2 += self.n + 1 
        col1 += self.m
        col2 += self.m + 1

        def sumRow(col1, col2, row):
            # sum a row on the range
            nonlocal res
            while col1 < col2:
                if col1 & 1:
                    res += self.trees[row][col1]
                    col1 += 1
                if col2 & 1:
                    col2 -= 1
                    res += self.trees[row][col2]
                col1 >>= 1
                col2 >>= 1
        
        res = 0
        # sum over row and parent rows
        while row1 < row2:
            if row1 & 1:
                sumRow(col1, col2, row1)
                row1 += 1
            if row2 & 1:
                row2 -= 1
                sumRow(col1, col2, row2)
            row1 >>= 1
            row2 >>= 1        
        
        return res