"""
Class Position
"""


class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setPosition(self, x, y):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.
        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        new_x = x
        new_y = y
        return Position(new_x, new_y)
    
    def get_manhattan_distance(position1, position2):
        """ 
        Return the manhattan distance between points p and q
        assuming both to have the same number of dimensions
        """
        p = [position1.getX(), position1.getY()]
        q = [position2.getX(), position2.getY()]
        # sum of absolute difference between coordinates
        distance = 0
        for p_i,q_i in zip(p,q):
            distance += abs(p_i - q_i)

        return distance

    def __eq__(self, obj):
        return obj.getX() == self.x and obj.getY() == self.y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    
