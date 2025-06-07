'''
Module to handle the "rooms", aka cells, of the maze
'''

from __future__ import annotations
# Above is so I can have type hinting in methods inside the class referring to the class

from graphics import Window, Point, Line

class Cell():
    def __init__(self, window: Window = None, x1=-1, y1=-1, x2=-1, y2=-1):
        '''This makes up every square in maze.'''
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        self.__win = window

    def draw(self):
        '''Draws the cell depending on which walls are true.'''        
        if self.__win is None:
            return
        
        point_top_left = Point(self.__x1, self.__y1)
        point_top_right = Point(self.__x2, self.__y1)
        point_bottom_left = Point(self.__x1, self.__y2)
        point_bottom_right = Point(self.__x2, self.__y2)

        # Left wall
        color = "black" if self.has_left_wall else "white"       
        self.__win.draw_line(Line(point_top_left, point_bottom_left), color)

        # Right wall
        color = "black" if self.has_right_wall else "white"       
        self.__win.draw_line(Line(point_top_right, point_bottom_right), color)

        # Top wall
        color = "black" if self.has_top_wall else "white"       
        self.__win.draw_line(Line(point_top_left, point_top_right), color)

        # Bottom wall
        color = "black" if self.has_bottom_wall else "white"       
        self.__win.draw_line(Line(point_bottom_left, point_bottom_right), color)
            
    def draw_move(self, to_cell: Cell, undo=False):
        '''Draws a line between the centers of two cells'''
        color = "red" if not undo else "gray"

        center = Point(
            abs(self.__x2 - self.__x1) // 2 + self.__x1,
            abs(self.__y2 - self.__y1) // 2 + self.__y1
        )

        to_cell_center = Point(
            abs(to_cell.__x2 - to_cell.__x1) // 2 + to_cell.__x1,
            abs(to_cell.__y2 - to_cell.__y1) // 2 + to_cell.__y1
        )

        if self.__win is not None:
            self.__win.draw_line(Line(center, to_cell_center), color)