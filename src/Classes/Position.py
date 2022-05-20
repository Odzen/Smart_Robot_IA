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

    
    def __eq__(self, obj):
        return isinstance(obj, Position) and obj.getX() == self.x and obj.getY() == self.y

    def __str__(self):  
        return  "(" + str(self.x) + "," +  str(self.y)  + ")"

