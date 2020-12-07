#Project:   Game Of Life Simulation
#Author:    Chris Saba
#Class:     CS2520 Python for Programmers
#Professor: Dominick Atanasio
#Date:      12/06/2020
import GOL
import os
import time


class main:
    def main():
        inputrow = int(input('how many rows? '))
        inputcol = int(input('how many columns? '))
        inputgen = int(input('how many generations? '))
        inputcells = int(input('how many maximum cells to start with? '))
        tickspeed = float(input('enter tick speed between ' +
                                'generations (format is in seconds): '))
        golboard = GOL.GOL(inputrow, inputcol, inputgen, inputcells, tickspeed)
        golboard.generationAdvance()
    if __name__ == '__main__':
        main()
