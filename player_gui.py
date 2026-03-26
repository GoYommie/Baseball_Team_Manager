"""
player_gui.py

This file creates the graphical user interface (GUI) for the Baseball Team Manager program.

It allows the user to:
- Retrieve a player by ID
- View player details
- Update player information
- Add a new player
- Cancel unsaved changes

The GUI is built using Tkinter and connects to the database through db.py.
"""

import tkinter as tk
from tkinter import messagebox
import db

# This variable keeps track of the player currently loaded from the database
current_player = None


def clear_fields():
    """
    Clears all input fields in the form.
    """
    # I used this function so I can reuse it whenever I need to reset the form
    entry_first.delete(0, tk.END)
    entry_last.delete(0, tk.END)
    entry_pos.delete(0, tk.END)
    entry_ab.delete(0, tk.END)
    entry_hits.delete(0, tk.END)

    # batting average field is read-only, so I temporarily enable it to clear it
    entry_avg.config(state="normal")
    entry_avg.delete(0, tk.END)
    entry_avg.config(state="readonly")


def show_player(row):
    """
    Displays player data from the database in the GUI fields.

    Parameters:
        row (tuple): A row retrieved from the database
    """
    clear_fields()  # clear previous values first

    # populate fields using row index positions from database
    entry_first.insert(0, row[2])
    entry_last.insert(0, row[3])
    entry_pos.insert(0, row[4])
    entry_ab.insert(0, row[5])
    entry_hits.insert(0, row[6])

    # calculate batting average
    at_bats = row[5]
    hits = row[6]

    # avoid division by zero
    if at_bats == 0:
        avg = 0.0
    else:
        avg = round(hits / at_bats, 3)

    # display batting average (read-only field)
    entry_avg.config(state="normal")
    entry_avg.insert(0, f"{avg:.3f}")
    entry_avg.config(state="readonly")


def get_player():
    """
    Retrieves a player using the entered Player ID and displays the data.
    """
    global current_player

    player_id = entry_id.get().strip()

    # check if ID is a valid number
    if not player_id.isdigit():
        messagebox.showerror("Error", "Invalid player ID.")
        clear_fields()
        return

    # get player from database
    row = db.get_player(int(player_id))

    # if no player is found
    if row is None:
        messagebox.showerror("Error", "Player not found.")
        clear_fields()
        current_player = None
        return

    # store player so we can update or cancel later
    current_player = row
    show_player(row)


def save_changes():
    """
    Saves updated player information back to the database.
    """
    global current_player

    # make sure a player is loaded first
    if current_player is None:
        messagebox.showerror("Error", "No player loaded.")
        return

    # get values from input fields
    player_id = int(entry_id.get().strip())
    first_name = entry_first.get().strip()
    last_name = entry_last.get().strip()
    position = entry_pos.get().strip().upper()
    at_bats = entry_ab.get().strip()
    hits = entry_hits.get().strip()

    # basic validation checks
    if first_name == "" or last_name == "" or position == "":
        messagebox.showerror("Error", "First name, last name, and position are required.")
        return

    if not at_bats.isdigit() or not hits.isdigit():
        messagebox.showerror("Error", "At bats and hits must be whole numbers.")
        return

    at_bats = int(at_bats)
    hits = int(hits)

    # logical validation
    if hits > at_bats:
        messagebox.showerror("Error", "Hits cannot be greater than at bats.")
        return

    # update database with new values
    db.update_player(player_id, first_name, last_name, position, at_bats, hits)

    # reload updated data
    row = db.get_player(player_id)
    current_player = row
    show_player(row)

    messagebox.showinfo("Success", "Player data updated successfully.")

    # clear form after saving
    clear_fields()
    entry_id.delete(0, tk.END)
    current_player = None


def cancel_changes():
    """
    Cancels any unsaved changes and restores original player data.
    """
    global current_player

    # if no player is loaded, just clear form
    if current_player is None:
        clear_fields()
        return

    # reload original data
    show_player(current_player)



# -----------------------------
# GUI setup
# -----------------------------
window = tk.Tk()
window.title("Player")

# labels and input fields
tk.Label(window, text="Player ID:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_id = tk.Entry(window, width=20)
entry_id.grid(row=0, column=1, padx=10, pady=5)

# button to get player
btn_get = tk.Button(window, text="Get Player", command=get_player)
btn_get.grid(row=0, column=2, padx=10, pady=5)

tk.Label(window, text="First name:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_first = tk.Entry(window, width=30)
entry_first.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text="Last name:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_last = tk.Entry(window, width=30)
entry_last.grid(row=2, column=1, padx=10, pady=5)

tk.Label(window, text="Position:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_pos = tk.Entry(window, width=30)
entry_pos.grid(row=3, column=1, padx=10, pady=5)

tk.Label(window, text="At bats:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
entry_ab = tk.Entry(window, width=30)
entry_ab.grid(row=4, column=1, padx=10, pady=5)

tk.Label(window, text="Hits:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
entry_hits = tk.Entry(window, width=30)
entry_hits.grid(row=5, column=1, padx=10, pady=5)

tk.Label(window, text="Batting Avg:").grid(row=6, column=0, padx=10, pady=5, sticky="e")
entry_avg = tk.Entry(window, width=30, state="readonly")
entry_avg.grid(row=6, column=1, padx=10, pady=5)

# buttons for actions
btn_save = tk.Button(window, text="Save Changes", command=save_changes)
btn_save.grid(row=7, column=0, padx=10, pady=10)

btn_cancel = tk.Button(window, text="Cancel", command=cancel_changes)
btn_cancel.grid(row=7, column=1, padx=10, pady=10)

# start the GUI
window.mainloop()