N = 9
NN = 3
def inRow(mat, row, key): # Checks whether a particular key exist in a row
    for i in range(N):
        if(mat[row][i]==key):
            return True
    return False
def inCol(mat, col, key): # Checks whether a particular key exist in a column
    for i in range(N):
        if(mat[i][col]==key):
            return True
    return False
def inSubGrid(mat, row, col, key): # Checks whether a particular key exist in a sub-grid
    for i in range(NN):
        for j in range(NN):
            if(mat[i+row][j+col]==key):
                return True
    return False
def isValid(mat, row, col, key): # Checks whether it is valid to insert an element
    if not inRow(mat, row, key) and not inCol(mat, col, key) and not inSubGrid(mat, row-row%NN, col-col%NN, key):
        return True
    return False
def getEmptyCell(mat):
    for i in range(N):
        for j in range(N):
            if(mat[i][j]==0):
                return i, j
    return None
def solve(mat):
    index = getEmptyCell(mat)
    if index == None:
        return True
    row = index[0]
    col = index[1]
    for i in range(N):
        if(isValid(mat, row, col, i+1)):
            mat[row][col] = i+1
            if solve(mat):
                return True
            mat[row][col] = 0
        global solMatrix
        solMatrix = mat
    return False
def getSolution(mat):
    solve(mat)
    return solMatrix

