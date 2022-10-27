import time


def getPath(parent_map: dict) -> list[int]:
    path = []
    child = 12345678
    while True:
        path.append(child)
        parent = parent_map[child]

        if parent == child:
            path.reverse()
            return path

        child = parent


def isGoal(state: int) -> bool:
    if state == 12345678:
        return True
    return False


def getChildren(state: int) -> list[int]:
    state = str(state)
    if len(state) == 8:
        state = '0' + state

    state = list(state)
    children = []

    if state[4] == '0':
        child = state.copy()
        child[4], child[1] = child[1], child[4]
        child = int(''.join(child))
        children.append(child)
        child = state.copy()
        child[4], child[7] = child[7], child[4]
        child = int(''.join(child))
        children.append(child)
        child = state.copy()
        child[4], child[3] = child[3], child[4]
        child = int(''.join(child))
        children.append(child)
        child = state.copy()
        child[4], child[5] = child[5], child[4]
        child = int(''.join(child))
        children.append(child)
        return children

    if state[0] == '0':
        child = state.copy()
        child[0], child[1] = child[1], child[0]
        child = int(''.join(child))
        children.append(child)
        child = state.copy()
        child[0], child[4] = child[4], child[0]
        child = int(''.join(child))
        children.append(child)
        return children

    if state[2] == '0':
        child = state.copy()
        child[2], child[1] = child[1], child[2]
        child = int(''.join(child))
        children.append(child)
        child = state.copy()
        child[2], child[5] = child[5], child[2]
        child = int(''.join(child))
        children.append(child)
        return children

    if state[6] == '0':
        child = state.copy()
        child[6], child[7] = child[7], child[6]
        child = int(''.join(child))
        children.append(child)
        child = state.copy()
        child[6], child[4] = child[4], child[6]
        child = int(''.join(child))
        children.append(child)
        return children

    if state[8] == '0':
        child = state.copy()
        child[8], child[7] = child[7], child[8]
        child = int(''.join(child))
        children.append(child)
        child = state.copy()
        child[8], child[5] = child[5], child[8]
        child = int(''.join(child))
        children.append(child)
        return children

    if state[1] == '0':
        child = state.copy()
        child[1], child[0] = child[0], child[1]
        child = int(''.join(child))
        children.append(child)
        child = state.copy()
        child[1], child[2] = child[2], child[1]
        child = int(''.join(child))
        children.append(child)
        child = state.copy()
        child[1], child[4] = child[4], child[1]
        child = int(''.join(child))
        children.append(child)
        return children

    if state[3] == '0':
        child = state.copy()
        child[3], child[0] = child[0], child[3]
        child = int(''.join(child))
        children.append(child)
        child = state.copy()
        child[3], child[4] = child[4], child[3]
        child = int(''.join(child))
        children.append(child)
        child = state.copy()
        child[3], child[6] = child[6], child[3]
        child = int(''.join(child))
        children.append(child)
        return children

    if state[5] == '0':
        child = state.copy()
        child[5], child[2] = child[2], child[5]
        child = int(''.join(child))
        children.append(child)
        child = state.copy()
        child[5], child[4] = child[4], child[5]
        child = int(''.join(child))
        children.append(child)
        child = state.copy()
        child[5], child[8] = child[8], child[5]
        child = int(''.join(child))
        children.append(child)
        return children

    if state[7] == '0':
        child = state.copy()
        child[7], child[6] = child[6], child[7]
        child = int(''.join(child))
        children.append(child)
        child = state.copy()
        child[7], child[8] = child[8], child[7]
        child = int(''.join(child))
        children.append(child)
        child = state.copy()
        child[7], child[4] = child[4], child[7]
        child = int(''.join(child))
        children.append(child)
        return children


def BFS(start_state: int) -> None:
    max_depth = 0
    found = False

    frontier = [[start_state, 0]]
    frontier_set = set()
    frontier_set.add(start_state)
    visited = set()
    parent_map = {start_state: start_state}

    start_time = time.time()

    while frontier:
        state = frontier.pop(0)
        frontier_set.remove(state[0])
        visited.add(state[0])
        max_depth = max(max_depth, state[1])

        if isGoal(state[0]):
            found = True
            break

        for child in getChildren(state[0]):
            if child not in frontier_set and child not in visited:
                frontier.append([child, state[1] + 1])
                frontier_set.add(child)
                parent_map[child] = state[0]

    path = getPath(parent_map)
    print(path)
    print(len(path))
    print(len(visited))
    print(time.time() - start_time)


def DFS(start_state: int) -> None:
    max_depth = 0
    found = False

    frontier = [[start_state, 0]]
    frontier_set = set()
    frontier_set.add(start_state)
    visited = set()
    parent_map = {start_state: start_state}

    start_time = time.time()

    while frontier:
        state = frontier.pop()
        frontier_set.remove(state[0])
        visited.add(state[0])
        max_depth = max(max_depth, state[1])

        if isGoal(state[0]):
            found = True
            break

        for child in getChildren(state[0]):
            if child not in frontier_set and child not in visited:
                frontier.append([child, state[1] + 1])
                frontier_set.add(child)
                parent_map[child] = state[0]

    path = getPath(parent_map)
    print(path)
    print(len(path))
    print(len(visited))
    print(time.time() - start_time)


DFS(123456708)
