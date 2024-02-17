# Import necessary libraries and modules
import pygame
import pgzero
import pgzrun
from random import randint
from pgzero.builtins import Actor

# Set the dimensions of the game window
WIDTH = 800
HEIGHT = 600

# Define the center coordinates of the game window
CENTER_X = WIDTH/2
CENTER_Y = HEIGHT/2

# Initialize various game-related variables
move_list = []            # List to store the generated dance moves
display_list = []         # List to store the dance moves to be displayed
song_list = ["arex beat", "great little challenge", 
             "lets play with the demon", "markalo disco", "vanishing-horizon"]  # List of songs

P1_score = 0              # Player 1's score
P2_score = 0              # Player 2's score
current_move = 0          # Index to keep track of the current move in the sequence
count = 4                 # Countdown timer
dance_length = 1          # Length of the dance sequence
sequence = 0              # Counter to determine the player's turn

say_dance = False         # Flag to indicate whether to display the "Player Dance!" message
show_countdown = True      # Flag to indicate whether to display the countdown message
moves_complete = False     # Flag to indicate whether the current dance sequence is complete
game_over = False          # Flag to indicate whether the game is over
game_intro = True          # Flag to indicate whether the game is in the intro state
P1_lost = False            # Flag to indicate whether Player 1 has lost
P2_lost = False            # Flag to indicate whether Player 2 has lost

# Create Actor objects for the dancers and dance move arrows
dancer = Actor("dancer-start")
dancer.pos = CENTER_X - 45, CENTER_Y - 40

dancer2 = Actor("dancer2-start")
dancer2.pos = CENTER_X + 50, CENTER_Y - 40

up = Actor("up")
right = Actor("right")
down = Actor("down")
left = Actor("left")

up.pos = CENTER_X, CENTER_Y + 110
right.pos = CENTER_X + 60, CENTER_Y + 170
down.pos = CENTER_X, CENTER_Y + 230
left.pos = CENTER_X - 60, CENTER_Y + 170

# Draw function to render the game elements on the screen
def draw():
    global game_over, P1_score, P2_score, say_dance
    global count, show_countdown
    
    # Check if the game is not over
    if not game_over:
        # Clear the screen and draw the background
        screen.clear()
        screen.blit("stage", (0, 0))
        
        # Draw the dancers and dance move arrows
        dancer.draw()
        dancer2.draw()
        up.draw()
        down.draw()
        right.draw()
        left.draw()
        
        # Display player scores
        screen.draw.text(f"P1 Score: {P1_score}", color="black", topleft=(10, 10))
        screen.draw.text(f"P2 Score: {P2_score}", color="black", topleft=(10, 27))
        
        # Display "Player Dance!" message
        if say_dance:
            if sequence % 2 == 0:
                player = 2
            else:
                player = 1
                
            screen.draw.text(f"Player {player} Dance!", color='black', topleft=(CENTER_X - 100, 150), fontsize=40)
        
        # Display the countdown message
        if show_countdown:
            screen.draw.text(f"Start in {count}!", color='black', topleft=(CENTER_X - 60, 150), fontsize=40)
    
    # Game over state
    else:
        # Clear the screen and draw the background
        screen.clear()
        screen.blit("stage", (0, 0))
        
        # Display player scores and "GAME OVER!" message
        screen.draw.text(f"P1 score: {P1_score}", color="black", topleft=(10, 10))
        screen.draw.text(f"P2 Score: {P2_score}", color="black", topleft=(10, 27))
        screen.draw.text("GAME OVER!", color="black", topleft=(CENTER_X - 130, 220), fontsize=60)

        # Display the loser message for the respective player
        if P1_lost:
            screen.draw.text("Player 1 Loses!", color="black", topleft=(CENTER_X - 70, 270), fontsize=30)
        elif P2_lost:
            screen.draw.text("Player 2 Loses!", color="black", topleft=(CENTER_X - 70, 270), fontsize=30)

# Function to reset the dancers and dance move arrows
def reset_dancer():
    global game_over
    
    # Check if the game is not over
    if not game_over:
        # Reset dancer and dance move arrow images
        dancer.image = "dancer-start"
        dancer2.image = "dancer2-start"
        up.image = "up"
        down.image = "down"
        right.image = "right"
        left.image = "left"

# Function to update the dancers based on the current move
def update_dancer(move):
    global game_over
    
    # Check if the game is not over
    if not game_over:
        # Update the dancers and dance move arrows based on the current move
        if sequence % 2 == 0:
            if move == 0:
                up.image = "up-lit"
                dancer2.image = "dancer2-up"
                clock.schedule(reset_dancer, 0.5)
            elif move == 1:
                right.image = "right-lit"
                dancer2.image = "dancer2-right"
                clock.schedule(reset_dancer, 0.5)
            elif move == 2:
                down.image = "down-lit"
                dancer2.image = "dancer2-down"
                clock.schedule(reset_dancer, 0.5)
            else:
                left.image = "left-lit"
                dancer2.image = "dancer2-left"
                clock.schedule(reset_dancer, 0.5)
        else:
            if move == 0:
                up.image = "up-lit"
                dancer.image = "dancer-up"
                clock.schedule(reset_dancer, 0.5)
            elif move == 1:
                right.image = "right-lit"
                dancer.image = "dancer-right"
                clock.schedule(reset_dancer, 0.5)
            elif move == 2:
                down.image = "down-lit"
                dancer.image = "dancer-down"
                clock.schedule(reset_dancer, 0.5)
            else:
                left.image = "left-lit"
                dancer.image = "dancer-left"
                clock.schedule(reset_dancer, 0.5)

# Function to display the dance moves
def display_moves():
    global move_list, display_list, dance_length
    global say_dance, show_countdown, current_move
    
    # Check if there are moves to display
    if display_list:
        this_move = display_list[0]
        display_list = display_list[1:]
        
        # Update the dancer and schedule the next move to be displayed
        if this_move == 0:
            update_dancer(0)
            clock.schedule(display_moves, 1)
        elif this_move == 1:
            update_dancer(1)
            clock.schedule(display_moves, 1)
        elif this_move == 2:
            update_dancer(2)
            clock.schedule(display_moves, 1)
        else:
            update_dancer(3)
            clock.schedule(display_moves, 1)
    else:
        say_dance = True
        show_countdown = False

# Function to generate a new set of dance moves
def generate_moves():
    global move_list, dance_length, count, sequence
    global show_countdown, say_dance
    
    # Reset countdown timer
    count = 4
    
    # Increase dance length every alternate sequence
    if (sequence % 2) == 0:
        dance_length += 1
    
    # Update sequence counter and reset move lists and flags
    sequence = sequence + 1
    move_list = []
    say_dance = False
      
    # Generate random dance moves and add them to the move list
    for move in range(0, dance_length):
        rand_move = randint(0, 3)
        move_list.append(rand_move)
        display_list.append(rand_move)
    
    # Set flags for countdown and display the moves
    show_countdown = True
    countdown()

# Function to implement the countdown
def countdown():
    global count, game_over, show_countdown
    
    # Decrement the countdown timer
    if count > 1:
        count = count - 1
        clock.schedule(countdown, 1)
    else:
        # Set flags to indicate countdown completion and display the dance moves
        show_countdown = False
        display_moves()

# Function to move to the next dance move in the sequence
def next_move():
    global dance_length, current_move, moves_complete
    
    # Check if there are more moves in the sequence
    if current_move < dance_length - 1:
        current_move = current_move + 1
    else:
        moves_complete = True

# Event handler for key release
def on_key_up(key):
    global P1_score, game_over, move_list, current_move, sequence
    global P2_score, P1_lost, P2_lost
    
    # Check if it's Player 1's turn
    if sequence % 2 != 0:
        # Update dancer based on the released key
        if key == keys.UP:
            update_dancer(0)
            
            # Check if the correct move was performed
            if move_list[current_move] == 0:
                P1_score = P1_score + 1
                next_move()
            else: 
                game_over = True
                P1_lost = True
        elif key == keys.RIGHT:
            update_dancer(1)
            
            if move_list[current_move] == 1:
                P1_score = P1_score + 1
                next_move()
            else: 
                game_over = True
                P1_lost = True
        elif key == keys.DOWN:
            update_dancer(2)
            
            if move_list[current_move] == 2:
                P1_score = P1_score + 1
                next_move()
            else: 
                game_over = True
                P1_lost = True
        elif key == keys.LEFT:
            update_dancer(3)
            
            if move_list[current_move] == 3:
                P1_score = P1_score + 1
                next_move()
            else: 
                game_over = True
                P1_lost = True
    
    # Check if it's Player 2's turn
    else:
        if key == keys.W:
            update_dancer(0)
            
            if move_list[current_move] == 0:
                P2_score = P2_score + 1
                next_move()
            else: 
                game_over = True
                P2_lost = True
        elif key == keys.D:
            update_dancer(1)
            
            if move_list[current_move] == 1:
                P2_score = P2_score + 1
                next_move()
            else: 
                game_over = True
                P2_lost = True
        elif key == keys.S:
            update_dancer(2)
            
            if move_list[current_move] == 2:
                P2_score = P2_score + 1
                next_move()
            else: 
                game_over = True
                P2_lost = True
        elif key == keys.A:
            update_dancer(3)
            
            if move_list[current_move] == 3:
                P2_score = P2_score + 1
                next_move()
            else: 
                game_over = True
                P2_lost = True

# Generate initial set of dance moves and play a random song
generate_moves()
music.play(song_list[randint(0, 4)])

# Update function to handle game logic
def update():
    global game_over, current_move, moves_complete
    
    # Check if the game is not over
    if not game_over:
        # Check if the current dance sequence is complete
        if moves_complete:
            # Generate a new set of dance moves and reset moves
            generate_moves()
            moves_complete = False
            current_move = 0
    else:
        # Stop playing music when the game is over
        music.stop()

# Run the Pygame Zero game
pgzrun.go()
