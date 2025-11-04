import ConwayGameOfLife
import time
import os
game = ConwayGameOfLife.ConwayGameOfLife()


gridy = game.create_grid(int(input('How many rows?\n')), int(input('How many columns?\n')) )
loops = int(input('How many times will the simulation run?'))
print(game.format_grid(gridy))
time.sleep(0.5)
for x in range(loops):
    os.system('clear')
    new_grid = game.update_grid(gridy)
    print(game.format_grid(new_grid))
    gridy = new_grid
    time.sleep(0.5)