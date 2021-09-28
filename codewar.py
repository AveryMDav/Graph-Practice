a = "\n".join([
    ".W...",
    ".W...",
    ".W.W.",
    "...W.",
    "...W."])


def path_finder(maze):
    maze_list = maze.split()
    X = 0
    Y = 0
    end_of_maze = len(maze) - 1
    current = (X, Y)

    while current != (5, 5):
        print(current)
        X += 1
        Y += 1
        current = (X, Y)

        if current == (5, 5):
            return print(current)

    return print(end_of_maze)


path_finder(a)
