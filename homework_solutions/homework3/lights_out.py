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

    queue = deque() # also okay to use a list with append and pop(0)

    discovered = set()
    queue.append(start_state)
    discovered.add(start_state)
    bptr = {start_state : None}
    moves = {start_state : None}

    
    while queue: 

      u = queue.popleft()
      
      # discover each adjacent state
      for rr in range(ROWS):
        for cc in range(COLS): 
          v = toggle(u, rr, cc)
          if not v in discovered: # if the state is new
            bptr[v] = u
            moves[v] = (rr,cc)

            if goal_test(v): # found the goal
              # now retrace the path
              path = [] 
              current = v
              while bptr[current]:
                path.append(moves[current]) 
                current = bptr[current]
              return path[::-1]

            # if v was not a goal state
            queue.append(v)
            discovered.add(v)

    return None # queue empty and no solution found          



class LightsOutGUI:
    def __init__(self, master, start_state):
        self.master = master
        self.cell_size = 80
        self.padding = 10
        
        master.title("Lights Out Solver")
        
        # Store start state as tuple and initialize current state
        self.start_state = tuple(tuple(row) for row in start_state)
        self.state = self.start_state
        self.size = len(self.start_state)
        
        # Create canvas
        canvas_size = self.size * self.cell_size + 2 * self.padding
        self.canvas = tk.Canvas(master, width=canvas_size, height=canvas_size, bg='gray')
        self.canvas.pack(pady=10)
        
        # Bind click event
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        
        # Create buttons frame
        button_frame = tk.Frame(master)
        button_frame.pack(pady=10)
        
        self.solve_button = tk.Button(button_frame, text="Solve", command=self.solve_game, 
                                       font=('Arial', 14), bg='lightgreen', width=10)
        self.solve_button.pack(side=tk.LEFT, padx=5)
        
        self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset_game,
                                       font=('Arial', 14), bg='lightcoral', width=10)
        self.reset_button.pack(side=tk.LEFT, padx=5)
        
        # Status label
        self.status_label = tk.Label(master, text="Click squares to toggle lights", 
                                     font=('Arial', 12))
        self.status_label.pack(pady=5)
        
        # Draw initial board
        self.draw_board()
    
    def draw_board(self):
        """Draw the current state of the board"""
        self.canvas.delete("all")
        
        for row in range(self.size):
            for col in range(self.size):
                x1 = col * self.cell_size + self.padding
                y1 = row * self.cell_size + self.padding
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                
                # Choose color based on state
                color = 'yellow' if self.state[row][col] == 1 else 'dark blue'
                
                # Draw rectangle
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, 
                                            outline='black', width=2,
                                            tags=f"cell_{row}_{col}")
        
        # Check if solved using your goal_test function
        if goal_test(self.state):
            self.status_label.config(text="🎉 Solved! All lights are off!", fg='green')
    
    def on_canvas_click(self, event):
        """Handle canvas click to toggle lights"""
        # Calculate which cell was clicked
        col = (event.x - self.padding) // self.cell_size
        row = (event.y - self.padding) // self.cell_size
        
        # Validate click is within bounds
        if 0 <= row < self.size and 0 <= col < self.size:
            self.toggle_cell(row, col)
    
    def toggle_cell(self, row, col):
        """Toggle a cell and its neighbors using your toggle function"""
        self.state = toggle(self.state, row, col)
        self.draw_board()
        self.status_label.config(text=f"Clicked ({row}, {col})", fg='black')
    
    def solve_game(self):
        """Solve the game from current state"""
        if goal_test(self.state):
            self.status_label.config(text="Already solved!", fg='green')
            return
        
        self.status_label.config(text="Solving...", fg='blue')
        self.solve_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)
        
        # Call your solve function with current state
        solution = solve(self.state)
        
        if solution is None:
            self.status_label.config(text="No solution found!", fg='red')
            self.solve_button.config(state=tk.NORMAL)
            self.reset_button.config(state=tk.NORMAL)
        else:
            self.show_solution(solution, 0)
    
    def show_solution(self, solution, step):
        """Show solution step by step with 0.5s pause"""
        if step >= len(solution):
            self.status_label.config(text=f"Solved in {len(solution)} moves!", fg='green')
            self.solve_button.config(state=tk.NORMAL)
            self.reset_button.config(state=tk.NORMAL)
            return
        
        row, col = solution[step]
        self.toggle_cell(row, col)
        self.status_label.config(text=f"Step {step + 1}/{len(solution)}: Click ({row}, {col})", 
                                fg='blue')
        
        # Schedule next step after 500ms
        self.master.after(500, lambda: self.show_solution(solution, step + 1))
    
    def reset_game(self):
        """Reset the game board to start state"""
        self.state = self.start_state
        self.draw_board()
        self.status_label.config(text="Board reset to start state. Click squares to toggle lights", fg='black')



if __name__ == "__main__":
    start = (
        (0, 1, 0, 0),
        (1, 0, 1, 0),
        (0, 1, 0, 1),
        (0, 0, 1, 0),
    )
    #print(pretty_state(start))
    #print()

    #solution_path = solve(start)
    #if not solution_path:
    #  print("No solution found.")

    #else:
    #  state = start 
    #  for move in solution_path: 
    #    print(move)
    #    state = toggle(state, *move)
    #    print(pretty_state(state)) 
    #    print()

    #print(f"Solved in {len(solution_path)} steps.")
    root = tk.Tk()
    game = LightsOutGUI(root, start)
    root.mainloop()




