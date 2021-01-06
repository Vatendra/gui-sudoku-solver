import numpy as np
import tkinter as tk
import findSolution
NN = 3
N = 9
class Sudoku():
    def __init__(self, master = None):
        self.printSudoku()
    def printSudoku(self):
        # prints the entry fields and solve button on window
        i = j = 0
        x_offset = -4
        y_offset = -4
        while i < 9:            
            if(i%NN==0):
                y_offset = y_offset+4
            while j < 9:
                if(j%NN==0):
                    x_offset = x_offset+4
                entryMatrix[i][j] = tk.Entry(root)
                entryMatrix[i][j].place(x=j*40+x_offset, y=i*40+y_offset, width=40, height=40)
                j = j+1
            j = 0
            x_offset = -4
            i = i+1
root = tk.Tk()
entryMatrix = np.array([[None]*9]*9)
valueMatrix = np.array([[0]*9]*9)
app = Sudoku(master = root)

def showSolution(solution): # fix insert object
    for i in range(N):
        for j in range(N):
            if entryMatrix[i][j].get() == '':
                entryMatrix[i][j].insert(0, solution[i][j])
def getValueMatrix():
    i = j = 0
    while i < 9:
        while j < 9:
            if entryMatrix[i][j].get() != '':
                valueMatrix[i][j] = entryMatrix[i][j].get()
            j = j+1
        j = 0
        i = i+1
    solution = findSolution.getSolution(valueMatrix)
    showSolution(solution)
tk.Button(root, text="Solve", command=getValueMatrix).place(x = 150, y = 400)
root.mainloop()