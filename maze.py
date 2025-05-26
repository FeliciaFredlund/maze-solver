'''
Module to handle the maze.
'''

from graphics import Window
from cell import Cell
import time

class Maze():
    def __init__(
            self, 
            x1: int, y1: int, 
            num_rows: int, num_cols: int, 
            cell_size_x: int, cell_size_y: int, 
            win: Window = None
        ):
        '''Initiates the basic settings for the maze'''
        
        self.__x1 = x1
        self.__y1 = y1
        
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        
        self.__win = win

        # List of lists of cells, first list is columns, second is rows
        # self.__cells[0][0] is top left
        # self.__cells[1][0] is the one to the right of [0][0]
        # self.__cells[0][1] is the one below [0][0]
        self.__cells = [] 
        
        self.__create_cells()
        self.__break_entrance_and_exit()

    def __create_cells(self):
        '''Creates all the cells of the maze and draws them one after the other'''
        for col_index in range(self.__num_cols):
            self.__cells.append([])
            for row_index in range(self.__num_rows):
                top_left_x = self.__x1 + (col_index * self.__cell_size_x)
                top_left_y = self.__y1 + (row_index * self.__cell_size_y)
                cell = Cell(
                    self.__win,
                    top_left_x,
                    top_left_y,
                    top_left_x + self.__cell_size_x,
                    top_left_y + self.__cell_size_y
                )
                self.__cells[col_index].append(cell)

        for col_index in range(self.__num_cols):
            for row_index in range(self.__num_rows):        
                self.__draw_cell(col_index, row_index)

    def __draw_cell(self, col_index, row_index):
        '''Calls draw on a specific cell in the maze and then animate'''
        self.__cells[col_index][row_index].draw()
        self.__animate()

    def __animate(self):
        '''Calls Window.redraw() (the update and draw function of Window) and sleeps to achieve "animation"'''
        if self.__win is None:
            return

        self.__win.redraw()
        time.sleep(0.05)

    def __break_entrance_and_exit(self):
        '''Remove walls to create entrance and exit'''
        # Entrance
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)

        # Exit
        self.__cells[-1][-1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)