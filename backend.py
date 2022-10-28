from frontend import Ui_MainWindow
from PyQt5 import QtWidgets
import random

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
    max_depth = 0
    found = False

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
                max_depth = max(max_depth, state[1] + 1)
                frontier_set.add(child)
                parent_map[child] = state[0]

    if not found:
        return False

    path = getPath(parent_map)
    cost = len(path)
    explored = len(explored)
    runtime = time.time() - start_time
    return path, cost, explored, max_depth, runtime


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

    if not found:
        return False

    path = getPath(parent_map)
    cost = len(path)
    explored = len(explored)
    runtime = time.time() - start_time
    return path, cost, explored, max_depth, runtime


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

        cost, explored, max_depth, runtime = 0, 0, 0, 0

        if self.ui.bfsRadio.isChecked():
            result = BFS(self.state)
            if not result:
                self.ui.pathFrame.hide()
                self.ui.prevButton.hide()
                self.ui.nextButton.hide()
                self.ui.costLabel.hide()
                self.ui.runtimeLabel.hide()
                self.ui.depthLabel.hide()
                self.ui.expandedLabel.hide()
                self.ui.costResult.hide()
                self.ui.runtimeResult.hide()
                self.ui.depthResult.hide()
                self.ui.expandedResult.hide()
                self.ui.progressLabel.setText('This State has no path to the goal')
                return
            self.path, cost, explored, max_depth, runtime = result

        elif self.ui.dfsRadio.isChecked():
            result = DFS(self.state)
            if not result:
                self.ui.progressLabel.setText('This State has no path to the goal')
                return
            self.path, cost, explored, max_depth, runtime = result

        elif self.ui.aRadio.isChecked():
            pass

        self.ui.expandedLabel.show()
        self.ui.depthLabel.show()
        self.ui.runtimeLabel.show()
        self.ui.pathFrame.show()
        self.ui.nextButton.show()
        self.ui.prevButton.show()
        self.ui.costLabel.show()

        self.ui.costResult.setText(str(cost))
        self.ui.expandedResult.setText(str(explored))
        self.ui.depthResult.setText(str(max_depth))
        self.ui.runtimeResult.setText(str(runtime))
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
        self.ui.solveButton.hide()
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
