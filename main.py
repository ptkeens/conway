#!/usr/bin/env python3

from random import randint

class GOLBoard:
    liveCell = 1
    deadCell = 0

    def __init__(self, xSize, ySize):
        self.xSize = xSize
        self.ySize = ySize
        self.generation = 0

    def seedBoard(self):
        self.board = [];

        for i in range(self.xSize):
            self.board.append(self.randomList(self.ySize))

    def randomList(self, len):
        myList = []
        for i in range(len):
            myList.append(randint(0,1))

        return myList

    def setBoard(self, board):
        self.board = board

    def getBoard(self):
        return self.board

    def initNewBoard(self):
        return [ [0] * self.ySize for i in range(self.xSize)]

    def evolveBoard(self):
        nextBoard = self.initNewBoard()

        for i in range(self.xSize):
            for j in range(self.ySize):
                nextBoard[i][j] = self.getCellsNextState(i, j)

        self.board = nextBoard
        self.generation += 1

    def __str__(self):
        return f"I am a {self.xSize} x {self.ySize} board!"

    def getCellsNextState(self, x, y):
        xRange = self.getNeighborRangeForAxis(x, self.xSize)
        yRange = self.getNeighborRangeForAxis(y, self.ySize)

        liveCells = 0
        deadCells = 0

        for i in xRange:
            for j in yRange:
                # don't evaluate our curent cell
                if (i,j) != (x,y):
                    if self.board[i][j] > 0:
                        liveCells += 1
                    else:
                        deadCells += 1
        
        currentState = self.board[x][y]

        if currentState:
            if liveCells < 2:
                next =  self.deadCell
            elif liveCells > 1 and liveCells < 4:
                next = self.liveCell
            else:
                next = self.deadCell
        else:
            if liveCells == 3:
                next = self.liveCell
            else:
                next = self.deadCell

        return next

    def getNeighborRangeForAxis(self, axisVal, axisMax):
        cellRange = []
        if axisVal-1 >=0:
            cellRange.append(axisVal-1)
        cellRange.append(axisVal)
        if axisVal+1 < axisMax:
            cellRange.append(axisVal+1)
  
        return cellRange

    def printBoard(self):
        print(f'Generation {self.generation}')
        for i in range(self.xSize):
            print(self.board[i])
        print()


# define our main()
def main():
    myBoard = GOLBoard(7,7)
    myBoard.seedBoard()
    myBoard.printBoard()
    for i in range(10):
        myBoard.evolveBoard()
        myBoard.printBoard()


# Run main if we are the parnet file
if __name__ == '__main__':
    main()