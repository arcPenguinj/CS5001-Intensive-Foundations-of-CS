'''
Sample Code
CS 5001, Fall 2020

This code will get you started with the final project, milestone 1.
'''
import turtle


NUM_SQUARES = 8 # The number of squares on each row.
SQUARE = 50 # The size of each square in the checkerboard.
SQUARE_COLORS = ("light gray", "white")


def click_handler(x, y):
    '''
        Function -- click_handler
            Called when a click occurs.
        Parameters:
            x -- X coordinate of the click. Automatically provided by Turtle.
            y -- Y coordinate of the click. Automatically provided by Turtle.
        Returns:
            Does not and should not return. Click handlers are a special type
            of function automatically called by Turtle. You will not have
            access to anything returned by this function.
    '''
    print("Clicked at ", x, y)


def main():
    board_size = NUM_SQUARES * SQUARE
    # Create the UI window. This should be the width of the board plus a little margin
    window_size = board_size + SQUARE # The extra + SQUARE is the margin
    turtle.setup(window_size, window_size)

    # Set the drawing canvas size. The should be actual board size
    turtle.screensize(board_size, board_size)
    turtle.bgcolor("white") # The window's background color
    turtle.tracer(0, 0) # makes the drawing appear immediately

    pen = turtle.Turtle() # This variable does the drawing.
    pen.penup() # This allows the pen to be moved.
    pen.hideturtle() # This gets rid of the triangle cursor.

    pen.color("black", "white") # The first parameter is the outline color, the second is the fille

    # YOUR CODE HERE
    pen.setposition(-board_size / 2 - 1, -board_size / 2 - 1)
    draw_square(pen, board_size)

    # Click handling
    screen = turtle.Screen()
    screen.onclick(click_handler) # This will call call the click_handler function when a click occurs
    turtle.done() # Stops the window from closing.



if __name__ == "__main__":
    main()