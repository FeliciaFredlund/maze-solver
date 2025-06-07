'''
Module to handle the maze.
'''

from graphics import Window
from cell import Cell
import time, random

class Maze():
    def __init__(
            self, 
            x1: int, y1: int, 
            num_rows: int, num_cols: int, 
            cell_size_x: int, cell_size_y: int, 
            win: Window = None,
            seed: int = None
        ):
        '''Initiates the basic settings for the maze'''
        
        self.__x1 = x1
        self.__y1 = y1
        
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        
        self.__win = win

        if seed is not None:
            random.seed(seed)

        # List of lists of cells, first list is columns, second is rows
        # self.__cells[0][0] is top left
        # self.__cells[1][0] is the one to the right of [0][0]
        # self.__cells[0][1] is the one below [0][0]
        self.__cells = [] 
        
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

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

    def __break_walls_r(self, col_index, row_index):
        current_cell = self.__cells[col_index][row_index]
        current_cell.visited = True

        while True:
            to_be_visited = []
            if col_index - 1 >= 0 and not self.__cells[col_index - 1][row_index].visited:
                to_be_visited.append(("left", col_index - 1, row_index))
            if col_index + 1 < self.__num_cols and not self.__cells[col_index + 1][row_index].visited:
                to_be_visited.append(("right", col_index + 1, row_index))
            if row_index - 1 >= 0 and not self.__cells[col_index][row_index - 1].visited:
                to_be_visited.append(("above", col_index, row_index - 1))
            if row_index + 1 < self.__num_rows and not self.__cells[col_index][row_index + 1].visited:
                to_be_visited.append(("below", col_index, row_index + 1))
            
            if len(to_be_visited) == 0:
                self.__draw_cell(col_index, row_index)
                return

            direction, new_cell_col_index, new_cell_row_index = to_be_visited[random.randrange(len(to_be_visited))]             
            
            match direction:
                case "left":
                    current_cell.has_left_wall = False
                    self.__cells[new_cell_col_index][new_cell_row_index].has_right_wall = False
                case "right":
                    current_cell.has_right_wall = False
                    self.__cells[new_cell_col_index][new_cell_row_index].has_left_wall = False
                case "above":
                    current_cell.has_top_wall = False
                    self.__cells[new_cell_col_index][new_cell_row_index].has_bottom_wall = False
                case "below":
                    current_cell.has_bottom_wall = False
                    self.__cells[new_cell_col_index][new_cell_row_index].has_top_wall = False

            self.__break_walls_r(new_cell_col_index, new_cell_row_index)

    def __reset_cells_visited(self):
        for column in self.__cells:
            for cell in column:
                cell.visited = False

    def solve(self):
        return self.__solve_r(0, 0)

    def __solve_r(self, col_index, row_index):
        self.__animate()

        current_cell = self.__cells[col_index][row_index]
        current_cell.visited = True

        if col_index == self.__num_cols - 1 and row_index == self.__num_rows - 1:
            return True
        
        directions = []
        if col_index - 1 >= 0 and not current_cell.has_left_wall  and not self.__cells[col_index - 1][row_index].visited:
            directions.append((col_index - 1, row_index))
        if col_index + 1 < self.__num_cols and not current_cell.has_right_wall  and not self.__cells[col_index + 1][row_index].visited:
            directions.append((col_index + 1, row_index))
        if row_index - 1 >= 0 and not current_cell.has_top_wall  and not self.__cells[col_index][row_index - 1].visited:
            directions.append((col_index, row_index - 1)) 
        if row_index + 1 < self.__num_rows and not current_cell.has_bottom_wall  and not self.__cells[col_index][row_index + 1].visited:
            directions.append((col_index, row_index + 1))
        
        for direction in directions:
            new_cell_col_index = direction[0]
            new_cell_row_index = direction[1]
            new_cell = self.__cells[new_cell_col_index][new_cell_row_index]
            
            current_cell.draw_move(new_cell)

            true_path = self.__solve_r(new_cell_col_index, new_cell_row_index)

            if true_path:
                return true_path
            else:
                current_cell.draw_move(new_cell, True)
        
        return False