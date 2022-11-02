import time
from math import sqrt
import heapq


def getPath(parent_map: dict) -> list[int]:
    """
    :param parent_map: Contains each child state as a key and the value is its parent
    :return: The path from start state to goal state
    """

    path = []
    child = 12345678
    while True:
        path.append(child)
        parent = parent_map[child]
        # if we find start state we reverse the array, so it is ordered from state to goal
        if parent == child:
            # parent = child only when start state is reached
            path.reverse()
            return path

        child = parent


def isGoal(state: int) -> bool:
    if state == 12345678:
        return True
    else:
        return False


def getChildren(state: int) -> list[int]:
    """
    :param state: State in integer form
    :return: List of all possible children
    """
    state = str(state)
    if len(state) == 8:
        state = '0' + state

    state = list(state)
    children = []

    index = state.index('0')

    row = index // 3
    col = index % 3

    if row > 0:
        # if row > 0, 0 can be swapped with the upper row
        child = state.copy()
        child[row * 3 + col], child[(row - 1) * 3 + col] = child[(row - 1) * 3 + col], child[row * 3 + col]
        children.append(int(''.join(child)))

    if row < 2:
        # if row < 2, 0 can be swapped with the lower row
        child = state.copy()
        child[row * 3 + col], child[(row + 1) * 3 + col] = child[(row + 1) * 3 + col], child[row * 3 + col]
        children.append(int(''.join(child)))

    if col > 0:
        # if col > 0, 0 can be swapped with the previous column
        child = state.copy()
        child[row * 3 + col], child[row * 3 + col - 1] = child[row * 3 + col - 1], child[row * 3 + col]
        children.append(int(''.join(child)))

    if col < 2:
        # if col < 2, 0 can be swapped with the following column
        child = state.copy()
        child[row * 3 + col], child[row * 3 + col + 1] = child[row * 3 + col + 1], child[row * 3 + col]
        children.append(int(''.join(child)))

    return children


def BFS(start_state: int) -> tuple:
    """
    :param start_state: The start state of the puzzle
    :return: path, cost, explored, max_depth, runtime if there is a path, else returns explored, max_depth, runtime
    """
    max_depth = 0
    found = False

    # frontier queue with start state inserted
    # frontier queue is a list of lists
    # each list consists of the state and its depth in the search tree

    frontier = [[start_state, 0]]
    frontier_set = set()
    frontier_set.add(start_state)
    explored = set()
    parent_map = {start_state: start_state}
    start_time = time.time()

    while frontier:
        state = frontier.pop(0)
        frontier_set.remove(state[0])
        explored.add(state[0])
        max_depth = max(max_depth, state[1])

        if isGoal(state[0]):
            found = True
            break

        for child in getChildren(state[0]):
            if child not in frontier_set and child not in explored:
                frontier.append([child, state[1] + 1])
                frontier_set.add(child)
                parent_map[child] = state[0]

    runtime = round(time.time() - start_time, 3)
    explored = len(explored)
    if found:
        path = getPath(parent_map)
        cost = len(path) - 1
        return path, cost, explored, max_depth, runtime

    return explored, max_depth, runtime


def getX(state: str, variable: str) -> int:
    """
    :param state: The state in str form
    :param variable: The char aiming to get its X
    :return: X of variable in the state
    """
    index = state.index(variable)
    if index == 0 or index == 3 or index == 6:
        return 1
    if index == 1 or index == 4 or index == 7:
        return 2
    if index == 2 or index == 5 or index == 8:
        return 3


def getY(state: str, variable: str) -> int:
    """
    :param state: The state in str form
    :param variable: The char aiming to get its Y
    :return: Y of variable in the state
    """
    index = state.index(variable)
    if index == 0 or index == 1 or index == 2:
        return 3
    if index == 3 or index == 4 or index == 5:
        return 2
    if index == 6 or index == 7 or index == 8:
        return 1


def heuristicManhattan(state: int) -> int:
    """
    :param state: The state in int form
    :return: Manhattan Heuristic for the given state
    """
    state = str(state)
    if len(state) == 8:
        state = '0' + state

    x1 = getX(state, '1')
    y1 = getY(state, '1')
    res = abs(x1 - 2) + abs(y1 - 3)

    x2 = getX(state, '2')
    y2 = getY(state, '2')
    res += abs(x2 - 3) + abs(y2 - 3)

    x3 = getX(state, '3')
    y3 = getY(state, '3')
    res += abs(x3 - 1) + abs(y3 - 2)

    x4 = getX(state, '4')
    y4 = getY(state, '4')
    res += abs(x4 - 2) + abs(y4 - 2)

    x5 = getX(state, '5')
    y5 = getY(state, '5')
    res += abs(x5 - 3) + abs(y5 - 2)

    x6 = getX(state, '6')
    y6 = getY(state, '6')
    res += abs(x6 - 1) + abs(y6 - 1)

    x7 = getX(state, '7')
    y7 = getY(state, '7')
    res += abs(x7 - 2) + abs(y7 - 1)

    x8 = getX(state, '8')
    y8 = getY(state, '8')
    res += abs(x8 - 3) + abs(y8 - 1)

    return res


def heuristicEuclidean(state: int) -> int:
    """
    :param state: The state in int form
    :return: Integer Euclidean Heuristic for the given state
    """
    state = str(state)
    if len(state) == 8:
        state = '0' + state

    x1 = getX(state, '1')
    y1 = getY(state, '1')
    res = sqrt(pow((x1 - 2), 2) + pow((y1 - 3), 2))

    x2 = getX(state, '2')
    y2 = getY(state, '2')
    res += sqrt(pow((x2 - 3), 2) + pow((y2 - 3), 2))

    x3 = getX(state, '3')
    y3 = getY(state, '3')
    res += sqrt(pow((x3 - 1), 2) + pow((y3 - 2), 2))

    x4 = getX(state, '4')
    y4 = getY(state, '4')
    res += sqrt(pow((x4 - 2), 2) + pow((y4 - 2), 2))

    x5 = getX(state, '5')
    y5 = getY(state, '5')
    res += sqrt(pow((x5 - 3), 2) + pow((y5 - 2), 2))

    x6 = getX(state, '6')
    y6 = getY(state, '6')
    res += sqrt(pow((x6 - 1), 2) + pow((y6 - 1), 2))

    x7 = getX(state, '7')
    y7 = getY(state, '7')
    res += sqrt(pow((x7 - 2), 2) + pow((y7 - 1), 2))

    x8 = getX(state, '8')
    y8 = getY(state, '8')
    res += sqrt(pow((x8 - 3), 2) + pow((y8 - 1), 2))

    return int(res)


def A(start_state: int, flag: int) -> tuple:
    """
    :param start_state: Start state of the puzzle
    :param flag: 1 for Euclidean Heuristic | 0 for Manhattan Heuristic
    :return: path, cost, explored, max_depth, runtime if there is a path, else returns explored, max_depth, runtime
    """
    max_depth = 0
    found = False
    f = heuristicEuclidean(start_state) if flag == 1 else heuristicManhattan(start_state)
    h = f

    # frontier heap with start state inserted
    # frontier heap is a list of lists
    # each list consists of the state, its heuristic and (cost + heuristic)
    frontier = [[f, h, start_state]]
    frontier_map = {start_state: f}
    explored = set()
    parent_map = {start_state: start_state}
    start_time = time.time()

    while frontier:
        state = heapq.heappop(frontier)
        if state[2] in frontier_map:
            frontier_map.pop(state[2])
        explored.add(state[2])
        g = state[0] - state[1]
        max_depth = max(max_depth, g)

        if isGoal(state[2]):
            found = True
            break

        for child in getChildren(state[2]):
            if child not in frontier_map and child not in explored:
                h = heuristicEuclidean(child) if flag == 1 else heuristicManhattan(child)
                heapq.heappush(frontier, [h + g + 1, h, child])
                max_depth = max(max_depth, g + 1)
                frontier_map[child] = h + g
                parent_map[child] = state[2]

            elif child in frontier_map:
                h = heuristicEuclidean(child) if flag == 1 else heuristicManhattan(child)
                temp = frontier_map[child]
                if h + g < temp:
                    # if a smaller f was found, insert the state again in the frontier with the new f
                    # update the parent map with the new parent for the state
                    heapq.heappush(frontier, [h + g + 1, h, child])
                    max_depth = max(max_depth, g + 1)
                    frontier_map[child] = h + g
                    parent_map[child] = state[2]

    runtime = round(time.time() - start_time, 3)
    explored = len(explored)
    if found:
        path = getPath(parent_map)
        cost = len(path) - 1
        return path, cost, explored, max_depth, runtime

    return explored, max_depth, runtime


def DFS(start_state: int) -> tuple:
    """
    :param start_state: Start state of the puzzle
    :return: path, cost, explored, max_depth, runtime if there is a path, else returns explored, max_depth, runtime
    """
    max_depth = 0
    found = False

    # frontier stack with start state inserted
    # frontier stack is a list of lists
    # each list consists of the state and its depth

    frontier = [[start_state, 0]]
    frontier_set = set()
    frontier_set.add(start_state)
    explored = set()
    parent_map = {start_state: start_state}

    start_time = time.time()

    while frontier:
        state = frontier.pop()
        frontier_set.remove(state[0])
        explored.add(state[0])
        max_depth = max(max_depth, state[1])

        if isGoal(state[0]):
            found = True
            break

        for child in getChildren(state[0]):
            if child not in frontier_set and child not in explored:
                frontier.append([child, state[1] + 1])
                max_depth = max(max_depth, state[1] + 1)
                frontier_set.add(child)
                parent_map[child] = state[0]

    runtime = round(time.time() - start_time, 3)
    explored = len(explored)
    if found:
        path = getPath(parent_map)
        cost = len(path) - 1
        return path, cost, explored, max_depth, runtime

    return explored, max_depth, runtime
