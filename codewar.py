import numpy as np

a = "\n".join([
    ".W...",
    ".W...",
    ".W.W.",
    "...W.",
    "...W.",
    "...W."])


# def path_finder(maze):
#     maze_list = maze.split()
#     end_of_maze = [(len(maze_list) - 1), (len(maze_list[len(maze_list) - 1]) - 1)]
#     current = [0, 0]
#
#     while current != end_of_maze:
#         visited = []
#         Y = current[0]
#         X = current[1]
#
#         while current[0] != len(maze_list) - 1:
#             if maze_list[X + 1][Y] == ".":
#                 print(current)
#                 Y += 1
#                 current = [X, Y]
#             elif maze_list[X + 1][Y] == ".":
#                 print(current)
#                 X += 1
#                 current = [X, Y]
#
#         return print("out of range")
#
#     return print(True)


def path_finder(maze, visited, current=0):
    goal = maze[len(maze) - 1]

    if visited[current] == 1:
        return False, print("maze impossible")

    if visited[current] == goal:
        return True, print(current, "goal")

    visited[current] = 1

    print("visit: ", current)

    if maze[current + 1] == ".":
        current = current + 1
        path_finder(maze, visited, current)
    elif maze[current - 6] == "." and visited[current - 6] != 1:
        current = current - 6
        path_finder(maze, visited, current)
    elif maze[current + 6] == ".":
        current = current + 6
        path_finder(maze, visited, current)
    else:

        return False, print("maze impossible")


visited_list = np.zeros(len(a))
path_finder(a, visited_list)
