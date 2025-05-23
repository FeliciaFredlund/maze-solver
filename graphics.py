'''
Module to handle graphics of the maze solver
'''

from tkinter import Tk, BOTH, Canvas

class Point():
    def __init__(self, x=0, y=0):
        '''Holds an x and y value for points in the window. Default is 0 for x and y.'''
        self.x = x
        self.y = y


class Line():
    def __init__(self, start: Point, end: Point):
        '''Line is created by having two points. Start and end denotes each end of the line.'''
        self.start = start
        self.end = end

    def draw(self, canvas: Canvas, fill_color: str):
        '''Draws the line'''
        canvas.create_line(
            self.start.x, self.start.y,
            self.end.x, self.end.y,
            fill=fill_color, width=2
        )


class Window():
    def __init__(self, width, height):
        '''
        Creates a tkinter window for the program.
        '''

        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)

        self.__running = False

    def redraw(self):
        '''This updates and draws the window.'''
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line: Line, fill_color: str):
        '''Uses Line.draw() to draw a line'''
        line.draw(self.__canvas, fill_color)

    def wait_for_close(self):
        '''This is the running loop of the window.'''
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        '''Method for closing the window.'''
        self.__running = False
