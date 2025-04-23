print("Game started!")


def draw_board(spots):
    board = (
        f"\n|{spots[1]}|{spots[2]}|{spots[3]}|\n"
        f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
        f"|{spots[7]}|{spots[8]}|{spots[9]}|\n"
    )
    print(board)

def check_turn(turn):
    return 'O' if turn % 2 == 0 else 'X'

def check_for_win(spots):
    win_conditions = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # rows
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # columns
        (1, 5, 9), (3, 5, 7)              # diagonals
    ]
    for a, b, c in win_conditions:
        if spots[a] == spots[b] == spots[c]:
            return True
    return False

# Game setup
spots = {i: str(i) for i in range(1, 10)}
playing, complete = True, False
turn = 0
prev_turn = -1

# Game loop
while playing:

    draw_board(spots)

    if prev_turn == turn:
        print("Invalid spot selected, try again.")
    prev_turn = turn

    print(f"Player {(turn % 2) + 1}'s turn. Pick a spot or press q to quit.")
    choice = input()

    if choice == 'q':
        playing = False
    elif choice.isdigit() and int(choice) in spots:
        if spots[int(choice)] not in {'X', 'O'}:
            turn += 1
            spots[int(choice)] = check_turn(turn)

    if check_for_win(spots):
        playing, complete = False, True
    elif turn > 8:
        playing = False

# Final board + result
draw_board(spots)

if complete:
    winner = "Player 1" if check_turn(turn) == 'X' else "Player 2"
    print(f"{winner} wins!")
else:
    print("It's a tie!")

input("Press Enter to exit...")




