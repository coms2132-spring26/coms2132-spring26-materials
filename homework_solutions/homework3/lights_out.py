from collections import deque
import tkinter as tk

ROWS = 4
COLS = 4

def pretty_state(state):
    """
    Returns a string representation of a state for printing.
    """
    cols = len(state[0])
    border = "+" + "+".join("-" for _ in range(cols)) + "+"

    lines = [border]
    for row in state:
        lines.append("|" + "|".join(str(int(v)) for v in row) + "|")
        lines.append(border)
    return "\n".join(lines)


def toggle(state, row, col):
    """
    Return a NEW state where (row,col) and its orthogonal neighbors are toggled.
    State format: tuple of tuples with 0/1 entries.
    """
    nrows = len(state)
    ncols = len(state[0])

    # Copy to a mutable list structure
    grid = [list(r) for r in state]

    # Modify the grid
    for dr, dc in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
        rr, cc = row + dr, col + dc
        if 0 <= rr < nrows and 0 <= cc < ncols:
            grid[rr][cc] = 1 if grid[rr][cc] == 0 else 0  # flip 0<->1

    # Convert back to immutable tuple representation
    return tuple(tuple(r) for r in grid)


def goal_test(state):
    """True iff all lights are off (all zeros)."""
    for row in state:
      for cell in row:
        if cell == 1: 
          return False 
    return True 


def solve(start_state):
    """
    Breadth-First Search for the shortest sequence of moves that solves Lights Out.
    Returns: list of (row, col) moves that lead from start_state to a goal state.
             If start_state is already solved, returns [].
             If no solution is found, returns None.
    """
    if goal_test(start_state):
        return []
    
    # TODO (part a): implement BFS here
    
    path = []
    # ... decode/retrace path here
    return path


if __name__ == "__main__":
    start = (
        (0, 1, 0, 0),
        (1, 0, 1, 0),
        (0, 1, 0, 1),
        (0, 0, 1, 0),
    )
    print(pretty_state(start))
    print()

    solution_path = solve(start)
    if not solution_path:
      print("No solution found.")

    else:
      state = start 
      for move in solution_path: 
        print(move)
        state = toggle(state, *move)
        print(pretty_state(state)) 
        print()

    print(f"Solved in {len(solution_path)} steps.")

    
