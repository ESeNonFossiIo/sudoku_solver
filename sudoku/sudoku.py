class Board(object):
    def __init__(self, board=None):
        if board != None:
            self.cells    = board.cells[:]
        else:
            self.cells    = [0]*81

    def __call__(self, x, y, v = None):
        if v != None:
            self.cells[x + 9*y] = v
        return self.cells[x + 9*y]

    def col(self, i):
        return [ self.cells[j + 9*i] for j in range(9) ]

    def row(self, j):
        return [ self.cells[j + 9*i] for i in range(9) ]

    def get_sub_matrix(self, i, j):
        return [ self.cells[ii + 9*jj] for ii in range(3*i, 3*(i+1)) for jj in range(3*j, 3*(j+1))]

    def is_valid(self):
        for i in range(3):
            for j in range(3):
                for v in [self.col(i + 3*j), self.row(i + 3*j), self.get_sub_matrix(i,j)]:
                    if len(set([i for i in v if i>0])) != len([i for i in v if i!=0]):
                        return False
        return True

    def available_digits(self, i, j):
        res = [i for i in self.col(j) + self.row(i) + self.get_sub_matrix(i//3,j//3) if i > 0]
        return (set(range(1,10)) - set(res))

    def __str__(self):
        r = ""
        for i in range(9):
            if i%3 == 0:
                r += "="*41 + "\n"
            for j in range(9):
                if j%3 == 0:
                    r += "||%2d "%self.cells[i+9*j]
                else:
                    r += "|%2d "%self.cells[i+9*j]
            r += "||\n"
        r += "="*41 + "\n"
        return r

def solve(board, n = 0):
    if not board.is_valid():
        return None
    b = Board(board)
    if n == 81:
        return b
    else:
        i, j = n//9, n%9
        if b(i,j) == 0:
            for m in b.available_digits(i,j):
                b(i,j,m)
                res = solve(b, n+1)
                if res != None:
                    return res
        else:
            return solve(b, n+1)
