'''
This is a program that will draw a maze and the solve it,
while showing the wrong paths it took.
'''

from graphics import Window
from maze import Maze
import time

def main():    
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) // num_cols
    cell_size_y = (screen_y - 2 * margin) // num_rows


    win = Window(screen_x, screen_y)

    maze = Maze(
        margin, margin, 
        num_rows, num_cols,
        cell_size_x,
        cell_size_y,
        win,
        )
    
    time.sleep(2.5)

    is_solvable = maze.solve()

    if not is_solvable:
        print("Sorry! Maze was unsolvable.")
    
    win.wait_for_close()

if __name__ == "__main__":
    main()