"""
main.py

This file is the entry point of the Baseball Team Manager program.

Its main responsibility is to start the user interface layer of the
application. The UI module handles all interactions with the user
such as displaying menus, getting input, and performing actions
like adding or editing players.

The program starts running when this file is executed.
"""

import ui


# This condition ensures that the program runs only when
# this file is executed directly and not when it is imported
# as a module in another file.
if __name__ == "__main__":
    
    # Call the main function from the UI module
    # This starts the Baseball Team Manager program
    ui.main()