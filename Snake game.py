# Importing moduls necessary for game
import random
import curses

# Initialize the curses library to create our screen
screen = curses.initscr()
# Hide the mouse cursor
curses.curs_set(0)  # 0 means invisible
# Get max screen height and width
screen_height, screen_width = screen.getmaxyx()
# Create a new window
window = curses.newwin(screen_height, screen_width, 0, 0)
# Allow window to receive input from the keyboard
window.keypad(1)
# Set the delay for updating the screen
window.timeout(100)  # every ml second update my screen. 1 sec = 100 ml\sec

# Set the x,y coordinates of the initial position of snake's head
snk_x = screen_width // 4
snk_y = screen_height // 2
# define the initial position of the snake body
snake = [
    [snk_y, snk_x],  # head
    [snk_y, snk_x - 1],
    [snk_y, snk_x - 2]  # tail
]
# Create the food in the middle of window
food = [screen_height // 2, screen_width // 2]
# Add the food by using PI character from curses module
window.addch(food[0], food[1], curses.ACS_PI)
# Set initial movement direction to right
key = curses.KEY_RIGHT
# Create game loop that loops forever until player loses or quits the game
while True:  # finite loop

    # Get the next key that will be pressed by user
    next_key = window.getch()
    # If user doesn't input anything, key remains same, else key will be set to the new pressed key
    key = key if next_key == -1 else next_key
    # Check if snake collided with the walls or itself
    if snake[0][0] in [0, screen_height] or snake[0][1] in [0, screen_width] or snake[0] in snake[1:]:
        curses.endwin()  # closing the window
        quit()  # exit the program
    # Set the new position of the snake head based on the direction
    new_head = [snake[0][0], snake[0][1]]
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1

    # Insert the new head to the first position of snake list
    snake.insert(0, new_head)
    # Check if snake ate the food
    if snake[0] == food:
        food = None  # remove food if snake ate it
        # While food is removed, generate new food in a random place on screen
        while food is None:
            new_food = [
                random.randint(1, screen_height - 1),
                random.randint(1, screen_width - 1)
            ]
            food = new_food if new_food not in snake else None
        window.addch(food[0], food[1], curses.ACS_PI)
    else:
        # Otherwise remove the last segment of snake body
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')

    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
    # updte the position of the snake on the screen






