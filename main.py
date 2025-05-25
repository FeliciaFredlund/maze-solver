'''
This is a program that will draw a maze and the solve it,
while showing the wrong paths it took.
'''

from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)
    
    c1 = Cell(win, 50, 50, 100, 100)
    c1.has_right_wall = False
    c1.draw()

    c2 = Cell(win, 100, 50, 150, 100)
    c2.has_left_wall = False
    c2.has_bottom_wall = False
    c2.draw()

    c1.draw_move(c2)

    c3 = Cell(win, 100, 100, 150, 150)
    c3.has_top_wall = False
    c3.has_right_wall = False
    c3.draw()

    c2.draw_move(c3)

    c4 = Cell(win, 150, 100, 200, 150)
    c4.has_left_wall = False
    c4.draw()

    c3.draw_move(c4, True)

    
    win.wait_for_close()

if __name__ == "__main__":
    main()