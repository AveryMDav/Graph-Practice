import numpy as np

a = "\n".join([
    ".W...",
    ".W...",
    ".W.W.",
    "...W.",
    "...W.",
    "...W."])


def path_finder(maze, visited, current=0):
    goal = len(maze) - 1

    if visited[current] == 1:
        return False

    if current == goal:
        return True, print(current, "goal")

    visited[current] = 1

    if maze[current + 1] == ".":
        path_finder(maze, visited, current + 1)

    if maze[current - 6] == ".":
        path_finder(maze, visited, current - 6)

    if maze[current + 6] == ".":
        path_finder(maze, visited, current + 6)

    if maze[current - 1] == ".":
        path_finder(maze, visited, current - 1)


visited_list = np.zeros(len(a))
path_finder(a, visited_list)
