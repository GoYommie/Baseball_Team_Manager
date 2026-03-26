import tkinter as tk
from tkinter import messagebox
import db

# This variable stores the last player data loaded from the database
current_player = None


def clear_fields():
    """
    Clears all text entry fields in the form.
    """
    entry_first.delete(0, tk.END)
    entry_last.delete(0, tk.END)
    entry_pos.delete(0, tk.END)
    entry_ab.delete(0, tk.END)
    entry_hits.delete(0, tk.END)
    entry_avg.config(state="normal")
    entry_avg.delete(0, tk.END)
    entry_avg.config(state="readonly")


def show_player(row):
    """
    Displays player data from the database in the text fields.
    """
    clear_fields()

    entry_first.insert(0, row[2])
    entry_last.insert(0, row[3])
    entry_pos.insert(0, row[4])
    entry_ab.insert(0, row[5])
    entry_hits.insert(0, row[6])

    # calculate batting average
    at_bats = row[5]
    hits = row[6]

    if at_bats == 0:
        avg = 0.0
    else:
        avg = round(hits / at_bats, 3)

    entry_avg.config(state="normal")
    entry_avg.insert(0, f"{avg:.3f}")
    entry_avg.config(state="readonly")


def get_player():
    """
    Gets a player by player ID and displays the data in the form.
    """
    global current_player

    player_id = entry_id.get().strip()

    if not player_id.isdigit():
        messagebox.showerror("Error", "Invalid player ID.")
        clear_fields()
        return

    row = db.get_player(int(player_id))

    if row is None:
        messagebox.showerror("Error", "Player not found.")
        clear_fields()
        current_player = None
        return

    current_player = row
    show_player(row)


def save_changes():
    """
    Saves edited player data back to the database.
    """
    global current_player

    if current_player is None:
        messagebox.showerror("Error", "No player loaded.")
        return

    player_id = int(entry_id.get().strip())
    first_name = entry_first.get().strip()
    last_name = entry_last.get().strip()
    position = entry_pos.get().strip().upper()
    at_bats = entry_ab.get().strip()
    hits = entry_hits.get().strip()

    if first_name == "" or last_name == "" or position == "":
        messagebox.showerror("Error", "First name, last name, and position are required.")
        return

    if not at_bats.isdigit() or not hits.isdigit():
        messagebox.showerror("Error", "At bats and hits must be whole numbers.")
        return

    at_bats = int(at_bats)
    hits = int(hits)

    if hits > at_bats:
        messagebox.showerror("Error", "Hits cannot be greater than at bats.")
        return

    db.update_player(player_id, first_name, last_name, position, at_bats, hits)

    # reload fresh data after saving
    row = db.get_player(player_id)
    current_player = row
    show_player(row)

    messagebox.showinfo("Success", "Player data updated successfully.")
    clear_fields()
    entry_id.delete(0, tk.END)
    current_player = None


def cancel_changes():
    """
    Restores the saved player data if the user cancels unsaved edits.
    """
    global current_player

    if current_player is None:
        clear_fields()
        return

    show_player(current_player)


# -----------------------------
# GUI setup
# -----------------------------
window = tk.Tk()
window.title("Player")

tk.Label(window, text="Player ID:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_id = tk.Entry(window, width=20)
entry_id.grid(row=0, column=1, padx=10, pady=5)

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

btn_save = tk.Button(window, text="Save Changes", command=save_changes)
btn_save.grid(row=7, column=0, padx=10, pady=10)

btn_cancel = tk.Button(window, text="Cancel", command=cancel_changes)
btn_cancel.grid(row=7, column=1, padx=10, pady=10)

window.mainloop()