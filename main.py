import random

BOARD_SIDE_LENGTH = 3
MAX_COMPUTER_MOVES_BEFORE_DRAW = 4

player_turns = []
computer_turns = []

def draw_board():
    for i in range(BOARD_SIDE_LENGTH):
        for j in range(BOARD_SIDE_LENGTH):
            move_printed = False
            for player_turn in player_turns:
                if (player_turn[0] == j and player_turn[1] == i):
                    print('X ', end = '')
                    move_printed = True
                    break
            for computer_turn in computer_turns:
                if (computer_turn[0] == j and computer_turn[1] == i):
                    print('O ', end = '')
                    move_printed = True
                    break
            if not move_printed:
                print('* ', end = '')
        print('\n', end = '')
    print('\n')

def get_computer_turn():
    x = random.randint(0, 2)
    y = random.randint(0, 2)

    if [x, y] in computer_turns or [x, y] in player_turns:
        return get_computer_turn()
    else:
        return [x, y]

def determine_if_winner(turns):
    # Horizontally
    for x in range(BOARD_SIDE_LENGTH):
        if [x, 0] in turns and [x, 1] in turns and [x, 2] in turns:
            return True
    # Vertically
    for y in range(BOARD_SIDE_LENGTH):
        if [0, y] in turns and [1, y] in turns and [2, y] in turns:
            return True
    # Diagonally
    if [0, 0] in turns and [1, 1] in turns and [2, 2] in turns:
        return True 
    if [0, 2] in turns and [1, 1] in turns and [2, 0] in turns:
        return True
    # When none match
    return False

while True:
    player_x = input('Enter the X coordinate: ')
    player_y = input('Enter the Y coordinate: ')
    print('\n', end='')

    try:
        x = int(player_x)
        y = int(player_y)

        if x < 0 or x >= BOARD_SIDE_LENGTH or y < 0 or y >= BOARD_SIDE_LENGTH:
            print("Move not allowed: Coordinates are out of bounds.\n")
            continue
        if [x, y] in player_turns or [x, y] in computer_turns:
            print('Move not allowed: Spot already taken.\n')
            continue
    except ValueError:
        print("Move not allowed: Coordinates must be integers.\n")
        continue
    
    player_turns.append([int(player_x), int(player_y)])

    if (determine_if_winner(player_turns)):
        print('Congratulations, you have won!\n')
        draw_board()
        break

    computer_turn = get_computer_turn()
    computer_turns.append(computer_turn)

    is_computer_winner = determine_if_winner(computer_turns)
    if (is_computer_winner):
        print('Oh no, you have lost against the computer...\n')
        draw_board()
        break

    # If neither the player nor the computer have won 
    # After the 4th player and computer turn, then it's a draw
    if len(computer_turns) == MAX_COMPUTER_MOVES_BEFORE_DRAW:
        print('It\'s a draw.\n')
        draw_board()
        break

    print(f"Your move: X: {player_x}, Y: {player_y}")
    print(f"The computer\'s move: X: {computer_turn[0]}, Y: {computer_turn[1]}\n")

    draw_board()
