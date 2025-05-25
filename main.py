'''
This is a program that will draw a maze and the solve it,
while showing the wrong paths it took.
'''

from graphics import Window
from maze import Maze

def main():    
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600


    win = Window(screen_x, screen_y)

    maze = Maze(
        margin, margin, 
        num_rows, num_cols,
        (screen_x - 2 * margin) // num_cols,
        (screen_y - 2 * margin) // num_rows,
        win
        )
    
    win.wait_for_close()

if __name__ == "__main__":
    main()