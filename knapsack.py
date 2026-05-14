# ==============================================================
#                   KNAPSACK VISUAL SOLVER
# ==============================================================

import os
import time
from datetime import datetime


# ==============================================================
# TERMINAL UTILITIES
# ==============================================================

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def typing(text, delay=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


# ==============================================================
# GLOBAL STATISTICS
# ==============================================================

steps = 0
backtracks = 0
best_solution = []
best_weight = 0


# ==============================================================
# BANNER
# ==============================================================

def banner():
    print("=" * 70)
    print("                 ADVANCED KNAPSACK SOLVER")
    print("=" * 70)
    print("          Recursive Backtracking Visualization")
    print("=" * 70)
    print()


# ==============================================================
# VISUAL DISPLAY
# ==============================================================

def show_items(items):
    print("\nAVAILABLE ITEMS")
    print("-" * 70)

    for i, item in enumerate(items, start=1):

        bar = "■" * min(item, 25)

        print(
            f"[{i:02}] "
            f"Weight : {item:>3} "
            f"| {bar}"
        )

    print("-" * 70)


def show_current_state(current, total, target):

    print("\nCURRENT BAG")
    print("-" * 70)

    if not current:
        print("Bag is empty.")

    else:
        for item in current:

            visual = "■" * min(item, 25)

            print(
                f"Weight : {item:>3} | {visual}"
            )

    print("-" * 70)

    print(f"Current Weight : {total}")
    print(f"Target Weight  : {target}")

    percentage = (total / target) * 100 if target != 0 else 0

    progress = int(percentage // 5)

    print(
        f"Capacity Usage : "
        f"[{'#' * progress}{'-' * (20 - progress)}] "
        f"{percentage:.1f}%"
    )

    print("-" * 70)


# ==============================================================
# LOADING ANIMATION
# ==============================================================

def loading_animation(text="Initializing Solver"):

    print()

    for _ in range(3):

        print(f"{text}.", end="\r")
        time.sleep(0.3)

        print(f"{text}..", end="\r")
        time.sleep(0.3)

        print(f"{text}...", end="\r")
        time.sleep(0.3)

    print(" " * 50)


# ==============================================================
# RECURSIVE KNAPSACK SOLVER
# ==============================================================

def knapsack(
    items,
    target,
    index=0,
    current=None,
    total=0,
    visual=True
):

    global steps
    global backtracks
    global best_solution
    global best_weight

    if current is None:
        current = []

    steps += 1

    # ==========================================================
    # UPDATE BEST SOLUTION
    # ==========================================================

    if total <= target and total > best_weight:
        best_weight = total
        best_solution = current[:]

    # ==========================================================
    # PERFECT SOLUTION FOUND
    # ==========================================================

    if total == target:

        if visual:

            clear()
            banner()

            print("PERFECT SOLUTION FOUND!")

            show_current_state(current, total, target)

            print(f"Steps       : {steps}")
            print(f"Backtracks  : {backtracks}")

            time.sleep(1)

        return True

    # ==========================================================
    # STOP CONDITIONS
    # ==========================================================

    if total > target or index >= len(items):

        backtracks += 1
        return False

    # ==========================================================
    # VISUALIZATION
    # ==========================================================

    if visual:

        clear()
        banner()

        print(f"Checking Item Index : {index}")
        print(f"Trying Weight       : {items[index]}")

        show_items(items)

        show_current_state(current, total, target)

        print(f"Steps       : {steps}")
        print(f"Backtracks  : {backtracks}")

        time.sleep(0.12)

    # ==========================================================
    # TAKE ITEM
    # ==========================================================

    take = knapsack(
        items,
        target,
        index + 1,
        current + [items[index]],
        total + items[index],
        visual
    )

    if take:
        return True

    # ==========================================================
    # BACKTRACK ANIMATION
    # ==========================================================

    if visual:

        clear()
        banner()

        print("BACKTRACKING...")
        print(f"Skipping Weight : {items[index]}")

        show_current_state(current, total, target)

        print(f"Steps       : {steps}")
        print(f"Backtracks  : {backtracks}")

        time.sleep(0.08)

    # ==========================================================
    # SKIP ITEM
    # ==========================================================

    skip = knapsack(
        items,
        target,
        index + 1,
        current,
        total,
        visual
    )

    return skip


# ==============================================================
# MAIN PROGRAM
# ==============================================================

def main():

    global steps
    global backtracks
    global best_solution
    global best_weight

    clear()
    banner()

    typing("Welcome to Advanced Knapsack Solver!\n")

    # ==========================================================
    # INPUT ITEMS
    # ==========================================================

    while True:

        try:

            total_items = int(
                input("Enter number of items : ")
            )

            if total_items <= 0:
                print("Number must be greater than 0.\n")

            else:
                break

        except ValueError:
            print("Please enter a valid number.\n")

    items = []

    print()

    for i in range(total_items):

        while True:

            try:

                weight = int(
                    input(f"Enter weight for item #{i+1} : ")
                )

                if weight <= 0:
                    print("Weight must be greater than 0.\n")

                else:
                    items.append(weight)
                    break

            except ValueError:
                print("Please enter a valid number.\n")

    # ==========================================================
    # INPUT TARGET
    # ==========================================================

    while True:

        try:

            target = int(
                input("\nEnter target weight : ")
            )

            if target <= 0:
                print("Target must be greater than 0.\n")

            else:
                break

        except ValueError:
            print("Please enter a valid number.\n")

    # ==========================================================
    # START SOLVER
    # ==========================================================

    clear()
    banner()

    show_items(items)

    print(f"\nTarget Weight : {target}")

    loading_animation("Starting Recursive Solver")

    start_time = time.time()

    solved = knapsack(
        items,
        target,
        visual=True
    )

    end_time = time.time()

    # ==========================================================
    # FINAL RESULT
    # ==========================================================

    clear()
    banner()

    print("FINAL RESULT")
    print("=" * 70)

    if solved:

        print("\nPerfect combination found!\n")

        show_current_state(
            best_solution,
            best_weight,
            target
        )

    else:

        print("\nPerfect combination not found.")
        print("Showing closest possible solution.\n")

        show_current_state(
            best_solution,
            best_weight,
            target
        )

    print("=" * 70)
    print("SELECTED ITEMS")
    print("=" * 70)

    if best_solution:

        for i, item in enumerate(best_solution, start=1):

            visual = "■" * min(item, 25)

            print(
                f"[{i}] "
                f"Weight : {item:>3} "
                f"| {visual}"
            )

    else:
        print("No items selected.")

    print("=" * 70)
    print("SOLVER STATISTICS")
    print("=" * 70)

    print(f"Total Items       : {len(items)}")
    print(f"Target Weight     : {target}")
    print(f"Best Weight       : {best_weight}")
    print(f"Total Steps       : {steps}")
    print(f"Total Backtracks  : {backtracks}")
    print(f"Execution Time    : {end_time - start_time:.4f} seconds")
    print(f"Finished At       : {datetime.now().strftime('%H:%M:%S')}")

    print("=" * 70)

    # ==========================================================
    # REPLAY OPTION
    # ==========================================================

    while True:

        again = input("\nTry again? (y/n) : ").lower()

        if again == "y":

            steps = 0
            backtracks = 0
            best_solution = []
            best_weight = 0

            main()
            return

        elif again == "n":

            print("\nThank you for using Advanced Knapsack Solver!")
            print("=" * 70)

            break

        else:
            print("Invalid input.")


# ==============================================================
# RUN PROGRAM
# ==============================================================

if __name__ == "__main__":
    main()