NUMBER_OF_SQUARES = 8
SQUARE = 50
CIRCLE_RADIUS = 20
WHITE_TILE = "White"
BLACK_TILE = "Black"
EMPTY_TILE = "Empty"

import turtle
from view import *

class OthelloModel:
    """
    Class OthelloModel -- Generates a matrix of Othello squares with empty tiles then places
    the 4 initial tiles at the centre
    """
    def __init__(self):
        """
        Constructor -- Creates a new instance of the OthelloModel class
        Parameters --
            self -- the current object
        Attributes --
            matrix -- An empty dictionary
            generate_matrix() -- Method as an intializer
        Methods --
            generate_matrix(), put_initial_tiles()
        """
        self.matrix = {}
        self.generate_matrix()

    def generate_matrix(self):
        """
        Method -- To generate a dictionary matrix and each value starting as EMPTY_TILE
        """
        for x in range(NUMBER_OF_SQUARES):
            for y in range(NUMBER_OF_SQUARES):
                self.matrix[(x,y)] = EMPTY_TILE
        self.put_initial_tiles()

    def put_initial_tiles(self):
        """
        Method -- To add the 4 tiles at the center of the matrix
        """
        for key in self.matrix.keys():
            if key[0] == (NUMBER_OF_SQUARES/2 - 1)and key[1] == (NUMBER_OF_SQUARES/2):
                self.matrix[key] = WHITE_TILE
            if key[0] == (NUMBER_OF_SQUARES/2)and key[1] == (NUMBER_OF_SQUARES/2 - 1):
                self.matrix[key] = WHITE_TILE

            if key[0] == (NUMBER_OF_SQUARES/2 - 1)and key[1] == (NUMBER_OF_SQUARES/2 - 1):
                self.matrix[key] = BLACK_TILE
            if key[0] == (NUMBER_OF_SQUARES/2)and key[1] == (NUMBER_OF_SQUARES/2):
                self.matrix[key] = BLACK_TILE

    def __str__(self):
        """
        Method -- returns a string that represents the OthelloModel class
        Parameters: self -- the current object
        """
        return "This is the OthelloModel class running"

    def __eq__(self, other):
        """
        Method -- compares the two OthelloModel classes
        Parameters: 
            self -- the current object
            other -- the other OthelloBoard to compare with
        """
        return self.put_initial_tiles() == other.put_initial_tiles()
    
class Player:
    """
    Class Player -- To change the value of the dictionary matrix based on player tile color
    """
    def __init__(self, tile_color):
        """
        Constructor -- Creates a new instance of the Player class
        Parameters --
            self -- the current object
            tile_color -- color of the tile to be played
        Attributes --
            tile_color -- color of the tile to be played
        Methods --
            make_move()
        """
        if tile_color != WHITE_TILE and tile_color != BLACK_TILE:
            raise ValueError("Tile must be white or black")
        
        self.tile_color = tile_color

    def make_move(self, matrix, row_position, column_position):
        """
        Method -- To add tile color to the row-column position
        Parameters --
            matrix -- the dictionary matrix
            row_position -- the row positional number
            column_position -- the column positional number
        """
        if not isinstance(row_position, int) or not isinstance(column_position, int):
            raise TypeError("The row and column parameters must be an integer")
        elif row_position not in range(NUMBER_OF_SQUARES) or column_position not in range(NUMBER_OF_SQUARES):
            raise ValueError("The row and column must be within 0-7")

        matrix.matrix[row_position, column_position] = self.tile_color

    def __str__(self):
        """
        Method -- returns a string that represents the Player class
        Parameters: self -- the current object
        """
        return "This is the Player class running of " + self.tile_color + " tile"

    def __eq__(self, other):
        """
        Method -- compares the two Player classes
        Parameters: 
            self -- the current object
            other -- the other Player to compare with
        """
        return self.tile_color == other.tile_color

class Decider:
    """
    Class Decider -- To decide the status of the game playing and validate a move
    """
    def __init__(self, othello_board):
        """
        Constructor -- Creates a new instance of the Decider class
        Parameters --
            self -- the current object
            othello_board -- the object from view class
        Attributes --
            othello_matrix -- the 8X8 othello board matrix
            player1 -- instance of Player class
            player2 -- instance of Player class
            current_turn -- current ongoing turn tile color
            next_turn -- next turn tile color
            othello_board -- the object from view class
            report_board_draw_initial_tiles() -- drawing the initial 4 tiles
        Methods --
            report_board_draw_initial_tiles(), update_board(), convert_to_x_y_coordinate(),
            get_move(), check_legal_move(), check_top(), check_top_right(), check_right(),
            check_bottom_right(), check_bottom(), check_bottom_left(), check_left(),
            check_top_left(), flip_tiles(), switch_turn(), computer(), get_empty_tiles(),
            get_highest_flip(), get_flip_count(), check_the_winner(), count_tiles(),
            report_board_declare_winner()
        """
        if not isinstance(othello_board, OthelloBoard):
            raise TypeError("Parameter passed must be an object of OthelloBoard class")

        self.othello_matrix = OthelloModel()                        #To prepare the initial board matrix

        self.player1 = Player(BLACK_TILE)                           #Creating two players and assigning color
        self.player2 = Player(WHITE_TILE)

        self.current_turn = self.player1                            #Assigning turns to first and second player
        self.next_turn = self.player2
        
        self.othello_board = othello_board
        self.report_board_draw_initial_tiles()                      #Deploy the 4 starting tiles

        print("Welcome to Othello!")
        print("The board row and column addresses vary from 0-7")
        print("\nThe game starts with Black's turn")

    def report_board_draw_initial_tiles(self):
        """
        Method -- To initiate the 4 starting tiles on the matrix
        """
        for key, value in self.othello_matrix.matrix.items():
            if value == WHITE_TILE:
                self.update_board(key[0], key[1], value)
            elif value == BLACK_TILE:
                self.update_board(key[0], key[1], value)

    def update_board(self, row, column, tile_color):
        """
        Method -- To draw the new tile entry on the matrix
        Parameters --
            row -- the square matrix row position
            column -- the square matrix column position
            tile_color -- color of the tile
        """
        if tile_color != WHITE_TILE and tile_color != BLACK_TILE:
            raise ValueError("Tile must be white or black")
        elif not isinstance(row, int) or not isinstance(column, int):
            raise TypeError("The row and column parameters must be an integer")
        elif row not in range(NUMBER_OF_SQUARES) or column not in range(NUMBER_OF_SQUARES):
            raise ValueError("Row and column values out of range")

        new_x, new_y = self.convert_to_x_y_coordinate(row, column)

        self.othello_board.get_instruction(new_x, new_y, tile_color)

    def convert_to_x_y_coordinate(self, row, column):
        """
        Method -- convert row and column position to x and y coordinates to draw tile
        Parameters --
            row -- the square matrix row position
            column -- the square matrix column position
        """
        if not isinstance(row, int) or not isinstance(column, int):
            raise TypeError("The row and column parameters must be an integer")
        elif row not in range(NUMBER_OF_SQUARES) or column not in range(NUMBER_OF_SQUARES):
            raise ValueError("Row and column values out of range")

        new_x = (column - 4) * SQUARE + (SQUARE/2)
        new_y = (row - 4) * SQUARE + (SQUARE - 2*CIRCLE_RADIUS)/2
        return new_x, new_y

    def get_move(self, row_position, column_position):
        """
        Method -- Getting the row and column coordinates from the controller
        Parameters --
            row_position -- the square matrix row position
            column_position -- the square matrix column position
        """
        if not isinstance(row_position, int) or not isinstance(column_position, int):
            raise TypeError("The row and column parameters must be an integer")
        elif row_position not in range(NUMBER_OF_SQUARES) or column_position not in range(NUMBER_OF_SQUARES):
            raise ValueError("Row and column values out of range")
        
        if self.othello_matrix.matrix[(row_position, column_position)] == EMPTY_TILE:
            self.row_position = row_position
            self.column_position = column_position
            self.tile_color = self.current_turn.tile_color

            self.mode = True                                                                        #Flip mode on
            if self.check_legal_move(self.row_position, self.column_position, self.mode):
                print("\nNow turn is for", self.next_turn.tile_color)
                self.current_turn.make_move(self.othello_matrix, row_position, column_position)
                self.update_board(row_position, column_position, self.tile_color)
                self.switch_turn()
                self.check_the_winner()

    def check_legal_move(self, row_position, column_position, mode):
        """
        Method -- This checks if the clicked position is legal. It will validate in 8 different directions based
                    on its square location. If centrally placed, then would be checked for 8 directions. If it is
                    an edge then in 5 directions. If it is a corner then 3 directions, etc.
        Parameters --
            row_position -- the square matrix row position
            column_position -- the square matrix column position
            mode -- it is the flip switch, if it is True, then while checking for legal moves it will start flipping
                    tiles, else if it is False, then it would not flip tiles while validating for legality.
        """
        if not isinstance(row_position, int) or not isinstance(column_position, int):
            raise TypeError("The row and column parameters must be an integer")
        elif row_position not in range(NUMBER_OF_SQUARES) or column_position not in range(NUMBER_OF_SQUARES):
            raise ValueError("Row and column values out of range")
        elif not isinstance(mode, bool):
            raise TypeError("The flip mode must be of Boolean type")
        
        if row_position in range(1, 7) and column_position in range (1, 7):
            if any([self.check_top(row_position, column_position), self.check_top_right(row_position, column_position), \
            self.check_right(row_position, column_position), self.check_bottom_right(row_position, column_position), \
            self.check_bottom(row_position, column_position), self.check_bottom_left(row_position, column_position), \
            self.check_left(row_position, column_position), self.check_top_left(row_position, column_position)]):
                return True
            else:
                return False
            
        elif row_position in range(1, 7) and column_position == 0:
            if any([self.check_top(row_position, column_position), self.check_top_right(row_position, column_position), \
            self.check_right(row_position, column_position), self.check_bottom_right(row_position, column_position), \
            self.check_bottom(row_position, column_position)]):
                return True
            else:
                return False

        elif row_position in range(1, 7) and column_position == 7:
            if any([self.check_top(row_position, column_position), self.check_bottom(row_position, column_position), \
            self.check_bottom_left(row_position, column_position), self.check_left(row_position, column_position), \
            self.check_top_left(row_position, column_position)]):
                return True
            else:
                return False

        elif row_position == 0 and column_position in range (1, 7):
            if any([self.check_top(row_position, column_position), self.check_top_right(row_position, column_position), \
            self.check_right(row_position, column_position), self.check_left(row_position, column_position), \
            self.check_top_left(row_position, column_position)]):
                return True
            else:
                return False

        elif row_position == 7 and column_position in range (1, 7):
            if any([self.check_right(row_position, column_position), self.check_bottom_right(row_position, column_position), \
            self.check_bottom(row_position, column_position), self.check_bottom_left(row_position, column_position), \
            self.check_left(row_position, column_position)]):
                return True
            else:
                return False

        elif row_position == 0 and column_position == 0:
            if any([self.check_top(row_position, column_position), self.check_top_right(row_position, column_position), \
            self.check_right(row_position, column_position)]):
                return True
            else:
                return False

        elif row_position == 0 and column_position == 7:
            if any([self.check_top(row_position, column_position), self.check_left(row_position, column_position), \
            self.check_top_left(row_position, column_position)]):
                return True
            else:
                return False

        elif row_position == 7 and column_position == 7:
            if any([self.check_left(row_position, column_position), self.check_bottom_left(row_position, column_position), \
            self.check_bottom(row_position, column_position)]):
                return True
            else:
                return False

        elif row_position == 7 and column_position == 0:
            if any([self.check_right(row_position, column_position), self.check_bottom_right(row_position, column_position), \
            self.check_bottom(row_position, column_position)]):
                return True
            else:
                return False

    def check_top(self, row_position, column_position):
        """
        Method -- This checks in the top direction and keeps on iterating with (row+1) movement. Once it hits the
                    current turn color, it calls the flip function and passes the flip_list as parameter then returns
                    True as a legal position in top directional check. If flip switch is off, i.e. mode is False,
                    then it will only return the list of valid flip_list tiles if it is a legal position.
        Parameters --
            row_position -- the square matrix row position
            column_position -- the square matrix column position
        """
        if not isinstance(row_position, int) or not isinstance(column_position, int):
            raise TypeError("The row and column parameters must be an integer")
        elif row_position not in range(NUMBER_OF_SQUARES) or column_position not in range(NUMBER_OF_SQUARES):
            raise ValueError("Row and column values out of range")

        flip_list = []
        if self.othello_matrix.matrix[(row_position + 1, column_position)] == self.next_turn.tile_color:
            new_row_position = row_position + 1
            list_row_column = list(self.othello_matrix.matrix.keys())

            while (new_row_position, column_position) in list_row_column:
                if self.othello_matrix.matrix[(new_row_position, column_position)] == self.next_turn.tile_color:
                    flip_list.append((new_row_position, column_position))
                    new_row_position = new_row_position + 1
                    continue

                if self.othello_matrix.matrix[(new_row_position, column_position)] == self.current_turn.tile_color:
                    if self.mode == True:
                        self.flip_tiles(flip_list, self.current_turn.tile_color)
                        return True
                    else:
                        return flip_list

                if self.othello_matrix.matrix[(new_row_position, column_position)] == EMPTY_TILE:
                    if self.mode == True:
                        return False
                    else:
                        return []
        return []
            
    def check_top_right(self, row_position, column_position):
        """
        Method -- This checks in the top-right direction and keeps on iterating with (row+1) and (column+1) movement.
                    Once it hits the current turn color, it calls the flip function and passes the flip_list as
                    parameter then returns True as a legal position in top-right directional check. If flip switch is off,
                    i.e. mode is False, then it will only return the list of valid flip_list tiles if it is a legal position.
        Parameters --
            row_position -- the square matrix row position
            column_position -- the square matrix column position
        """
        if not isinstance(row_position, int) or not isinstance(column_position, int):
            raise TypeError("The row and column parameters must be an integer")
        elif row_position not in range(NUMBER_OF_SQUARES) or column_position not in range(NUMBER_OF_SQUARES):
            raise ValueError("Row and column values out of range")

        flip_list = []
        if self.othello_matrix.matrix[(row_position + 1, column_position + 1)] == self.next_turn.tile_color:
            new_row_position = row_position + 1
            new_column_position = column_position + 1
            list_row_column = list(self.othello_matrix.matrix.keys())

            while (new_row_position, new_column_position) in list_row_column:
                if self.othello_matrix.matrix[(new_row_position, new_column_position)] == self.next_turn.tile_color:
                    flip_list.append((new_row_position, new_column_position))
                    new_row_position = new_row_position + 1
                    new_column_position = new_column_position + 1
                    continue

                if self.othello_matrix.matrix[(new_row_position, new_column_position)] == self.current_turn.tile_color:
                    if self.mode == True:
                        self.flip_tiles(flip_list, self.current_turn.tile_color)
                        return True
                    else:
                        return flip_list

                if self.othello_matrix.matrix[(new_row_position, new_column_position)] == EMPTY_TILE:
                    if self.mode == True:
                        return False
                    else:
                        return []
        return []

    def check_right(self, row_position, column_position):
        """
        Method -- This checks in the right direction and keeps on iterating with (column+1) movement. Once it hits the
                    current turn color, it calls the flip function and passes the flip_list as parameter then returns
                    True as a legal position in right directional check. If flip switch is off, i.e. mode is False,
                    then it will only return the list of valid flip_list tiles if it is a legal position.
        Parameters --
            row_position -- the square matrix row position
            column_position -- the square matrix column position
        """
        if not isinstance(row_position, int) or not isinstance(column_position, int):
            raise TypeError("The row and column parameters must be an integer")
        elif row_position not in range(NUMBER_OF_SQUARES) or column_position not in range(NUMBER_OF_SQUARES):
            raise ValueError("Row and column values out of range")

        flip_list = []
        if self.othello_matrix.matrix[(row_position, column_position + 1)] == self.next_turn.tile_color:
            new_column_position = column_position + 1
            list_row_column = list(self.othello_matrix.matrix.keys())

            while (row_position, new_column_position) in list_row_column:
                if self.othello_matrix.matrix[(row_position, new_column_position)] == self.next_turn.tile_color:
                    flip_list.append((row_position, new_column_position))
                    new_column_position = new_column_position + 1
                    continue
                    
                if self.othello_matrix.matrix[(row_position, new_column_position)] == self.current_turn.tile_color:
                    if self.mode == True:
                        self.flip_tiles(flip_list, self.current_turn.tile_color)
                        return True
                    else:
                        return flip_list

                if self.othello_matrix.matrix[(row_position, new_column_position)] == EMPTY_TILE:
                    if self.mode == True:
                        return False
                    else:
                        return []
        return []

    def check_bottom_right(self, row_position, column_position):
        """
        Method -- This checks in the bottom-right direction and keeps on iterating with (row-1) and (column+1) movement.
                    Once it hits the current turn color, it calls the flip function and passes the flip_list as
                    parameter then returns True as a legal position in bottom-right directional check. If flip switch is off,
                    i.e. mode is False, then it will only return the list of valid flip_list tiles if it is a legal position.
        Parameters --
            row_position -- the square matrix row position
            column_position -- the square matrix column position
        """
        if not isinstance(row_position, int) or not isinstance(column_position, int):
            raise TypeError("The row and column parameters must be an integer")
        elif row_position not in range(NUMBER_OF_SQUARES) or column_position not in range(NUMBER_OF_SQUARES):
            raise ValueError("Row and column values out of range")

        flip_list = []
        if self.othello_matrix.matrix[(row_position - 1, column_position + 1)] == self.next_turn.tile_color:
            new_row_position = row_position - 1
            new_column_position = column_position + 1
            list_row_column = list(self.othello_matrix.matrix.keys())

            while (new_row_position, new_column_position) in list_row_column:
                if self.othello_matrix.matrix[(new_row_position, new_column_position)] == self.next_turn.tile_color:
                    flip_list.append((new_row_position, new_column_position))
                    new_row_position = new_row_position - 1
                    new_column_position = new_column_position + 1
                    continue
                    
                if self.othello_matrix.matrix[(new_row_position, new_column_position)] == self.current_turn.tile_color:
                    if self.mode == True:
                        self.flip_tiles(flip_list, self.current_turn.tile_color)
                        return True
                    else:
                        return flip_list

                if self.othello_matrix.matrix[(new_row_position, new_column_position)] == EMPTY_TILE:
                    if self.mode == True:
                        return False
                    else:
                        return []
        return []

    def check_bottom(self, row_position, column_position):
        """
        Method -- This checks in the bottom direction and keeps on iterating with (row-1) movement. Once it hits the
                    current turn color, it calls the flip function and passes the flip_list as parameter then returns
                    True as a legal position in bottom directional check. If flip switch is off, i.e. mode is False,
                    then it will only return the list of valid flip_list tiles if it is a legal position.
        Parameters --
            row_position -- the square matrix row position
            column_position -- the square matrix column position
        """
        if not isinstance(row_position, int) or not isinstance(column_position, int):
            raise TypeError("The row and column parameters must be an integer")
        elif row_position not in range(NUMBER_OF_SQUARES) or column_position not in range(NUMBER_OF_SQUARES):
            raise ValueError("Row and column values out of range")

        flip_list = []
        if self.othello_matrix.matrix[(row_position - 1, column_position)] == self.next_turn.tile_color:
            new_row_position = row_position - 1
            list_row_column = list(self.othello_matrix.matrix.keys())

            while (new_row_position, column_position) in list_row_column:
                if self.othello_matrix.matrix[(new_row_position, column_position)] == self.next_turn.tile_color:
                    flip_list.append((new_row_position, column_position))
                    new_row_position = new_row_position - 1
                    continue
                    
                if self.othello_matrix.matrix[(new_row_position, column_position)] == self.current_turn.tile_color:
                    if self.mode == True:
                        self.flip_tiles(flip_list, self.current_turn.tile_color)
                        return True
                    else:
                        return flip_list

                if self.othello_matrix.matrix[(new_row_position, column_position)] == EMPTY_TILE:
                    if self.mode == True:
                        return False
                    else:
                        return []
        return []

    def check_bottom_left(self, row_position, column_position):
        """
        Method -- This checks in the bottom-left direction and keeps on iterating with (row-1) and (column-1) movement.
                    Once it hits the current turn color, it calls the flip function and passes the flip_list as
                    parameter then returns True as a legal position in bottom-left directional check. If flip switch is off,
                    i.e. mode is False, then it will only return the list of valid flip_list tiles if it is a legal position.
        Parameters --
            row_position -- the square matrix row position
            column_position -- the square matrix column position
        """
        if not isinstance(row_position, int) or not isinstance(column_position, int):
            raise TypeError("The row and column parameters must be an integer")
        elif row_position not in range(NUMBER_OF_SQUARES) or column_position not in range(NUMBER_OF_SQUARES):
            raise ValueError("Row and column values out of range")

        flip_list = []
        if self.othello_matrix.matrix[(row_position - 1, column_position - 1)] == self.next_turn.tile_color:
            new_row_position = row_position - 1
            new_column_position = column_position - 1
            list_row_column = list(self.othello_matrix.matrix.keys())

            while (new_row_position, new_column_position) in list_row_column:
                if self.othello_matrix.matrix[(new_row_position, new_column_position)] == self.next_turn.tile_color:
                    flip_list.append((new_row_position, new_column_position))
                    new_row_position = new_row_position - 1
                    new_column_position = new_column_position - 1
                    continue
                    
                if self.othello_matrix.matrix[(new_row_position, new_column_position)] == self.current_turn.tile_color:
                    if self.mode == True:
                        self.flip_tiles(flip_list, self.current_turn.tile_color)
                        return True
                    else:
                        return flip_list

                if self.othello_matrix.matrix[(new_row_position, new_column_position)] == EMPTY_TILE:
                    if self.mode == True:
                        return False
                    else:
                        return []
        return []

    def check_left(self, row_position, column_position):
        """
        Method -- This checks in the left direction and keeps on iterating with (column-1) movement. Once it hits the
                    current turn color, it calls the flip function and passes the flip_list as parameter then returns
                    True as a legal position in left directional check. If flip switch is off, i.e. mode is False,
                    then it will only return the list of valid flip_list tiles if it is a legal position.
        Parameters --
            row_position -- the square matrix row position
            column_position -- the square matrix column position
        """
        if not isinstance(row_position, int) or not isinstance(column_position, int):
            raise TypeError("The row and column parameters must be an integer")
        elif row_position not in range(NUMBER_OF_SQUARES) or column_position not in range(NUMBER_OF_SQUARES):
            raise ValueError("Row and column values out of range")

        flip_list = []
        if self.othello_matrix.matrix[(row_position, column_position - 1)] == self.next_turn.tile_color:
            new_column_position = column_position - 1
            list_row_column = list(self.othello_matrix.matrix.keys())

            while (row_position, new_column_position) in list_row_column:
                if self.othello_matrix.matrix[(row_position, new_column_position)] == self.next_turn.tile_color:
                    flip_list.append((row_position, new_column_position))
                    new_column_position = new_column_position - 1
                    continue
                    
                if self.othello_matrix.matrix[(row_position, new_column_position)] == self.current_turn.tile_color:
                    if self.mode == True:
                        self.flip_tiles(flip_list, self.current_turn.tile_color)
                        return True
                    else:
                        return flip_list

                if self.othello_matrix.matrix[(row_position, new_column_position)] == EMPTY_TILE:
                    if self.mode == True:
                        return False
                    else:
                        return []
        return []

    def check_top_left(self, row_position, column_position):
        """
        Method -- This checks in the top-left direction and keeps on iterating with (row+1) and (column-1) movement.
                    Once it hits the current turn color, it calls the flip function and passes the flip_list as
                    parameter then returns True as a legal position in top-left directional check. If flip switch is off,
                    i.e. mode is False, then it will only return the list of valid flip_list tiles if it is a legal position.
        Parameters --
            row_position -- the square matrix row position
            column_position -- the square matrix column position
        """
        if not isinstance(row_position, int) or not isinstance(column_position, int):
            raise TypeError("The row and column parameters must be an integer")
        elif row_position not in range(NUMBER_OF_SQUARES) or column_position not in range(NUMBER_OF_SQUARES):
            raise ValueError("Row and column values out of range")

        flip_list = []
        if self.othello_matrix.matrix[(row_position + 1, column_position - 1)] == self.next_turn.tile_color:
            new_row_position = row_position + 1
            new_column_position = column_position - 1
            list_row_column = list(self.othello_matrix.matrix.keys())

            while (new_row_position, new_column_position) in list_row_column:
                if self.othello_matrix.matrix[(new_row_position, new_column_position)] == self.next_turn.tile_color:
                    flip_list.append((new_row_position, new_column_position))
                    new_row_position = new_row_position + 1
                    new_column_position = new_column_position - 1
                    continue
                    
                if self.othello_matrix.matrix[(new_row_position, new_column_position)] == self.current_turn.tile_color:
                    if self.mode == True:
                        self.flip_tiles(flip_list, self.current_turn.tile_color)
                        return True
                    else:
                        return flip_list

                if self.othello_matrix.matrix[(new_row_position, new_column_position)] == EMPTY_TILE:
                    if self.mode == True:
                        return False
                    else:
                        return []
        return []

    def flip_tiles(self, flip_list, tile_color):
        """
        Method -- This flips all the tiles given in the flip_list parameter to the tile_color given
                    as a parameter.
        Parameters --
            flip_list -- the list of tiles to be flipped
            tile_color -- the tile_color to which it is to be flipped
        """
        if not isinstance(flip_list, list):
            raise TypeError("The flip_list parameter must be of list datatype")
        elif tile_color != WHITE_TILE and tile_color != BLACK_TILE:
            raise ValueError("Tile must be white or black")
        
        for row_column in flip_list:
            self.current_turn.make_move(self.othello_matrix, row_column[0], row_column[1])
            self.update_board(row_column[0], row_column[1], tile_color)

    def switch_turn(self):
        """
        Method -- Once a valid move is played, it switches to other tile color. And in case the other
                    color is White, then it will trigger the computer to play.
        """
        temporary_turn = self.current_turn
        self.current_turn = self.next_turn
        self.next_turn = temporary_turn

        if self.current_turn == self.player2:
            self.computer()

    def computer(self):
        """
        Method -- This method automates the White player to play as a computer. It will get the list
                    of legal positions and will choose the optimal move by filling the square that flips
                    the maximum number of tiles by a particular move. This method runs in flip mode off,
                    in which while checking for legal positions, it would not start flipping the tiles.
        """
        self.mode = False                                                                           #Flip mode off
        empty_tiles = self.get_empty_tiles()
        legal_tiles = []

        for row_column in empty_tiles:
            if self.check_legal_move(row_column[0], row_column[1], self.mode):
                legal_tiles.append(row_column)

        if legal_tiles == []:
            self.check_the_winner()
        else:
            row_position, column_position = self.get_highest_flip(legal_tiles)
            print(f"White has played ({row_position}, {column_position})")
            self.get_move(row_position, column_position)

    def get_empty_tiles(self):
        """
        Method -- This method returns the list of square positions that are empty on the board.
        """
        list_tile = []
        for key, value in self.othello_matrix.matrix.items():
            if value == EMPTY_TILE:
                list_tile.append(key)
        return list_tile

    def get_highest_flip(self, legal_tiles):
        """
        Method -- This method returns the row and column position of the legal square, by choosing
                    which will flip the maximum number of tiles. If multiple positions flip the same
                    number of tiles then the last maximum flip count position from the list of
                    legal_tiles is chosen.
        Parameters --
            legal_tiles -- The list of positions that are legal according to the current turn
        """
        if not isinstance(legal_tiles, list):
            raise TypeError("The legal_tiles parameter must be of list datatype")
        
        counter = 0
        for row_column in legal_tiles:
            temp_count = len(self.get_flip_count(row_column[0], row_column[1], self.mode))
            if temp_count >= counter:
                counter = temp_count
                row = row_column[0]
                column = row_column[1]
        return row, column

    def get_flip_count(self, row_position, column_position, mode):
        """
        Method -- This method returns the list of tiles that could be flipped for a particular square position. It
                    will list out in 8 different directions based on its square location. If centrally placed, then
                    would be checked for 8 directions. If it is an edge then in 5 directions. If it is a corner
                    then 3 directions, etc.
        Parameters --
            row_position -- the square matrix row position
            column_position -- the square matrix column position
            mode -- it is the flip switch, if it is True, then while checking for legal moves it will start flipping
                    tiles, else if it is False, then it would not flip tiles while validating for legality.
        """
        if not isinstance(row_position, int) or not isinstance(column_position, int):
            raise TypeError("The row and column parameters must be an integer")
        elif row_position not in range(NUMBER_OF_SQUARES) or column_position not in range(NUMBER_OF_SQUARES):
            raise ValueError("Row and column values out of range")
        elif not isinstance(mode, bool):
            raise TypeError("The flip mode must be of Boolean type")

        if row_position in range(1, 7) and column_position in range (1, 7):
            total_flips = list(self.check_top(row_position, column_position) + self.check_top_right(row_position, column_position)\
                            + self.check_right(row_position, column_position)+ self.check_bottom_right(row_position, column_position)\
                            + self.check_bottom(row_position, column_position)+ self.check_bottom_left(row_position, column_position)\
                            + self.check_left(row_position, column_position)+ self.check_top_left(row_position, column_position))
            return total_flips
            
        elif row_position in range(1, 7) and column_position == 0:
            total_flips = list(self.check_top(row_position, column_position) + self.check_top_right(row_position, column_position)\
                            + self.check_right(row_position, column_position) + self.check_bottom_right(row_position, column_position)\
                            + self.check_bottom(row_position, column_position))
            return total_flips

        elif row_position in range(1, 7) and column_position == 7:
            total_flips = list(self.check_top(row_position, column_position) + self.check_bottom(row_position, column_position)\
                            + self.check_bottom_left(row_position, column_position) + self.check_left(row_position, column_position)\
                            + self.check_top_left(row_position, column_position))

            return total_flips

        elif row_position == 0 and column_position in range (1, 7):
            total_flips = list(self.check_top(row_position, column_position) + self.check_top_right(row_position, column_position)\
                            + self.check_right(row_position, column_position) + self.check_left(row_position, column_position)\
                            + self.check_top_left(row_position, column_position))
            return total_flips

        elif row_position == 7 and column_position in range (1, 7):
            total_flips = list(self.check_right(row_position, column_position) + self.check_bottom_right(row_position, column_position)\
                            + self.check_bottom(row_position, column_position) + self.check_bottom_left(row_position, column_position)\
                            + self.check_left(row_position, column_position))
            return total_flips

        elif row_position == 0 and column_position == 0:
            total_flips = list(self.check_top(row_position, column_position) + self.check_top_right(row_position, column_position)\
                            + self.check_right(row_position, column_position))
            return total_flips

        elif row_position == 0 and column_position == 7:
            total_flips = list(self.check_top(row_position, column_position) + self.check_left(row_position, column_position)\
                            + self.check_top_left(row_position, column_position))
            return total_flips

        elif row_position == 7 and column_position == 7:
            total_flips = list(self.check_left(row_position, column_position) + self.check_bottom_left(row_position, column_position)\
                            + self.check_bottom(row_position, column_position))
            return total_flips
            
        elif row_position == 7 and column_position == 0:
            total_flips = list(self.check_right(row_position, column_position) + self.check_bottom_right(row_position, column_position)\
                            + self.check_bottom(row_position, column_position))
            return total_flips
            
    def check_the_winner(self):
        """
        Method -- This method is to check which tile has won or if it is a tie. Also, if no more legal
                    moves are available then it will automatically count the total tile distribution
                    and declare winnner.
        """
        empty_count, black_count, white_count = self.count_tiles()

        if empty_count == 0:
            if black_count > white_count:
                winner = BLACK_TILE
                self.report_board_declare_winner(winner, black_count)
            elif white_count > black_count:
                winner = WHITE_TILE
                self.report_board_declare_winner(winner, white_count)
            else:
                winner = EMPTY_TILE
                self.report_board_declare_winner(winner, black_count)

        else:
            self.mode = False
            empty_tiles = self.get_empty_tiles()
            legal_tiles = []
            for row_column in empty_tiles:
                if self.check_legal_move(row_column[0], row_column[1], self.mode):
                    legal_tiles.append(row_column)
            
            if legal_tiles == []:
                if black_count > white_count:
                    winner = BLACK_TILE
                    self.report_board_declare_winner(winner, black_count)
                else:
                    winner = WHITE_TILE
                    self.report_board_declare_winner(winner, white_count)

    def count_tiles(self):
        """
        Method -- This method counts the number of tiles in each color
        """
        empty_count, black_count, white_count = 0, 0, 0
        for value in self.othello_matrix.matrix.values():
            if value == EMPTY_TILE:
                empty_count += 1
            elif value == BLACK_TILE:
                black_count += 1
            elif value == WHITE_TILE:
                white_count += 1
        return empty_count, black_count, white_count

    def report_board_declare_winner(self, winner, tiles_count):
        """
        Method -- This method is used to pass on the winner and the tiles count
        Parameters --
            winner -- the tile colour which won, tile must be white or black or
                        empty(for tie/draw)
            tiles_count -- the total number of tiles of winning color
        """
        if not isinstance(tiles_count, int):
            raise TypeError("The tiles count must be an integer")
        elif winner != WHITE_TILE and winner != BLACK_TILE and winner != EMPTY_TILE:
            raise ValueError("Tile must be white or black or empty(for tie/draw)")

        if winner == EMPTY_TILE:
            winner_data = f"IT'S A TIE!! There are {tiles_count} of each!"
        else:
            winner_data = f"The winner is {winner} and {winner} has {tiles_count} tiles."

        self.othello_board.declare_winner(winner_data)
        self.othello_board.make_score_file(tiles_count)

    def __str__(self):
        """
        Method -- returns a string that represents the Decider class
        Parameters: self -- the current object
        """
        return "This is the Decider class running"

    def __eq__(self, other):
        """
        Method -- compares the two Decider classes
        Parameters: 
            self -- the current object
            other -- the other Decider to compare with
        """
        return self.othello_board == other.othello_board
