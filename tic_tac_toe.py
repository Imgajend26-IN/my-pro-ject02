import math
import random

EMPTY = " "
PLAYER_X = "X"
PLAYER_O = "O"

def new_board():
    return [EMPTY] * 9

def display_board(board):
    # prints a 3x3 board
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def available_moves(board):
    return [i for i, v in enumerate(board) if v == EMPTY]

def is_full(board):
    return all(v != EMPTY for v in board)

def winner(board):
    # return 'X' or 'O' if there's a winner, or None
    wins = [
        (0,1,2),(3,4,5),(6,7,8),  # rows
        (0,3,6),(1,4,7),(2,5,8),  # cols
        (0,4,8),(2,4,6)           # diagonals
    ]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] != EMPTY:
            return board[a]
    return None

def print_instructions():
    print("Tic-Tac-Toe")
    print("Enter a number 1-9 to place your mark:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()

def player_move(board, mark):
    moves = available_moves(board)
    while True:
        try:
            choice = input(f"Player {mark}, choose 1-9: ").strip()
            idx = int(choice) - 1
            if idx in moves:
                board[idx] = mark
                return
            else:
                print("Invalid move — spot taken or out of range.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

def minimax(board, depth, is_maximizing, ai_mark, human_mark):
    win = winner(board)
    if win == ai_mark:
        return 10 - depth
    elif win == human_mark:
        return depth - 10
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves(board):
            board[move] = ai_mark
            score = minimax(board, depth+1, False, ai_mark, human_mark)
            board[move] = EMPTY
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves(board):
            board[move] = human_mark
            score = minimax(board, depth+1, True, ai_mark, human_mark)
            board[move] = EMPTY
            best_score = min(best_score, score)
        return best_score

def best_move(board, ai_mark, human_mark):
    best_score = -math.inf
    move_choice = None
    for move in available_moves(board):
        board[move] = ai_mark
        score = minimax(board, 0, False, ai_mark, human_mark)
        board[move] = EMPTY
        if score > best_score:
            best_score = score
            move_choice = move
    return move_choice

def ai_move(board, ai_mark, human_mark, difficulty="hard"):
    # difficulty: "hard" uses minimax (unbeatable)
    # "medium" randomly chooses best of a few or random
    # "easy" random
    moves = available_moves(board)
    if difficulty == "easy":
        return random.choice(moves)
    if difficulty == "medium":
        # 50% best move, 50% random
        if random.random() < 0.5:
            return best_move(board, ai_mark, human_mark)
        else:
            return random.choice(moves)
    # default hard
    return best_move(board, ai_mark, human_mark)

def play_game(vs_ai=True, ai_starts=False, ai_difficulty="hard"):
    board = new_board()
    print_instructions()
    current = PLAYER_O if ai_starts and vs_ai else PLAYER_X

    # If AI plays, determine its mark
    if vs_ai:
        ai_mark = PLAYER_O if ai_starts else PLAYER_O if random.random() < 0 else PLAYER_O
        # We'll let human choose mark below for clarity
        pass
    # Let human pick X or O if vs AI
    if vs_ai:
        human_choice = ""
        while human_choice not in ("X", "O"):
            human_choice = input("Do you want to be X or O? (X goes first): ").strip().upper()
        human_mark = human_choice
        ai_mark = PLAYER_O if human_mark == PLAYER_X else PLAYER_X
        current = PLAYER_X  # X always moves first
    else:
        human_mark = None
        ai_mark = None

    display_board(board)

    while True:
        if vs_ai:
            if current == human_mark:
                player_move(board, human_mark)
            else:
                print(f"AI ({ai_mark}) is thinking...")
                move = ai_move(board, ai_mark, human_mark, difficulty=ai_difficulty)
                board[move] = ai_mark
        else:
            # two human players
            player_move(board, current)

        display_board(board)
        win = winner(board)
        if win:
            print(f"🎉 {win} wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break

        # switch
        current = PLAYER_O if current == PLAYER_X else PLAYER_X

def main():
    print("Welcome — Tic Tac Toe\n")
    while True:
        mode = ""
        while mode not in ("1","2"):
            print("Choose mode:")
            print("1) Player vs AI")
            print("2) Player vs Player")
            mode = input("Enter 1 or 2: ").strip()

        if mode == "1":
            diff = ""
            while diff not in ("easy","medium","hard"):
                diff = input("Choose AI difficulty (easy, medium, hard): ").strip().lower()
            play_game(vs_ai=True, ai_starts=False, ai_difficulty=diff)
        else:
            play_game(vs_ai=False)

        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()