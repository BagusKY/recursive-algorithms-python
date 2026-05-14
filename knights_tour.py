# =========================================================
#               KNIGHT'S TOUR VISUAL SOLVER
# =========================================================

import os
import time
from datetime import datetime


# =========================
# TERMINAL UTILITIES
# =========================

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def typing(text, delay=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


# =========================
# GLOBAL STATISTICS
# =========================

steps = 0
backtracks = 0


# =========================
# KNIGHT MOVES
# =========================

moves = [
    (2, 1),
    (1, 2),
    (-1, 2),
    (-2, 1),
    (-2, -1),
    (-1, -2),
    (1, -2),
    (2, -1)
]


# =========================
# BANNER
# =========================

def banner():
    print("=" * 65)
    print("               KNIGHT'S TOUR SOLVER")
    print("=" * 65)
    print("        Recursive Backtracking Visualization")
    print("=" * 65)
    print()


# =========================
# BOARD DISPLAY
# =========================

def print_board(board):
    n = len(board)

    print()

    for row in board:
        for cell in row:
            if cell == -1:
                print("  . ", end="")
            else:
                print(f"{cell:3} ", end="")
        print()

    print()


# =========================
# VALID MOVE CHECK
# =========================

def is_valid(x, y, board):
    n = len(board)

    return (
        0 <= x < n and
        0 <= y < n and
        board[x][y] == -1
    )


# =========================
# LOADING ANIMATION
# =========================

def loading_animation(text="Initializing"):
    print()

    for _ in range(3):
        print(f"{text}.", end="\r")
        time.sleep(0.3)

        print(f"{text}..", end="\r")
        time.sleep(0.3)

        print(f"{text}...", end="\r")
        time.sleep(0.3)

    print(" " * 40)


# =========================
# RECURSIVE SOLVER
# =========================

def solve(board, x, y, move_count, visual=True):
    global steps
    global backtracks

    n = len(board)

    # Semua kotak sudah dikunjungi
    if move_count == n * n:
        return True

    # Coba semua kemungkinan langkah
    for dx, dy in moves:

        next_x = x + dx
        next_y = y + dy

        if is_valid(next_x, next_y, board):

            steps += 1

            board[next_x][next_y] = move_count

            if visual:
                clear()
                banner()

                print(f"Current Move : {move_count}")
                print(f"Knight Position : ({next_x}, {next_y})")

                print_board(board)

                print(f"Steps       : {steps}")
                print(f"Backtracks  : {backtracks}")

                time.sleep(0.08)

            # Rekursi
            if solve(board, next_x, next_y, move_count + 1, visual):
                return True

            # Backtracking
            board[next_x][next_y] = -1
            backtracks += 1

            if visual:
                clear()
                banner()

                print("Backtracking...")
                print_board(board)

                print(f"Steps       : {steps}")
                print(f"Backtracks  : {backtracks}")

                time.sleep(0.05)

    return False


# =========================
# MAIN PROGRAM
# =========================

def main():
    global steps
    global backtracks

    clear()
    banner()

    typing("Welcome to Knight's Tour Visual Solver!\n")

    # Input ukuran papan
    while True:
        try:
            n = int(input("Enter board size (minimum 5) : "))

            if n < 5:
                print("Board size must be at least 5.\n")
            else:
                break

        except ValueError:
            print("Please enter a valid number.\n")

    # Input posisi awal
    while True:
        try:
            start_x = int(input("Enter starting row    : "))
            start_y = int(input("Enter starting column : "))

            if 0 <= start_x < n and 0 <= start_y < n:
                break

            else:
                print("Position out of range.\n")

        except ValueError:
            print("Please enter valid numbers.\n")

    # Membuat papan
    board = [[-1 for _ in range(n)] for _ in range(n)]

    # Posisi awal
    board[start_x][start_y] = 0

    clear()
    banner()

    print(f"Board Size      : {n} x {n}")
    print(f"Starting Point  : ({start_x}, {start_y})")

    loading_animation("Starting Solver")

    start_time = time.time()

    solved = solve(board, start_x, start_y, 1, visual=True)

    end_time = time.time()

    clear()
    banner()

    print("FINAL RESULT")
    print("=" * 65)

    if solved:

        print("\nKnight's Tour Completed Successfully!\n")

        print_board(board)

    else:

        print("\nNo Solution Found.\n")

    print("=" * 65)
    print("SOLVER STATISTICS")
    print("=" * 65)

    print(f"Board Size        : {n}x{n}")
    print(f"Starting Position : ({start_x}, {start_y})")
    print(f"Total Steps       : {steps}")
    print(f"Total Backtracks  : {backtracks}")
    print(f"Execution Time    : {end_time - start_time:.4f} seconds")
    print(f"Finished At       : {datetime.now().strftime('%H:%M:%S')}")

    print("=" * 65)

    # Replay option
    while True:

        again = input("\nTry another board? (y/n) : ").lower()

        if again == "y":

            steps = 0
            backtracks = 0

            main()
            return

        elif again == "n":

            print("\nThank you for using Knight's Tour Solver!")
            print("=" * 65)

            break

        else:
            print("Invalid input.")


# =========================
# RUN PROGRAM
# =========================

if __name__ == "__main__":
    main()