import unittest
import turtle
from model import *
from view import *
from controller import *

class testModelOthelloBoard(unittest.TestCase):
    screen = turtle.Screen()
    othello = turtle.Turtle()
    othello_board = OthelloBoard(screen, othello)
    othello_decider = Decider(othello_board)
    controller = Controller(othello_decider)

    def test_init_basic(self):
        with self.assertRaises(TypeError):
            self.othello_decider = Decider(5)

    def test_update_board_float_row(self):
        with self.assertRaises(TypeError):
            self.othello_decider.update_board(1.2, 2, "Black")

    def test_update_board_float_column(self):
        with self.assertRaises(TypeError):
            self.othello_decider.update_board(1, 2.2, "Black")

    def test_update_board_higher_column(self):
        with self.assertRaises(ValueError):
            self.othello_decider.update_board(1, 8, "White")

    def test_update_board_lower_row(self):
        with self.assertRaises(ValueError):
            self.othello_decider.update_board(-1, 2, "White")

    def test_update_board_invalid_tile_color(self):
        with self.assertRaises(ValueError):
            self.othello_decider.update_board(1, 2, "Pink")

    def test_update_board_string_argument(self):
        with self.assertRaises(TypeError):
            self.othello_decider.update_board("One", 2, "White")

    def test_convert_to_x_y_coordinate_float_argument(self):
        with self.assertRaises(TypeError):
            self.othello_decider.convert_to_x_y_coordinate(1, 2.2)

    def test_convert_to_x_y_coordinate_string_argument(self):
        with self.assertRaises(TypeError):
            self.othello_decider.convert_to_x_y_coordinate(1, "Two")

    def test_convert_to_x_y_coordinate_higher_column(self):
        with self.assertRaises(ValueError):
            self.othello_decider.convert_to_x_y_coordinate(1, 8)

    def test_convert_to_x_y_coordinate_basic(self):
        self.assertEqual(self.othello_decider.convert_to_x_y_coordinate(2, 3), (-25.0, -95.0))
        
    def test_get_move_float_argument(self):
        with self.assertRaises(TypeError):
            self.othello_decider.get_move(1.2, 2)

    def test_get_move_lower_column(self):
        with self.assertRaises(ValueError):
            self.othello_decider.get_move(4, -2)

    def test_get_move_string_argument(self):
        with self.assertRaises(TypeError):
            self.othello_decider.get_move(1, "Two")

    def test_check_legal_move_float_argument(self):
        with self.assertRaises(TypeError):
            self.othello_decider.check_legal_move(1, 2.5, True)

    def test_check_legal_move_string_argument(self):
        with self.assertRaises(TypeError):
            self.othello_decider.check_legal_move("One", 2, False)

    def test_check_legal_move_higher_column(self):
        with self.assertRaises(ValueError):
            self.othello_decider.check_legal_move(1, 10, True)

    def test_check_legal_move_string_mode(self):
        with self.assertRaises(TypeError):
            self.othello_decider.check_legal_move(1, 0, "True")

    def test_check_top_float_argument(self):
        with self.assertRaises(TypeError):
            self.othello_decider.check_top(4, 4.5)

    def test_check_top_string_argument(self):
        with self.assertRaises(TypeError):
            self.othello_decider.check_top(4, "Four")

    def test_check_top_higher_row(self):
        with self.assertRaises(ValueError):
            self.othello_decider.check_top(9, 3)

    def test_check_top_lower_column(self):
        with self.assertRaises(ValueError):
            self.othello_decider.check_top(3, -3)

    def test_check_top_right_float_argument(self):
        with self.assertRaises(TypeError):
            self.othello_decider.check_top_right(4, 4.5)

    def test_check_top_right_string_argument(self):
        with self.assertRaises(TypeError):
            self.othello_decider.check_top_right(4, "Four")

    def test_check_top_right_higher_row(self):
        with self.assertRaises(ValueError):
            self.othello_decider.check_top_right(9, 3)

    def test_check_top_right_lower_column(self):
        with self.assertRaises(ValueError):
            self.othello_decider.check_top_right(3, -3)

    def test_check_right_float_argument(self):
        with self.assertRaises(TypeError):
            self.othello_decider.check_right(4, 4.5)

    def test_check_right_string_argument(self):
        with self.assertRaises(TypeError):
            self.othello_decider.check_right(4, "Four")

    def test_check_right_higher_row(self):
        with self.assertRaises(ValueError):
            self.othello_decider.check_right(9, 3)

    def test_check_right_lower_column(self):
        with self.assertRaises(ValueError):
            self.othello_decider.check_right(3, -3)

    def test_check_bottom_right_float_argument(self):
        with self.assertRaises(TypeError):
            self.othello_decider.check_bottom_right(4, 4.5)

    def test_check_bottom_right_string_argument(self):
        with self.assertRaises(TypeError):
            self.othello_decider.check_bottom_right(4, "Four")

    def test_check_bottom_right_higher_row(self):
        with self.assertRaises(ValueError):
            self.othello_decider.check_bottom_right(9, 3)

    def test_check_bottom_right_lower_column(self):
        with self.assertRaises(ValueError):
            self.othello_decider.check_bottom_right(3, -3)

    def test_check_bottom_float_argument(self):
        with self.assertRaises(TypeError):
            self.othello_decider.check_bottom(4, 4.5)

    def test_check_bottom_string_argument(self):
        with self.assertRaises(TypeError):
            self.othello_decider.check_bottom(4, "Four")

    def test_check_bottom_higher_row(self):
        with self.assertRaises(ValueError):
            self.othello_decider.check_bottom(9, 3)

    def test_check_bottom_lower_column(self):
        with self.assertRaises(ValueError):
            self.othello_decider.check_bottom(3, -3)

    def test_check_bottom_left_float_argument(self):
        with self.assertRaises(TypeError):
            self.othello_decider.check_bottom_left(4, 4.5)

    def test_check_bottom_left_string_argument(self):
        with self.assertRaises(TypeError):
            self.othello_decider.check_bottom_left(4, "Four")

    def test_check_bottom_left_higher_row(self):
        with self.assertRaises(ValueError):
            self.othello_decider.check_bottom_left(9, 3)

    def test_check_bottom_left_lower_column(self):
        with self.assertRaises(ValueError):
            self.othello_decider.check_bottom_left(3, -3)

    def test_check_left_float_argument(self):
        with self.assertRaises(TypeError):
            self.othello_decider.check_left(4, 4.5)

    def test_check_left_string_argument(self):
        with self.assertRaises(TypeError):
            self.othello_decider.check_left(4, "Four")

    def test_check_left_higher_row(self):
        with self.assertRaises(ValueError):
            self.othello_decider.check_left(9, 3)

    def test_check_left_lower_column(self):
        with self.assertRaises(ValueError):
            self.othello_decider.check_left(3, -3)

    def test_check_top_left_float_argument(self):
        with self.assertRaises(TypeError):
            self.othello_decider.check_left(4, 4.5)

    def test_check_top_left_string_argument(self):
        with self.assertRaises(TypeError):
            self.othello_decider.check_left(4, "Four")

    def test_check_top_left_higher_row(self):
        with self.assertRaises(ValueError):
            self.othello_decider.check_left(9, 3)

    def test_check_top_left_lower_column(self):
        with self.assertRaises(ValueError):
            self.othello_decider.check_left(3, -3)

    def test_flip_tiles_invalid_color(self):
        with self.assertRaises(ValueError):
            self.othello_decider.flip_tiles([], "Pink")

    def test_flip_tiles_invalid_parameter(self):
        with self.assertRaises(TypeError):
            self.othello_decider.flip_tiles("list", "White")

    def test_get_highest_flip_invalid_parameter(self):
        with self.assertRaises(TypeError):
            self.othello_decider.get_highest_flip("list")

    def test_get_flip_count_string_row(self):
        with self.assertRaises(TypeError):
            self.othello_decider.get_flip_count("One", 2, True)

    def test_get_flip_count_float_column(self):
        with self.assertRaises(TypeError):
            self.othello_decider.get_flip_count(1, 2.0, True)

    def test_get_flip_count_invalid_mode(self):
        with self.assertRaises(TypeError):
            self.othello_decider.get_flip_count(1, 2, "True")

    def test_get_flip_count_higher_row(self):
        with self.assertRaises(ValueError):
            self.othello_decider.get_flip_count(9, 2, True)

    def test_report_board_declare_winner_invalid_tile_count(self):
        with self.assertRaises(TypeError):
            self.othello_decider.report_board_declare_winner("Black", 15.5)

    def test_report_board_declare_winner_invalid_winner(self):
        with self.assertRaises(ValueError):
            self.othello_decider.report_board_declare_winner("Pink", 15)

    def test_str_printing(self):
        self.assertEqual(str(self.othello_decider), "This is the Decider class running")

    def test_view_OthelloBoard_init_invalid_turtle_obj(self):
        with self.assertRaises(TypeError):
            othello_board1 = OthelloBoard(self.screen, "H")

    def test_view_OthelloBoard_init_invalid_screen(self):
        with self.assertRaises(TypeError):
            othello_board2 = OthelloBoard("S", self.othello)

    def test_view_OthelloBoard_get_instruction_invalid_coordinate(self):
        with self.assertRaises(TypeError):
            self.othello_board.get_instruction(2.2, "Three", "Black")

    def test_view_OthelloBoard_get_instruction_invalid_tile_color(self):
        with self.assertRaises(ValueError):
            self.othello_board.get_instruction(2.2, 3.3, "Pink")

    def test_view_OthelloBoard_declare_winner_invalid_parameter(self):
        with self.assertRaises(TypeError):
            self.othello_board.declare_winner(22)

    def test_view_OthelloBoard_make_score_file_invalid_tiles_count(self):
        with self.assertRaises(TypeError):
            self.othello_board.make_score_file("Twenty")

    def test_view_OthelloBoard_add_to_used_score_file_invalid_contents(self):
        with self.assertRaises(TypeError):
            self.othello_board.add_to_used_score_file(123, 25, "Name")

    def test_view_OthelloBoard_add_to_used_score_file_invalid_tiles_count(self):
        with self.assertRaises(TypeError):
            self.othello_board.add_to_used_score_file("Contents", "Twenty", "Name")

    def test_view_OthelloBoard_add_to_used_score_file_invalid_name(self):
        with self.assertRaises(TypeError):
            self.othello_board.add_to_used_score_file("Contents", 25, 123)

    def test_view_OthelloBoard_str_printing(self):
        self.assertEqual(str(self.othello_board), "This is the OthelloBoard class running")

    def test_controller_init_basic(self):
        with self.assertRaises(TypeError):
            self.controller("txt")

    def test_controller_get_click_sting_x(self):
        with self.assertRaises(TypeError):
            self.controller.get_click("Twenty", 25)

    def test_controller_get_click_string_y(self):
        with self.assertRaises(TypeError):
            self.controller.get_click(25, "Twenty")

    def test_controller_convert_click_to_row_column_string_x(self):
        with self.assertRaises(TypeError):
            self.controller.get_click("Twenty", 25)

    def test_controller_convert_click_to_row_column_string_y(self):
        with self.assertRaises(TypeError):
            self.controller.get_click(25, "Twenty")

    def test_controller_convert_click_to_row_column_valid_parameters(self):
        self.assertEqual(self.controller.convert_click_to_row_column(25.0, -55.0), (2, 4))

    def test_controller_str_printing(self):
        self.assertEqual(str(self.controller), "This is the Controller class running")
            
class testModelPlayer(unittest.TestCase):

    def test_init_basic(self):
        player1 = Player("White")
        self.assertEqual(player1.tile_color, "White")

    def test_init_invalid_tile(self):
        with self.assertRaises(ValueError):
            player2 = Player("Pink")

    def test_make_move_float_column(self):
        with self.assertRaises(TypeError):
            player2 = Player("Black")
            player2.make_move({}, 2, 2.5)

    def test_make_move_string_row(self):
        with self.assertRaises(TypeError):
            player3 = Player("Black")
            player3.make_move({}, "Two", 3)

    def test_make_move_lower_column(self):
        with self.assertRaises(ValueError):
            player4 = Player("White")
            player4.make_move({}, 2, -3)

    def test_str_printing(self):
        player1 = Player("White")
        self.assertEqual(str(player1), "This is the Player class running of White tile")

    def test_equality_true(self):
        player1 = Player("White")
        other = Player("White")
        self.assertTrue(player1 == other)

    def test_equality_false(self):
        player1 = Player("White")
        other = Player("Black")
        self.assertFalse(player1 == other)

class testModelOthelloModel(unittest.TestCase):

    def test_str_printing(self):
        othello = OthelloModel()
        self.assertEqual(str(othello), "This is the OthelloModel class running")

    def test_equality_true_basic_OthelloModel(self):
        othello = OthelloModel()
        other = OthelloModel()
        self.assertTrue(othello.put_initial_tiles() == other.put_initial_tiles())            

def main():
     unittest.main(verbosity = 3)

if __name__ == "__main__":
    main()
