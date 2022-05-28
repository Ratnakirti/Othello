NUMBER_OF_SQUARES = 8
SQUARE = 50
CIRCLE_RADIUS = 20
WHITE_TILE = "White"
BLACK_TILE = "Black"
EMPTY_TILE = "Empty"

from model import *

class Controller:
    """
    Class Controller -- It is the controller part of Othello matrix
    """
    def __init__(self, decider):
        """
        Constructor -- Creates a new instance of the OthelloMatrix class
        Parameters --
            self -- the current object
            decider -- an object of the model class
        Attributes --
            decider -- an object of the model class
        Methods --
            get_click(), convert_click_to_row_column(), check_row_column_in_range()
            report_decider()
        """
        if not isinstance(decider, Decider):
            raise TypeError("The parameter must be object of Decider class")
        
        self.decider = decider

    def get_click(self, x, y):
        """
        Method -- to receive the x and y coordinates from the onclick
        Parameters --
            x -- It is the x coordinate
            y -- It is the y coordinate
        """
        if not isinstance(x, int) and not isinstance(x, float):
            raise TypeError("The x coordinate should be int or float")
        if not isinstance(y, int) and not isinstance(y, float):
            raise TypeError("The y coordinate should be int or float")
        
        row, column = self.convert_click_to_row_column(x, y)
        if row in range(NUMBER_OF_SQUARES) and column in range(NUMBER_OF_SQUARES):
            self.decider.get_move(row, column)

    def convert_click_to_row_column(self, x, y):
        """
        Method -- to convert x and y coordinates to row and column
        Parameters --
            x -- It is the x coordinate
            y -- It is the y coordinate
        """
        if not isinstance(x, int) and not isinstance(x, float):
            raise TypeError("The x coordinate should be int or float")
        if not isinstance(y, int) and not isinstance(y, float):
            raise TypeError("The y coordinate should be int or float")
        
        row = int(x//SQUARE + NUMBER_OF_SQUARES/2)
        column = int(y//SQUARE + NUMBER_OF_SQUARES/2)
        return column, row

    def __str__(self):
        """
        Method -- returns a string that represents the Controller
        Parameters: self -- the current object
        """
        return "This is the Controller class running"

    def __eq__(self, other):
        """
        Method -- compares the value of two Controller classes
        Parameters: 
            self -- the current object
            other -- the other Controller to compare with
        """
        return self.decider == other.decider
