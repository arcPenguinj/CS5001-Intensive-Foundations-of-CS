'''
Fall2020
CS 5001
Yici Zhu
Final Project
'''

import turtle
from draw_utilities import draw_square
from draw_utilities import draw_circle
from game_state import GameState


NUM_SQUARES = 8  # The number of squares on each row.
SQUARE = 50  # The size of each square in the checkerboard.
SQUARE_COLORS = ("light gray", "white")
CIRCLE_COLORS = ("black", "red")
CIRCLE = SQUARE / 2  # The size of each chess in the checkerboard
PLAYER_ROWS = 3
CORNER = (- NUM_SQUARES * SQUARE) / 2


def draw_board():
    '''
    Function -- draw board
        Draw chess board
    Parameters:
        None. Use Constant variables
    Returns:
        Nothing. Draws 8 * 8 squares.
    '''
    board_size = NUM_SQUARES * SQUARE
    # Create the UI window. This should be the width of the board plus a little margin
    window_size = board_size + SQUARE  # The extra + SQUARE is the margin
    turtle.setup(window_size, window_size)

    # Set the drawing canvas size. The should be actual board size
    turtle.screensize(board_size, board_size)
    turtle.bgcolor("white")  # The window's background color
    turtle.tracer(0, 0)  # makes the drawing appear immediately

    pen = turtle.Turtle()  # This variable does the drawing.
    pen.penup()  # This allows the pen to be moved.
    pen.hideturtle()  # This gets rid of the triangle cursor.

    pen.color("black", "white")  # The first parameter is the outline color, the second is the fille

    # YOUR CODE HERE
    # step 1 the board outline
    corner = -board_size / 2
    pen.setposition(corner, corner) # bottom left
    draw_square(pen, board_size)

    # step2 the square
    pen.color("black", SQUARE_COLORS[0])
    for col in range(NUM_SQUARES):
        for row in range(NUM_SQUARES):
            if col % 2 != row % 2:
                pen.setposition(corner + SQUARE * col, corner + SQUARE * row)
                draw_square(pen, SQUARE)

    # step3 the circle
    # step3.1 play's chess
    pen.color(CIRCLE_COLORS[0], CIRCLE_COLORS[0])
    for row in range(PLAYER_ROWS):
        for col in range(NUM_SQUARES):
            if row % 2 != col % 2:
                pen.setposition(corner + SQUARE * col + SQUARE / 2, corner + SQUARE * row)
                draw_circle(pen, CIRCLE)

    # step 3.2 AI's chess
    pen.color(CIRCLE_COLORS[1], CIRCLE_COLORS[1])
    for row in range(PLAYER_ROWS):
        for col in range(NUM_SQUARES):
            if row % 2 == col % 2:
                pen.setposition(corner + SQUARE / 2 + SQUARE * col, corner + SQUARE * (NUM_SQUARES - 1) - SQUARE * row )
                draw_circle(pen, CIRCLE)


def reset():
    '''
    Function -- reset
        reset the game
    Parameters:
        None.
    Returns:
        call GameState to replay the game
    '''
    draw_board()
    game_state = GameState()
    return game_state


def main():
    game_state = reset()
    game_state.game_start()

    # Click handling
    screen = turtle.Screen()
    screen.onclick(game_state.click_handler) # This will call call the click_handler function when a click occurs

    turtle.done() # Stops the window from closing.


if __name__ == "__main__":
    main()
