# LibraryDatabaseSystem
A Python console application that helps a city library track book lending, calculate late fees, and search borrower records. Built as a class project for COP1000 – Introduction to Programming.
Features

Add borrowing records – Capture borrower name, phone number, book title, category, days borrowed, and daily fee rate
Display all records – View every record currently stored in the system
Search by phone number – Look up a specific borrower's record using their 10-digit phone number
Late fee calculation – Automatically calculates total late fees based on days borrowed and the daily rate
Summary statistics – On exit, displays total records, total late fees collected, and the average late fee
Full input validation – Every user input is validated before being accepted (names, phone numbers, days, fee rates, and menu selections)

How It Works
The program uses parallel arrays (lists) to store up to 100 borrowing records. A menu-driven loop lets the user add records, view records, or search — and the program won't accept bad input at any step.
How to Run

Make sure you have Python 3 installed
Download or clone this repository
Open a terminal and navigate to the folder where the file is saved
Run the program:

bashpython CityLibrarySystemv2.py

Note: Depending on your system, you may need to use python3 instead of python.

What I Learned
This project reinforced core programming concepts including:

Input validation with while loops
Parallel arrays for structured data storage
Modular design using functions
Linear search algorithms
Menu-driven program flow

Acknowledgments
I used Claude by Anthropic as a learning resource when I got stuck. All code was written by me — Claude was used strictly as a tool for understanding concepts, not for generating code.
Author
Collin Fryman
COP1000 – April 2026
