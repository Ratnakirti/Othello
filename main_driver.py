import turtle

from model import *
from view import *
from controller import *

def main():
    '''
    Creating instances for the global "turtle screen" and the global "turtle othello"""
    '''
    screen = turtle.Screen()
    othello = turtle.Turtle()

    "Passing the screen and turtle as parameters to be drawn"
    othello_board = OthelloBoard(screen, othello)

    "Passing the othello_board(view) to the othello_decider(model)"
    othello_decider = Decider(othello_board)

    "Passing the othello_decider(model) to the controller"
    controller = Controller(othello_decider)

    "Whenever there is a click, the controller would be invoked"
    screen.onclick(controller.get_click)

if __name__ == "__main__":
    main()
