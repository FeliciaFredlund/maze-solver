'''
Module to handle the "rooms", aka cells, of the maze
'''

from graphics import Window, Point, Line

class Cell():
    def __init__(self, window: Window):
        '''This makes up every square in maze.'''
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1

        self.__win = window

    def draw(self, x1=0, x2=0, y1=0, y2=0):
        '''Draws the cell depending on which walls are true.'''
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        
        point_top_left = Point(x1, y1)
        point_top_right = Point(x2, y1)
        point_bottom_left = Point(x1, y2)
        point_bottom_right = Point(x2, y2)

        if self.has_left_wall:       
            self.__win.draw_line(Line(point_top_left, point_bottom_left), "black")

        if self.has_right_wall:       
            self.__win.draw_line(Line(point_top_right, point_bottom_right), "black")

        if self.has_top_wall:       
            self.__win.draw_line(Line(point_top_left, point_top_right), "black")

        if self.has_bottom_wall:       
            self.__win.draw_line(Line(point_bottom_left, point_bottom_right), "black")