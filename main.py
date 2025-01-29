import random
import turtle

CELL_SIZE = 20
WIDTH, HEIGHT = 45, 45

COLORS = ["red", "blue", "green", "yellow", "cyan", "magenta", "gray", "orange", "purple", "pink", "brown", "lime"]

def generate_maze():
    # making a "blank" maze
    maze = [[1] * WIDTH for _ in range(HEIGHT)]

    # starting in the corner
    stack = [(1, 1)]
    
    # setting the corner to a path
    maze[1][1] = 0

    while stack:
        x, y = stack[-1]

        # all possible directions (2 instead of 1 for nice matrix)
        directions = [(2, 0), (0, 2), (-2, 0), (0, -2)]
        random.shuffle(directions)

        # neighbors that can accept the above directions
        valid_neighbors = []

        for dx, dy in directions:
            # getting the absolute coords from direction
            nx, ny = x + dx, y + dy

            # making sure its valid
            if 0 < nx < HEIGHT and 0 < ny < WIDTH and maze[nx][ny] == 1:
                valid_neighbors.append((nx, ny))

        if valid_neighbors:
            # getting a random valid neighbor (doesn't matter)
            nx, ny = random.choice(valid_neighbors)

            # finding the "wall" that is between the current cell and neighbor cell
            maze[x + (nx - x) // 2][y + (ny - y) // 2] = 0

            # setting neighbor to a path
            maze[nx][ny] = 0

            # moving to the valid neighbor
            stack.append((nx, ny))
        else:
            # backtracking and verifying all neighbors have been tested
            stack.pop()
 
    return maze


def draw_maze(maze):
    # initial startup
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-WIDTH * CELL_SIZE // 2, HEIGHT * CELL_SIZE // 2)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            if maze[y][x] == 1:
                turtle.goto(
                    -WIDTH * CELL_SIZE // 2 + x * CELL_SIZE, 
                    HEIGHT * CELL_SIZE // 2 - y * CELL_SIZE
                )
               
                turtle.pendown()
                turtle.begin_fill()

                for _ in range(4):
                    turtle.forward(CELL_SIZE)
                    turtle.right(90)

                turtle.end_fill()
                turtle.penup()


def navigate_maze(maze):
    # initial startup
    turtle.speed(0)
    turtle.hideturtle()
    turtle.pensize(CELL_SIZE // 4)
    turtle.color("red")
    turtle.penup()
    x, y = 1, 1
    turtle.goto(
        (-WIDTH * CELL_SIZE // 2 + x * CELL_SIZE) + (CELL_SIZE // 2),
        (HEIGHT * CELL_SIZE // 2 - y * CELL_SIZE) - (CELL_SIZE // 2)
    )
    
    direction = (1, 0)
    
    directions = {
        (1, 0): [(0, -1), (0, 1)],
        (0, -1): [(-1, 0), (1, 0)],
        (-1, 0): [(0, 1), (0, -1)],
        (0, 1): [(1, 0), (-1, 0)]
    }
    
    while True:
        possible_direction = directions[direction][0]
        ax, ay = x + possible_direction[0], y + possible_direction[1]
        
        if maze[ay][ax] == 0:
            direction = possible_direction
            turtle.left(90)
            turtle.color(random.choice(COLORS))
            turtle.pendown()
            turtle.forward(CELL_SIZE)
            x, y = ax, ay
        else:
            ax, ay = x + direction[0], y + direction[1]
            if maze[ay][ax] == 0:
                turtle.pendown()
                turtle.forward(CELL_SIZE)
                x, y = ax, ay
            else:
                direction = directions[direction][1]
                turtle.right(90)
                turtle.color(random.choice(COLORS))
    input()

maze = generate_maze()
draw_maze(maze)
navigate_maze(maze)

