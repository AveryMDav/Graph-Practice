import numpy as np

a = "\n".join([
    ".W...",
    ".W...",
    ".W.W.",
    "...W.",
    "...WW",
    "...W."])


def path_finder(maze, visited, current=0):
    goal = len(maze) - 1

    if visited[current] == 1:
        return False

    if current == goal:
        return True

    visited[current] = 1

    if maze[current + 1] == ".":
        if path_finder(maze, visited, current + 1):
            return True

    if maze[current - 6] == "." and current > 5:
        if path_finder(maze, visited, current - (maze.index("\n") + 1)):
            return True

    if maze[current + 6] == "." and current < (len(maze) - (maze.index("\n") + 1)):
        if path_finder(maze, visited, current + (maze.index("\n") + 1)):
            return True

    if maze[current - 1] == "." and current != 0:
        if path_finder(maze, visited, current - 1):
            return True

    return False


visited_list = np.zeros(len(a))
path_finder(a, visited_list)
