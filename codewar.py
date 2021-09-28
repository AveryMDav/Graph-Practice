a = "\n".join([
    ".W...",
    ".W...",
    ".W.W.",
    "...W.",
    "...W.",
    "...W."])


def path_finder(maze):
    maze_list = maze.split()
    end_of_maze = [(len(maze_list) - 1), (len(maze_list[len(maze_list) - 1]) - 1)]
    current = [0, 0]

    while current != end_of_maze:
        visited = []
        Y = current[0]
        X = current[1]

        while current[0] != len(maze_list) - 1:
            if maze_list[X + 1][Y] == ".":
                print(current)
                Y += 1
                current = [X, Y]
            elif maze_list[X + 1][Y] == ".":
                print(current)
                X += 1
                current = [X, Y]

        return print("out of range")

    return print(True)


path_finder(a)
