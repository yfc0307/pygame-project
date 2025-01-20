import random

class Maze:
    def __init__(self, width, height):
        self.width = width #25
        self.height = height #21

    def create_grid(self):
        return [['WALL' for _ in range(self.width)] for _ in range(self.height)]

    def get_neighbors(self, grid, x, y):
        neighbors = []
        if x > 1 and grid[y][x - 2] == 'WALL':
            neighbors.append((x - 2, y))
        if x < len(grid[0]) - 2 and grid[y][x + 2] == 'WALL':
            neighbors.append((x + 2, y))
        if y > 1 and grid[y - 2][x] == 'WALL':
            neighbors.append((x, y - 2))
        if y < len(grid) - 2 and grid[y + 2][x] == 'WALL':
            neighbors.append((x, y + 2))
        return neighbors

    def generate_maze(self):
        grid = self.create_grid()
        stack = [(1, 1)]
        while stack:
            x, y = stack[-1]
            grid[y][x] = 'PATH'
            neighbors = self.get_neighbors(grid, x, y)
            if neighbors:
                nx, ny = random.choice(neighbors)
                if nx > x:
                    grid[y][x + 1] = 'PATH'
                elif nx < x:
                    grid[y][x - 1] = 'PATH'
                if ny > y:
                    grid[y + 1][x] = 'PATH'
                elif ny < y:
                    grid[y - 1][x] = 'PATH'
                stack.append((nx, ny))
            else:
                stack.pop()
        return grid

    #maze = generate_maze(25, 21)
    #print_maze(maze)
