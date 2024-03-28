import os
import time
import random
import keyboard

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to draw the game board
def draw_board(paddle1, paddle2, ball, score1, score2):
    print(" " * (ball['x'] - 1) + ball['symbol'] + " " * (board_width - ball['x'] - 1))
    print("\n" * (paddle1['y'] - paddle_height) + ("#" * paddle_height) + "\n" * (board_height - paddle1['y'] - paddle_height))
    print("\n" * (paddle2['y'] - paddle_height) + ("#" * paddle_height) + "\n" * (board_height - paddle2['y'] - paddle_height))
    print("Player 1: " + str(score1) + "  Player 2: " + str(score2))

# Function to move the paddles
def move_paddles():
    if keyboard.is_pressed('w'):
        if paddle1['y'] > 1:
            paddle1['y'] -= 1
    elif keyboard.is_pressed('s'):
        if paddle1['y'] < board_height - paddle_height + 1:
            paddle1['y'] += 1

    if keyboard.is_pressed('up arrow'):
        if paddle2['y'] > 1:
            paddle2['y'] -= 1
    elif keyboard.is_pressed('down arrow'):
        if paddle2['y'] < board_height - paddle_height + 1:
            paddle2['y'] += 1

# Function to update the ball position
def update_ball():
    global ball_speed_x, ball_speed_y

    # Check for collision with walls or paddles
    if ball['y'] == 1 or ball['y'] == board_height:
        ball_speed_y *= -1
    elif ball['x'] == 2:
        if paddle1['y'] <= ball['y'] <= paddle1['y'] + paddle_height - 1:
            ball_speed_x *= -1
    elif ball['x'] == board_width - 1:
        if paddle2['y'] <= ball['y'] <= paddle2['y'] + paddle_height - 1:
            ball_speed_x *= -1
    elif ball['x'] == 1 or ball['x'] == board_width:
        if ball['x'] == 1:
            score2 += 1
        else:
            score1 += 1
        reset_ball()
    else:
        ball['x'] += ball_speed_x
        ball['y'] += ball_speed_y

# Function to reset the ball to the center
def reset_ball():
    global ball
    ball = {'x': board_width // 2, 'y': board_height // 2, 'symbol': 'O'}

# Initialize game variables
board_width = 20
board_height = 10
paddle_height = 3
ball_speed_x = 1
ball_speed_y = 1
score1 = 0
score2 = 0

paddle1 = {'y': board_height // 2 - paddle_height // 2}
paddle2 = {'y': board_height // 2 - paddle_height // 2}
ball = {'x': board_width // 2, 'y': board_height // 2, 'symbol': 'O'}

# Main game loop
while True:
    clear_screen()
    move_paddles()
    update_ball()
    draw_board(paddle1, paddle2, ball, score1, score2)
    time.sleep(0.1)
