'''
This is a program that will draw a maze and the solve it,
while showing the wrong paths it took.
'''

from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    

    line = Line(Point(10, 10), Point(50, 50))
    win.draw_line(line, "black")
    line = Line(Point(500, 80), Point(80, 500))
    win.draw_line(line, "red")
    
    win.wait_for_close()

if __name__ == "__main__":
    main()