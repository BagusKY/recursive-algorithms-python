# =========================================================
#                N-QUEENS VISUAL SOLVER
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
# BANNER
# =========================

def banner():
    print("=" * 60)
    print("               N-QUEENS VISUAL SOLVER")
    print("=" * 60)
    print("     Recursive Backtracking Algorithm Project")
    print("=" * 60)
    print()


# =========================
# BOARD DISPLAY
# =========================

def print_board(board):
    n = len(board)

    print("\n" + "   " + " ".join([str(i) for i in range(n)]))
    print("   " + "--" * n)

    for i in range(n):
        print(f"{i}| ", end="")

        for j in range(n):
            if board[i][j] == 1:
                print("♛ ", end="")
            else:
                print("· ", end="")

        print()

    print()


# =========================
# SAFE CHECK
# =========================

def is_safe(board, row, col):
    n = len(board)

    # Cek kiri
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Cek diagonal kiri atas
    i = row
    j = col

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False

        i -= 1
        j -= 1

    # Cek diagonal kiri bawah
    i = row
    j = col

    while i < n and j >= 0:
        if board[i][j] == 1:
            return False

        i += 1
        j -= 1

    return True


# =========================
# ANIMATION
# =========================

def loading_animation(text="Searching"):
    print()

    for _ in range(3):
        print(f"{text}.", end="\r")
        time.sleep(0.3)

        print(f"{text}..", end="\r")
        time.sleep(0.3)

        print(f"{text}...", end="\r")
        time.sleep(0.3)

    print(" " * 30)


# =========================
# RECURSIVE SOLVER
# =========================

def solve(board, col, visual=True):
    global steps
    global backtracks

    n = len(board)

    # Semua queen berhasil ditempatkan
    if col >= n:
        return True

    # Coba setiap baris
    for row in range(n):

        steps += 1

        if is_safe(board, row, col):

            board[row][col] = 1

            if visual:
                clear()
                banner()

                print(f"Placing Queen #{col + 1}")
                print_board(board)

                print(f"Steps       : {steps}")
                print(f"Backtracks  : {backtracks}")

                time.sleep(0.15)

            # Rekursi
            if solve(board, col + 1, visual):
                return True

            # Backtracking
            board[row][col] = 0
            backtracks += 1

            if visual:
                clear()
                banner()

                print("Backtracking...")
                print_board(board)

                print(f"Steps       : {steps}")
                print(f"Backtracks  : {backtracks}")

                time.sleep(0.15)

    return False


# =========================
# MAIN PROGRAM
# =========================

def main():
    global steps
    global backtracks

    clear()
    banner()

    typing("Welcome to N-Queens Visual Solver!\n")

    while True:
        try:
            n = int(input("Enter board size (minimum 4) : "))

            if n < 4:
                print("Board size must be at least 4.\n")
            else:
                break

        except ValueError:
            print("Please enter a valid number.\n")

    board = [[0 for _ in range(n)] for _ in range(n)]

    clear()
    banner()

    print(f"Board Size : {n} x {n}")
    print()

    loading_animation("Initializing Solver")

    start_time = time.time()

    solved = solve(board, 0, visual=True)

    end_time = time.time()

    clear()
    banner()

    print("FINAL RESULT")
    print("=" * 60)

    if solved:
        print("\nSolution Found Successfully!\n")
        print_board(board)

    else:
        print("\nNo Solution Found.\n")

    print("=" * 60)
    print("SOLVER STATISTICS")
    print("=" * 60)

    print(f"Board Size        : {n}x{n}")
    print(f"Total Steps       : {steps}")
    print(f"Total Backtracks  : {backtracks}")
    print(f"Execution Time    : {end_time - start_time:.4f} seconds")
    print(f"Finished At       : {datetime.now().strftime('%H:%M:%S')}")

    print("=" * 60)

    # Replay option
    while True:
        again = input("\nTry another board? (y/n) : ").lower()

        if again == "y":
            steps = 0
            backtracks = 0
            main()
            return

        elif again == "n":
            print("\nThank you for using N-Queens Visual Solver!")
            print("=" * 60)
            break

        else:
            print("Invalid input.")


# =========================
# RUN PROGRAM
# =========================

if __name__ == "__main__":
    main()