"""
A* Algorithm
"""
from Classes.Position import Position
from SearchAlgorithms.InformedSearch.Avara import Avara


class AStar(Avara):
    def __init__(self, robot, firstShip, secondShip, items, oils, obstacles, mainMaze):
        super().__init__(robot, firstShip, secondShip, items, oils, obstacles, mainMaze)

    #Override, main algorithm
    # The only line that I change here is the sorting of the slack before getting the current node with pop. Here I use the heuristic for sorting
    def getItems(self, initialNode):
        stack = []
        stack.append(initialNode)
        temp_First_goal = self.first_Goal
        temp_Second_goal = self.second_Goal
        while len(stack) != 0:
            stack.sort(key=lambda node: node.getHeuristic(self.first_Goal, self.second_Goal)) # CHANGE HERE COMPARED TO SUPER -> I sort by Heuristic (cost + manhattan), to get always the one with minor value(f = g + h) possible
            currentNode = stack.pop(0)
            currentNode.analizeGoal(temp_First_goal, temp_Second_goal)

            if self.isAllItemsRecollected():
                return self.findPath(self.getItemsRecollected()[1]) # Gets the second element, because this is the final one. The first one [0] is the path to the first item founded

            if currentNode.getIsGoal():
                print("Found one Item", currentNode, "\n")
                #self.setDepth(currentNode.getDepth() + self.getDepth())
                print("Path: ", self.findPath(currentNode), "\n")
                self.itemsRecollected.append(currentNode)
                stack = []  # Clean stack
                stack.append(currentNode)  # Add current Node as root
                # Set the position of the found item, because the robot already grabbed the item, so this node is not longer a goal
                # I set them to (99,99), to no to interfer with the analizeGoal method
                if temp_Second_goal in self.getPositionItemsRecollected():
                    temp_Second_goal = Position(99, 99)
                elif temp_First_goal in self.getPositionItemsRecollected():
                    temp_First_goal = Position(99, 99)

            else:
                self.analizeMove(currentNode)
                stack.extend(currentNode.getChildren())
