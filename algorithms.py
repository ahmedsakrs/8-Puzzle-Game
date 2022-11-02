import time
from math import sqrt
import heapq


def getPath(parent_map: dict) -> list[int]:
    # array containing final path to goal state
    path = []
    # assuming this function is called only when reached goal state, so we will start with it
    child = 12345678
    # loop until we find start state
    while True:
        path.append(child)
        parent = parent_map[child]
        # if we find start state we reverse the array, so it is ordered from state to goal
        if parent == child:
            path.reverse()
            return path

        child = parent


def isGoal(state: int) -> bool:
    if state == 12345678:
        return True
    else:
        return False


def getChildren(state: int) -> list[int]:
    state = str(state)
    if len(state) == 8:
        state = '0' + state

    state = list(state)
    children = []

    index = state.index('0')

    row = index // 3
    col = index % 3

    if row > 0:
        child = state.copy()
        child[row * 3 + col], child[(row - 1) * 3 + col] = child[(row - 1) * 3 + col], child[row * 3 + col]
        children.append(int(''.join(child)))

    if row < 2:
        child = state.copy()
        child[row * 3 + col], child[(row + 1) * 3 + col] = child[(row + 1) * 3 + col], child[row * 3 + col]
        children.append(int(''.join(child)))

    if col > 0:
        child = state.copy()
        child[row * 3 + col], child[row * 3 + col - 1] = child[row * 3 + col - 1], child[row * 3 + col]
        children.append(int(''.join(child)))

    if col < 2:
        child = state.copy()
        child[row * 3 + col], child[row * 3 + col + 1] = child[row * 3 + col + 1], child[row * 3 + col]
        children.append(int(''.join(child)))

    return children


def BFS(start_state: int):
    # start max depth
    max_depth = 0
    # set found with false
    found = False
    # frontier queue with start state inserted
    frontier = [[start_state, 0]]  # what is 0 parameter?
    # frontier set
    frontier_set = set()
    # add start into frontier set
    frontier_set.add(start_state)
    # explored set
    explored = set()
    # parent map initialized with start state
    parent_map = {start_state: start_state}
    # initialize time
    start_time = time.time()

    # loop while frontier is not empty
    while frontier:
        # get first state in queue
        state = frontier.pop(0)
        # remove state from frontier set
        frontier_set.remove(state[0])
        # add state to explored
        explored.add(state[0])
        # find max depth: max of new state's depth and current max depth
        max_depth = max(max_depth, state[1])

        # if goal state is reached break
        if isGoal(state[0]):
            found = True
            break
        # get all children of new state
        for child in getChildren(state[0]):
            # check if child is not in frontier and explored
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
    index = state.index(variable)
    if index == 0 or index == 3 or index == 6:
        return 1
    if index == 1 or index == 4 or index == 7:
        return 2
    if index == 2 or index == 5 or index == 8:
        return 3


def getY(state: str, variable: str) -> int:
    index = state.index(variable)
    if index == 0 or index == 1 or index == 2:
        return 3
    if index == 3 or index == 4 or index == 5:
        return 2
    if index == 6 or index == 7 or index == 8:
        return 1


def heuristicManhattan(state: int) -> int:
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


def heuristicEuclidean(state: int) -> float:
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


def A(start_state: int, flag: int):
    max_depth = 0
    found = False
    f = heuristicEuclidean(start_state) if flag == 1 else heuristicManhattan(start_state)
    h = f
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


def DFS(start_state: int):
    max_depth = 0
    found = False

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
