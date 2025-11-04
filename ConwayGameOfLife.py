import random


class ConwayGameOfLife:
    def __init__(self):
        pass

    def create_grid(self, g1, g2):
        arrays = []
        for x in range(g1):
            array2 = []
            for y in range(g2):
                array2.append(random.randint(0, 1))
            arrays.append(array2)
        return (arrays)

    def format_grid(self, grid):
        string1 = ''
        for x in grid:
            for y in x:
                string1 += '#' if y == 1 else '.'
                string1 += ' '
            string1 = string1.strip()
            string1 += '\n'
        return (string1)

    def count_neighbors(self, grids, rows, column):
        if rows >= len(grids) or column >= len(grids[0]) or rows < 0 or column < 0:
            return print("Please type a valid position")
        counter = 0
        el = rows
        elc = column
        if rows == 0:
            el = 1
        if column == 0:
            elc = 1
        for row in range(el - 1, rows + 2):
            for col in range(elc - 1, column + 2):
                try:
                    if grids[row][col] == 1:
                        counter += 1
                except IndexError:
                    counter += 0
        if grids[rows][column] == 1:
            counter -= 1
        return counter

    def update_grid(self, grid):
        new_grid2 = []
        grid2_format2 = []
        for row in range(len(grid)):
            new_grid1 = []
            grid2_format1 = []
            for column in range(len(grid[0])):
                cell = grid[row][column]
                value = self.count_neighbors(grid, row, column)
                if cell == 0:
                    if value == 3:
                        new_grid1.append('#')
                        grid2_format1.append(1)
                    else:
                        new_grid1.append('.')
                        grid2_format1.append(0)
                elif cell == 1:
                    if value < 2 or value > 3:
                        new_grid1.append('.')
                        grid2_format1.append(0)
                    else:
                        new_grid1.append('#')
                        grid2_format1.append(1)
            new_grid2.append(new_grid1)
            grid2_format2.append(grid2_format1)
        return grid2_format2







