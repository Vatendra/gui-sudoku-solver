import numpy as np
import tkinter as tk
import findSolution
NN = 3 # rows/columns of subgrid
N = 9 # rows/columns of grid
class Sudoku():
    def __init__(self, master = None):
        self.printSudoku()
    def printSudoku(self):
        # prints the entry fields and solve button on window
        x_offset = 0 # To distinguish sub-grids while printing
        y_offset = 0 # To distinguish sub-grids while printing
        for i in range(N):            
            if(i%NN==0):
                y_offset = y_offset+4
            for j in range(N):
                if(j%NN==0):
                    x_offset = x_offset+4
                entryMatrix[i][j] = tk.Entry(root, font = ('calibre',16,'bold'), justify='center', bg='#0A090C', fg='#ECC30B',relief='raised')
                entryMatrix[i][j].place(x=j*40+x_offset, y=i*40+y_offset, width=40, height=40)
            x_offset = 0
root = tk.Tk()
entryMatrix = np.array([[None]*N]*N) # Stores entry field objects
valueMatrix = np.array([[0]*N]*N) # Copies integer values from entry field objects
root.title("Sudoku Solver")
root.geometry('376x468')
root.configure(bg='#0A090C')
app = Sudoku(master = root)

def showSolution(solution): # displays solution to entry fields on window
    for i in range(N):
        for j in range(N):
            if entryMatrix[i][j].get() == '':
                entryMatrix[i][j].configure(fg='#00A300') # Changing text color of solution
                entryMatrix[i][j].insert(0, solution[i][j]) # Inserting solution to empty cells
def getValueMatrix(): # copies user input from entry fields to valueMatrix
    for i in range(N):
        for j in range(N):
            if entryMatrix[i][j].get() != '':
                valueMatrix[i][j] = entryMatrix[i][j].get()
    solution = findSolution.getSolution(valueMatrix)
    showSolution(solution)
tk.Button(root, text="Solve", command=getValueMatrix, font = ('calibre',16,'bold'), bg='#FFFDFD', fg='#0A090C',relief='raised').place(x = 140, y = 400)
root.mainloop()