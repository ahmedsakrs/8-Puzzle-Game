from math import sqrt
import PyQt5
from frontend import Ui_MainWindow
from PyQt5 import QtWidgets
import random
import heapq
from PyQt5.QtCore import QPropertyAnimation
import time


def getPath(parent_map: dict) -> list[int]:
    # array containing final path to goal state
    path = []
    # assuming this function is called only when reached goal state so we will start with it
    child = 12345678
    # loop until we find start state
    while True:
        path.append(child)
        parent = parent_map[child]
        # if we find start state we reverse the array so it is ordered from state to goal
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
    # append a 0 to state in case the 0 bloack was at the beginning
    if len(state) == 8:
        state = '0' + state

    state = list(state)
    children = []
    # Get childs if 0 is in any block
    # if 0 block is in the middle-> 4 possible children
    if state[4] == '0':
        # copy initial state
        child = state.copy()
        # first possibility->exchange center block with its above block(index:4 with index:1)
        child[4], child[1] = child[1], child[4]
        # Turn child into integer
        child = int(''.join(child))
        # append child to children array
        children.append(child)
        # copy initial state
        child = state.copy()
        # second possibility->exchange center block with its below block(index:4 with index:1)
        child[4], child[7] = child[7], child[4]
        # Turn child into integer
        child = int(''.join(child))
        # append child to children array
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
        child[0], child[3] = child[3], child[0]
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
        child[6], child[3] = child[3], child[6]
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

    res = 0

    x1 = getX(state, '1')
    y1 = getY(state, '1')
    temp = abs(x1 - 2) + abs(y1 - 3)
    res = res + temp
    x2 = getX(state, '2')
    y2 = getY(state, '2')
    temp = abs(x2 - 3) + abs(y2 - 3)
    res = res + temp
    x3 = getX(state, '3')
    y3 = getY(state, '3')
    temp = abs(x3 - 1) + abs(y3 - 2)
    res = res + temp
    x4 = getX(state, '4')
    y4 = getY(state, '4')
    temp = abs(x4 - 2) + abs(y4 - 2)
    res = res + temp
    x5 = getX(state, '5')
    y5 = getY(state, '5')
    temp = abs(x5 - 3) + abs(y5 - 2)
    res = res + temp
    x6 = getX(state, '6')
    y6 = getY(state, '6')
    temp = abs(x6 - 1) + abs(y6 - 1)
    res = res + temp
    x7 = getX(state, '7')
    y7 = getY(state, '7')
    temp = abs(x7 - 2) + abs(y7 - 1)
    res = res + temp
    x8 = getX(state, '8')
    y8 = getY(state, '8')
    temp = abs(x8 - 3) + abs(y8 - 1)
    res = res + temp

    return res


def heuristicEuclidean(state: int) -> float:
    state = str(state)
    if len(state) == 8:
        state = '0' + state

    res = 0

    x1 = getX(state, '1')
    y1 = getY(state, '1')
    temp = sqrt(pow((x1 - 2), 2) + pow((y1 - 3), 2))
    res = res + temp
    x2 = getX(state, '2')
    y2 = getY(state, '2')
    temp = sqrt(pow((x2 - 3), 2) + pow((y2 - 3), 2))
    res = res + temp
    x3 = getX(state, '3')
    y3 = getY(state, '3')
    temp = sqrt(pow((x3 - 1), 2) + pow((y3 - 2), 2))
    res = res + temp
    x4 = getX(state, '4')
    y4 = getY(state, '4')
    temp = sqrt(pow((x4 - 2), 2) + pow((y4 - 2), 2))
    res = res + temp
    x5 = getX(state, '5')
    y5 = getY(state, '5')
    temp = sqrt(pow((x5 - 3), 2) + pow((y5 - 2), 2))
    res = res + temp
    x6 = getX(state, '6')
    y6 = getY(state, '6')
    temp = sqrt(pow((x6 - 1), 2) + pow((y6 - 1), 2))
    res = res + temp
    x7 = getX(state, '7')
    y7 = getY(state, '7')
    temp = sqrt(pow((x7 - 2), 2) + pow((y7 - 1), 2))
    res = res + temp
    x8 = getX(state, '8')
    y8 = getY(state, '8')
    temp = sqrt(pow((x8 - 3), 2) + pow((y8 - 1), 2))
    res = res + temp

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


class PuzzleSolver(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.state = None
        self.mode = None
        self.path = None
        self.i = 0

        self.ui.setupUi(self)
        self.ui.randomFrame.hide()
        self.ui.stateFrame.hide()
        self.ui.algorithmBox.hide()
        self.ui.heuristicGroup.hide()
        self.ui.solveButton.hide()
        self.ui.pathFrame.hide()
        self.ui.prevButton.hide()
        self.ui.nextButton.hide()
        self.ui.costLabel.hide()
        self.ui.runtimeLabel.hide()
        self.ui.depthLabel.hide()
        self.ui.expandedLabel.hide()

        self.ui.randomButton.clicked.connect(self.initialize_random)
        self.ui.stateButton.clicked.connect(self.get_input)

        self.ui.bfsRadio.clicked.connect(self.show_solve_hide_heuristic)
        self.ui.dfsRadio.clicked.connect(self.show_solve_hide_heuristic)
        self.ui.aRadio.clicked.connect(self.show_heuristic)

        self.ui.manhattanRadio.clicked.connect(self.show_solve)
        self.ui.euclideanRadio.clicked.connect(self.show_solve)

        self.ui.solveButton.clicked.connect(self.solve)
        self.ui.nextButton.clicked.connect(self.next)
        self.ui.prevButton.clicked.connect(self.prev)

    def next(self):
        self.i += 1
        self.ui.progressLabel.setText('State ' + str(self.i) + ' / ' + str(len(self.path) - 1))
        self.ui.prevButton.setEnabled(True)
        if self.i == len(self.path) - 1:
            self.ui.nextButton.setEnabled(False)
        self.display_path()

    def prev(self):
        self.i -= 1
        self.ui.progressLabel.setText('State ' + str(self.i) + ' / ' + str(len(self.path) - 1))
        self.ui.nextButton.setEnabled(True)
        if self.i == 0:
            self.ui.prevButton.setEnabled(False)
        self.display_path()

    def solve(self):
        self.i = 0
        if self.mode == 'input':
            valid = self.validate()
            if not valid:
                return

        self.ui.progressLabel.show()
        self.ui.nextButton.setEnabled(True)
        self.ui.prevButton.setEnabled(False)
        self.ui.expandedLabel.show()
        self.ui.depthLabel.show()
        self.ui.runtimeLabel.show()
        self.ui.runtimeResult.show()
        self.ui.depthResult.show()
        self.ui.expandedResult.show()

        result = None

        if self.ui.bfsRadio.isChecked():
            result = BFS(self.state)

        elif self.ui.dfsRadio.isChecked():
            result = DFS(self.state)

        elif self.ui.aRadio.isChecked():
            heuristic = 0 if self.ui.manhattanRadio.isChecked() else 1

            result = A(self.state, heuristic)
        if len(result) == 3:
            self.ui.pathFrame.hide()
            self.ui.prevButton.hide()
            self.ui.nextButton.hide()
            self.ui.costLabel.hide()
            self.ui.costResult.hide()
            self.ui.runtimeResult.setText(str(result[2]) + ' sec')
            self.ui.depthResult.setText(str(result[1]))
            self.ui.expandedResult.setText(str(result[0]))
            self.ui.progressLabel.setText('This State has no path to the goal')
            return
        self.path, cost, explored, max_depth, runtime = result

        self.ui.pathFrame.show()
        self.ui.nextButton.show()
        self.ui.prevButton.show()
        self.ui.costLabel.show()
        self.ui.costResult.show()

        self.ui.costResult.setText(str(cost))
        self.ui.expandedResult.setText(str(explored))
        self.ui.depthResult.setText(str(max_depth))
        self.ui.runtimeResult.setText(str(runtime) + ' sec')
        self.ui.progressLabel.setText('State ' + str(self.i) + ' / ' + str(len(self.path) - 1))

        self.display_path()

    def display_path(self):
        current = list(str(self.path[self.i]))
        if len(current) == 8:
            current.insert(0, '')
        else:
            i = current.index('0')
            current[i] = ''

        self.ui.result0.setText(current[0])
        self.ui.result1.setText(current[1])
        self.ui.result2.setText(current[2])
        self.ui.result3.setText(current[3])
        self.ui.result4.setText(current[4])
        self.ui.result5.setText(current[5])
        self.ui.result6.setText(current[6])
        self.ui.result7.setText(current[7])
        self.ui.result8.setText(current[8])

    def validate(self) -> bool:
        self.state = []
        self.state.append(self.ui.text0.text())
        self.state.append(self.ui.text1.text())
        self.state.append(self.ui.text2.text())
        self.state.append(self.ui.text3.text())
        self.state.append(self.ui.text4.text())
        self.state.append(self.ui.text5.text())
        self.state.append(self.ui.text6.text())
        self.state.append(self.ui.text7.text())
        self.state.append(self.ui.text8.text())

        valid = {'', '1', '2', '3', '4', '5', '6', '7', '8'}
        if valid - set(self.state) == set():
            index = self.state.index('')
            self.state[index] = '0'
            self.state = int(''.join(self.state))
            return True

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText('Insert all values 1 - 8\nLeave only one empty block')
        msg.setWindowTitle("Error")
        msg.exec_()
        return False

    def show_solve_hide_heuristic(self) -> None:
        self.ui.heuristicGroup.hide()
        self.ui.solveButton.show()

    def get_input(self) -> None:
        self.ui.algorithmBox.show()
        self.ui.randomFrame.hide()
        self.ui.stateFrame.show()
        self.mode = 'input'

    def show_solve(self) -> None:
        self.ui.solveButton.show()

    def show_heuristic(self) -> None:
        if not self.ui.euclideanRadio.isChecked() and not self.ui.manhattanRadio.isChecked():
            self.ui.solveButton.hide()
        else:
            self.ui.solveButton.show()
        self.ui.heuristicGroup.show()

    def initialize_random(self) -> None:
        self.ui.stateFrame.hide()
        self.ui.randomFrame.show()
        self.mode = 'random'

        self.state = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        random.shuffle(self.state)
        self.display_state()
        self.state = int(''.join(self.state))

        self.ui.algorithmBox.show()

    def swap(self, previous_state: int, next_state: int):
        previous_state = str(previous_state)
        next_state = str(next_state)

        if len(previous_state) == 8:
            previous_state = '0' + previous_state

        if len(next_state) == 8:
            next_state = '0' + next_state

        differences = []

        for i in range(9):
            if previous_state[i] != next_state[i]:
                differences.append(i)

        if 0 in differences and 1 in differences:
            self.anim = QPropertyAnimation(self.ui.result0, b'geometry')
            self.anim.setDuration(250)
            x0, y0, w0, h0 = self.ui.result0.geometry().x(), self.ui.result0.geometry().y(), self.ui.result0.geometry().width(), self.ui.result0.geometry().height()
            self.anim.setStartValue(self.ui.result0.geometry())
            self.anim.setEndValue(PyQt5.QtCore.QRect(x0 + 45, y0, w0, h0))

            self.anim2 = QPropertyAnimation(self.ui.result1, b'geometry')
            self.anim2.setDuration(250)
            x1, y1, w1, h1 = self.ui.result1.geometry().x(), self.ui.result1.geometry().y(), self.ui.result1.geometry().width(), self.ui.result1.geometry().height()
            self.anim2.setStartValue(self.ui.result1.geometry())
            self.anim2.setEndValue(PyQt5.QtCore.QRect(x1 - 45, y1, w1, h1))

            self.anim2.start()
            self.anim.start()

            val0 = self.ui.result0.text()
            val1 = self.ui.result1.text()

            self.ui.result0.setText(val1)
            self.ui.result1.setText(val0)

            self.anim = QPropertyAnimation(self.ui.result0, b'geometry')
            self.anim.setDuration(250)
            self.anim.setStartValue(self.ui.result0.geometry())
            self.anim.setEndValue(PyQt5.QtCore.QRect(x0, y0, w0, h0))

            self.anim2 = QPropertyAnimation(self.ui.result1, b'geometry')
            self.anim2.setDuration(250)
            self.anim2.setStartValue(self.ui.result1.geometry())
            self.anim2.setEndValue(PyQt5.QtCore.QRect(x1, y1, w1, h1))

            self.anim.start()
            self.anim2.start()

        if 1 in differences and 2 in differences:
            self.anim = QPropertyAnimation(self.ui.result1, b'geometry')
            self.anim.setDuration(500)
            self.anim.setStartValue(self.ui.result1.geometry())
            self.anim.setEndValue(self.ui.result2.geometry())

            self.anim2 = QPropertyAnimation(self.ui.result2, b'geometry')
            self.anim2.setDuration(500)
            self.anim2.setStartValue(self.ui.result2.geometry())
            self.anim2.setEndValue(self.ui.result1.geometry())

            self.anim2.start()
            self.anim.start()

            self.ui.result1.setObjectName("temp")
            self.ui.result2.setObjectName("result1")
            self.ui.temp.setObjectName('result2')

    def display_state(self) -> None:
        index = 0
        for i in range(len(self.state)):
            if self.state[i] == '0':
                self.state[i] = ''
                index = i
                break

        self.ui.label0.setText(self.state[0])
        self.ui.label1.setText(self.state[1])
        self.ui.label2.setText(self.state[2])
        self.ui.label3.setText(self.state[3])
        self.ui.label4.setText(self.state[4])
        self.ui.label5.setText(self.state[5])
        self.ui.label6.setText(self.state[6])
        self.ui.label7.setText(self.state[7])
        self.ui.label8.setText(self.state[8])

        self.state[index] = '0'


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    gui = PuzzleSolver()
    gui.show()
    sys.exit(app.exec())
