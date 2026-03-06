
## ⚾ Baseball Team Manager

CPRO 2201 – Python Programming II
Midterm Project
Red Deer Polytechnic

Author: Adeyomi Solomon
Project Type: Console-Based Python Application
Language: Python 3
-------------------------------------------------


## Project Overview
The Baseball Team Manager is a console-based Python application that allows users to manage a baseball team lineup. This project implements Sections 1–3 of the case study of Murach's python programming 11 and demonstrates the use of Object-Oriented Programming (OOP) principles in Python.

The program allows users to:

•	View the team lineup
•	Add new players
•	Remove players
•	Move players to different lineup positions
•	Edit a player’s position
•	Edit a player’s statistics
•	Automatically calculate batting averages
•	Save all changes to a file so data is not lost

## Project Development Progression

Section 1 – Procedural Implementation
The first version of the program was written using procedural programming. Functions were used to manage the lineup and player data was stored in a CSV file.

Section 2 – Program Enhancements
The second stage improved the design and usability of the program. Enhancements included improved input validation, better output formatting, and additional helper functions.

Section 3 – Object-Oriented Programming (OOP)
The final stage converted the program into an object-oriented design using a Player class and a Lineup class to manage player information and lineup operations.

## Program Architecture

User Interface Layer (ui.py)
•	Handles interaction with the user including menus and input.
    Business Logic Layer (objects.py)
•	Contains Player and Lineup classes that manage program logic.

Data Access Layer (db.py)
•	Handles reading and writing player data to players.csv.

Program Entry Point (main.py)
•	Starts the application and launches the user interface.

## Project Structure

main.py – program entry point
ui.py – user interface functions
objects.py – Player and Lineup classes
db.py – CSV file handling
players.csv – player data storage
README.md – project documentation

## How to Run the Program

1. Make sure Python 3 is installed on your computer.
2. Open a terminal in the project folder.
3. Run the program using: python main.py
4. Follow the menu options displayed on the screen.

## Version Control

This project is maintained using Git and GitHub. Commits track the progression from procedural implementation to enhanced functionality and finally the object-oriented design.



