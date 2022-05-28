NUMBER_OF_SQUARES = 8
SQUARE = 50
CIRCLE_RADIUS = 20
WHITE_TILE = "White"
BLACK_TILE = "Black"
EMPTY_TILE = "Empty"

import turtle
from model import *

class OthelloBoard:
    """
    Class OthelloBoard -- To receive instructions from model and declare winner
    """
    def __init__(self, screen, turtle_object):
        """
        Constructor -- Creates a new instance of the OthelloMatrix class
        Parameters --
            self -- the current object
            screen -- object of turtle screen
            turtle_object -- it is the object of turtle Othello
        Attributes --
            othello_screen -- object of turtle screen
            othello_turtle -- it is the object of turtle Othello
        Methods --
            get_instruction(), declare_winner(), make_score_file(),
            add_to_used_score_file()
        """
        if not isinstance(screen, turtle._Screen) or not isinstance(turtle_object, turtle.Turtle):
            raise TypeError("First parameter must be object of turtle.Screen() and second parameter must be object of turtle.Turtle()")
        
        self.othello_screen = OthelloScreen(screen)
        self.othello_turtle = OthelloTurtle(turtle_object)

    def get_instruction(self, x_coordinate, y_coordinate, tile_color):
        """
        Method -- This is used to pass the x and y coordinates by the model
        Parameters --
            x_coordinate -- the x coordinate being passed
            y_coordinate -- the y coordinate being passed
            tiles_color -- the color of the tile being passed
        """
        if not isinstance(x_coordinate, float) or not isinstance(y_coordinate, float):
            raise TypeError("The x and y coordinate parameters must be of float type")
        elif tile_color != WHITE_TILE and tile_color != BLACK_TILE:
            raise ValueError("Tile must be white or black")
        
        self.othello_turtle.draw_tile_on_matrix(x_coordinate, y_coordinate, tile_color)

    def declare_winner(self, winner_data):
        """
        Method -- This is used to declare the winner after game ends
        Parameters --
            winner_data -- The message at the end of the game from model
        """
        if not isinstance(winner_data, str):
            raise TypeError("The winner data must be of string type")
        
        print("\nNo more moves remaining\nGAME OVER!!")
        print(winner_data)

    def make_score_file(self, tiles_count):
        """
        Method -- This method is used to create a new scores file if it does not exist or else
                    append the high score to an existing scores file.
        Parameters --
            tiles_count -- The total number of tiles of the winner
        """
        if not isinstance(tiles_count, int):
            raise TypeError("The tiles count must be of integer type")

        try:
            file_open = open("scores.txt", "a+")
            file_open.seek(0)
            contents = file_open.read()
            file_open.close()
            name = input("Enter winner name: ")

            if contents == "":
                add_top = name + " " + str(tiles_count)
                file_open = open("scores.txt", "w")
                file_open.write(add_top)
                file_open.close()
                print("The name has been added to the Scores file successfully. Press ENTER to Exit.")
                raise SystemExit

            else:
                self.add_to_used_score_file(contents, tiles_count, name)
                print("The name has been added to the Scores file successfully. Press Enter to Exit.")
                raise SystemExit

        except OSError:
            print("OS error has occurred trying to open the file")
        except PermissionError:
            print("You do not have permission to use the file")
        except Exception as err:
            print("An unexpected error has occured opening the file. The error is %s"%(repr(err)))                  #repr(object) - Returns a string containing a printable
                                                                                                                    #representation of an object.

    def add_to_used_score_file(self, contents, tiles_count, name):
        """
        Method -- This method is used to add the scores to an existing file. If the new score is
                    is higher than the current values then it goes to the top, else it is appended
                    to the bottom of the file.
        Parameters --
            contents -- the contents of the already existing scores file
            tiles_count -- the total number of tiles of the winner
            name -- the name of the winner
        """
        if not isinstance(contents, str):
            raise TypeError("The contents of the file must be string type")
        elif not isinstance(tiles_count, int):
            raise TypeError("The tiles count must be of integer type")
        elif not isinstance(name, str):
            raise TypeError("The name of the winner must be of string type")

        try:
            line_list = []
            score_list = []
            splitted = contents.split("\n")
            
            for elements in splitted:
                line_list.append(elements.split())

            for elements in line_list:
                score_list.append(elements[-1])

            if tiles_count >= int(score_list[0]):
                add_top = name + " " + str(tiles_count)+ "\n"
                contents = add_top + contents
                file_open = open("scores.txt", "w")
                file_open.write(contents)
                file_open.close()
                
            else:
                file_open = open("scores.txt", "a+")
                add_down = "\n" + name + " " + str(tiles_count)
                file_open.write(add_down)
                file_open.close()

        except FileNotFoundError:
            print("The file was not found.")
        except OSError:
            print("OS error has occurred trying to open the file")
        except PermissionError:
            print("You do not have permission to use the file")
        except Exception as err:
            print("An unexpected error has occured opening the file. The error is %s"%(repr(err)))                  #repr(object) - Returns a string containing a printable
                                                                                                                    #representation of an object.
    def __str__(self):
        """
        Method -- returns a string that represents the OthelloBoard
        Parameters: self -- the current object
        """
        return "This is the OthelloBoard class running"

    def __eq__(self, other):
        """
        Method -- compares the value of two OthelloBoard
        Parameters: 
            self -- the current object
            other -- the other OthelloBoard to compare with
        """
        return self.turtle_object == other.turtle_object

class OthelloScreen:
    """
    Class OthelloScreen -- To initialize and setup the othello turtle screen
    """
    def __init__(self, screen):
        """
        Constructor -- Creates a new instance of the OthelloScreen class
        Parameters --
            self -- the current object
            screen -- it is the object of turtle screen
        Attributes --
            othello_screen -- the screen object of the turtle
            initialize_screen() -- to initialize the screen setup
        Methods --
            initialize_screen()
        """
        if not isinstance(screen, turtle._Screen):
            raise TypeError("The parameter must be object of turtle.Screen()")

        self.othello_screen = screen
        self.initialize_screen()

    def initialize_screen(self):
        """
        Method -- It sets up the window size, screensize and background color
        """
        self.othello_screen.setup(NUMBER_OF_SQUARES * SQUARE + SQUARE, NUMBER_OF_SQUARES * SQUARE + SQUARE)
        self.othello_screen.screensize(NUMBER_OF_SQUARES * SQUARE, NUMBER_OF_SQUARES * SQUARE)
        self.othello_screen.bgcolor("White")

    def __str__(self):
        """
        Method -- returns a string that represents the OthelloScreen
        Parameters: self -- the current object
        """
        return "This is the OthelloScreen class running"

    def __eq__(self, other):
        """
        Method -- compares the value of two OthelloScreen
        Parameters: 
            self -- the current object
            other -- the other OthelloScreen to compare with
        """
        return self.othello_screen == other.othello_screen

class OthelloTurtle:
    """
    Class OthelloTurtle -- To create the matrix on the screen by turtle
    """
    def __init__(self, turtle_object):
        """
        Constructor -- Creates a new instance of the OthelloTurtle class
        Parameters --
            self -- the current object
            turtle_object -- it is the object of turtle Othello
        Attributes --
            corner -- the coordinates for the bottom left corner in the matrix
            othello_turtle -- it is the object of turtle Othello
            prepare_turtle() -- creating the base of the othello matrix
            draw_matrix() -- adding the vertical and horizontal lines
        Methods --
            prepare_turtle(), draw_matrix(), draw_background(), draw_horizontal_lines(),
            draw_vertical_lines(), draw_lines(), draw_tile_on_matrix(), draw_circle()
        """
        if not isinstance(turtle_object, turtle.Turtle):
            raise TypeError("The parameter must be object of turtle.Turtle()")

        self.othello_turtle = turtle_object
        self.corner = (-NUMBER_OF_SQUARES * SQUARE)/2
        self.prepare_turtle()
        self.draw_matrix()

    def prepare_turtle(self):
        """
        Method -- To establish the turtle's basic features
        """
        self.othello_turtle.speed(0)
        self.othello_turtle.penup()
        self.othello_turtle.hideturtle()
        self.othello_turtle.color("black", "forest green")

    def draw_matrix(self):
        """
        Method -- To draw the matrix with the lines and background
        """
        self.othello_turtle.setposition(self.corner, self.corner)
        self.draw_background()
        self.draw_horizontal_lines()
        self.draw_vertical_lines()

    def draw_background(self):
        """
        Method -- To draw the background of Othello matrix
        """
        self.othello_turtle.begin_fill()
        for i in range(4):
            self.othello_turtle.pendown()
            self.othello_turtle.forward(SQUARE * NUMBER_OF_SQUARES)
            self.othello_turtle.left(90)
        self.othello_turtle.end_fill()
        self.othello_turtle.penup()

    def draw_horizontal_lines(self):
        """
        Method -- To draw the horizontal lines
        """
        for i in range(NUMBER_OF_SQUARES + 1):
            self.othello_turtle.setposition(self.corner, (SQUARE * i) + self.corner)
            self.draw_lines()

    def draw_vertical_lines(self):
        """
        Method -- To draw the vertical lines
        """
        self.othello_turtle.left(90)
        for i in range(NUMBER_OF_SQUARES + 1):
            self.othello_turtle.setposition((SQUARE * i) + self.corner, self.corner)
            self.draw_lines()
        self.othello_turtle.right(90)

    def draw_lines(self):
        """
        Method -- To draw one side of line(vertical or horizontal)
        """
        self.othello_turtle.pendown()
        self.othello_turtle.forward(SQUARE * NUMBER_OF_SQUARES)
        self.othello_turtle.penup()

    def draw_tile_on_matrix(self, x_coordinate, y_coordinate, tile_color):
        """
        Method -- To draw the tile on matrix
        Parameters --
            x_coordinate -- the x coordinate of the tile
            y_coordinate -- the y coordinate of the tile
            tile_color -- The color of circle that needs to be created
        """
        if not isinstance(x_coordinate, float) or not isinstance(y_coordinate, float):
            raise TypeError("The x and y coordinate parameters must be of float type")
        elif tile_color != WHITE_TILE and tile_color != BLACK_TILE:
            raise ValueError("Tile must be white or black")
        
        self.othello_turtle.setposition(x_coordinate, y_coordinate)
        self.draw_circle(tile_color)

    def draw_circle(self, tile_color):
        """
        Method -- To create a circle of tile color
        Parameters --
            tile_color -- The color of circle that needs to be created
        """
        if tile_color != WHITE_TILE and tile_color != BLACK_TILE:
            raise ValueError("Tile must be white or black")
        
        self.othello_turtle.fillcolor(tile_color)
        self.othello_turtle.begin_fill()
        self.othello_turtle.pendown()
        self.othello_turtle.circle(CIRCLE_RADIUS)
        self.othello_turtle.end_fill()
        self.othello_turtle.penup()
        
    def __str__(self):
        """
        Method -- returns a string that represents the OthelloTurtle
        Parameters: self -- the current object
        """
        return "This is the OthelloTurtle class running"

    def __eq__(self, other):
        """
        Method -- compares the value of two OthelloTurtle
        Parameters: 
            self -- the current object
            other -- the other Player to compare with
        """
        return self.turtle_object == other.turtle_object
