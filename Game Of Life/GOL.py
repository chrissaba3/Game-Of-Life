#Project:   Game Of Life Simulation
#Author:    Chris Saba
#Date:      12/06/2020
import os
from collections import namedtuple, defaultdict
import time
import random
Cell = namedtuple('Cell', ['x', 'y'])
clear = lambda: os.system("cls" if os.name == 'nt' else 'clear')

class BoundryError(Exception):
    pass

class GenerationError(Exception):
    pass

class GOL:
    def __init__(self, rows, columns, generations, cells, tickspeed):
        '''
        Game Of Life constructor initializes all the inputs into variables
        used by the GOL Class
        '''
        self._columns = columns
        self._rows = rows
        self._generations = generations
        self._cells = cells
        self._tickspeed = tickspeed
        self._board = self.generateBoard()

    def generateBoard(self):
        '''
        Intialize the first board, checks boundries for negative or invalid
        values, adds cells by 25% chance, and keeps adding until cell count
        is reached. if board is iterated before cell count is reached, it
        will repopulate until met.
        '''
        try:
            if(self._rows < 0 or self._columns < 0):
                raise BoundryError
        except BoundryError:
            print("Invalid Row or Column dimension, input must be positive.")
        board = set()
        cellcount = self._cells
        while cellcount > 0:
            for row in range(self._rows):
                for col in range(self._columns):
                    startpos = random.randint(0, 3)
                    if(cellcount < 1):
                        return board
                    if startpos == 1:
                        board.add(Cell(int(row), int(col)))
                        cellcount = cellcount - 1
        return board

    def getNeighbourCount(board, rows, cols):
        '''
        collects neighbors checked by getNeighbors
        adds them per cell to be determined whether
        a new cell is born or stays alive/dies.
        '''
        col = cols
        row = rows
        neighbour_counts = defaultdict(int)
        try:
            if(row > -1 or col > -1):
                pass
        except BoundryError:
            print("Invalid Row or Column dimension, input must be positive.")
        for cell in board:
            for neighbour in GOL.getNeighbours(cell, row, col):
                neighbour_counts[neighbour] += 1
        return neighbour_counts

    def generationAdvance(self):
        '''
        Handles the generation advancement as a driver
        takes variables and calculates time and count
        Callable function, not automatically ran.
        '''
        iteration = 1
        clear()
        try:
            if(self._generations < 1):
                raise GenerationError
        except GenerationError:
            print("Invalid number of generations, input must be positive.")
        print(GOL.boardToString(self._board, self._rows, self._columns))
        time.sleep(self._tickspeed)
        for i in range(self._generations):
            self._board = GOL.advanceBoard(
                self._board, self._rows, self._columns)
            clear()
            print(GOL.boardToString(self._board, self._rows, self._columns))
            print(f"Generation: {iteration}/{self._generations}")
            iteration += 1
            time.sleep(self._tickspeed)

    def getNeighbours(cell, row, col):
        '''
        finds neighbors in a search from depth -1 to +2
        input cell[x,y] find x+2,-1 y+2,-1
        returns cell if found, count is counted by
        getNeighbourCount
        '''
        for y in range(cell.y - 1, cell.y + 2):
            if(int(cell.y) > col or int(cell.y) < 0):
                return cell
            for x in range(cell.x - 1, cell.x + 2):
                if(int(cell.x) > row or int(cell.x) < 0):
                    return cell
                if (x, y) != (cell.x, cell.y):
                    yield Cell(x, y)

    def advanceBoard(board, row, col):
        '''
        Finds cells neighbour counts, applies
        Game Of Life rules, and enforces wall
        boundaries in the conditional, and if
        passed, will add a new cell to a new
        board.
        '''
        new_board = set()
        for cell, count in GOL.getNeighbourCount(board, row, col).items():
            new_board.add(cell) if (count == 3 and
                                    (cell.x > 0 and cell.x < row)
                                    and (cell.y > 0 and cell.y < col)
                                    or (cell in board and count == 2
                                        and ((cell.x > 0 and cell.x < row)
                                             and (cell.y > 0 and cell.y < col)
                                             ))) else new_board
        return new_board

    def boardToString(board, row, col):
        '''
        takes board and converts into string,
        bounds size by inputs, prints X for cell
        prints - for empty/dead cell. If cell is
        present in location, print cell in location
        '''
        board_str = ""
        for y in range(row):
            for x in range(col):
                if Cell(x, y) in board:
                    board_str += 'X '
                else:
                    board_str += '- '
            board_str += '\n'
        return board_str.strip()


if __name__ == '__main__':
    inputRow = int(input('how many rows? '))
    inputCol = int(input('how many columns? '))
    inputGen = int(input('how many Generations? '))
    inputCells = int(input('how many maximum cells to start with? '))
    tickSpeed = float(input('Enter tick speed between generations' +
                            ' (format is in seconds): '))
    golBoard = GOL(inputRow, inputCol, inputGen, inputCells, tickSpeed)
    golBoard.generationAdvance()
