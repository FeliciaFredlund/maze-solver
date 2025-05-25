'''
Module to handle the "rooms", aka cells, of the maze
'''

from graphics import Window, Point, Line

class Cell():
    def __init__(self, window: Window, x1=-1, x2=-1, y1=-1, y2=-1):
        '''This makes up every square in maze.'''
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        self.__win = window

    def draw(self):
        '''Draws the cell depending on which walls are true.'''        
        point_top_left = Point(self.__x1, self.__y1)
        point_top_right = Point(self.__x2, self.__y1)
        point_bottom_left = Point(self.__x1, self.__y2)
        point_bottom_right = Point(self.__x2, self.__y2)

        if self.has_left_wall:       
            self.__win.draw_line(Line(point_top_left, point_bottom_left), "black")

        if self.has_right_wall:       
            self.__win.draw_line(Line(point_top_right, point_bottom_right), "black")

        if self.has_top_wall:       
            self.__win.draw_line(Line(point_top_left, point_top_right), "black")

        if self.has_bottom_wall:       
            self.__win.draw_line(Line(point_bottom_left, point_bottom_right), "black")