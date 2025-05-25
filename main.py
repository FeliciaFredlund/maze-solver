'''
This is a program that will draw a maze and the solve it,
while showing the wrong paths it took.
'''

from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)
    
    a = Cell(win)
    a.draw(1, 51, 1, 51)

    a = Cell(win)
    a.has_bottom_wall = False
    a.draw(60, 110, 1, 51)

    a = Cell(win)
    a.has_top_wall = False
    a.draw(120, 170, 1, 51)

    a = Cell(win)
    a.has_left_wall = False
    a.draw(180, 230, 1, 51)

    a = Cell(win)
    a.has_right_wall = False
    a.draw(240, 290, 1, 51)
    
    win.wait_for_close()

if __name__ == "__main__":
    main()