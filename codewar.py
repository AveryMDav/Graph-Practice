import numpy as np

a = "\n".join([
    ".WWWW",
    "W.WWW",
    "WW.WW",
    "WWW.W",
    "WWWW."])


def path_finder(maze):
    visited_list = np.zeros(len(maze))
    return path_finder_helper(maze, visited_list)


def path_finder_helper(maze, visited, current=0):
    goal = len(maze) - 1

    if maze[0] == "W":
        return False

    if visited[current] == 1:
        return False

    if current == goal:
        return True

    visited[current] = 1

    if maze[current + 1] == ".":
        if path_finder_helper(maze, visited, current + 1):
            return True

    if current > 5 and maze[current - (maze.index("\n") + 1)] == ".":
        if path_finder_helper(maze, visited, current - (maze.index("\n") + 1)):
            return True

    if current <= (len(maze) - (maze.index("\n") + 1)) and maze[current + (maze.index("\n") + 1)] == ".":
        if path_finder_helper(maze, visited, current + (maze.index("\n") + 1)):
            return True

    if current != 0 and maze[current - 1] == ".":
        if path_finder_helper(maze, visited, current - 1):
            return True

    return False


print(path_finder(a))
