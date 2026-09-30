# Mini-Library-project
A Mini Library Management System is a simple Python program used to manage books in a library. It allows the user to add books, display available books, and search for a particular book. The program uses lists, functions, loops, and conditional statements to perform different library operations.
markdown

# Mini Library Management System

A lightweight console-based **Mini Library Management System built with Python to help manage a collection of books. Mini Library Management System allows users to add, search, track, issue and return books through an interactive command-line interface.

## 📖 Project Overview

Mini Library Management System is designed to simulate core library operations in a window. Mini Library Management System utilizes an in-memory python list to store book titles making it fast and completely dependency-free. Mini Library Management System serves as a demonstration of procedural programming, user-input handling and basic data manipulation in Python.


## ✨ Features

* Add Books: Append book titles directly to the library inventory.

* Display Inventory: List all available books with sequential numbering.

* Search Functionality: Instantly verify if a specific book exists in the library catalog.

* Issue System: Check out a book to remove it from the list.

* Return System: Add a checked-out book back into the system inventory.

* Interactive Terminal Menu: Clean user-friendly options with error handling for invalid selections.


## 🛠️ Technologies & Tools Used

* Language: Python 3.x

* Modules:None (Uses built-in features)

* Environment: Command Line / Terminal Interface


## 🚀 Steps to Install & Run

### Prerequisites

Make sure you have Python 3 installed on your machine. You can check your version by running

bash

python --version

### Installation

1. Clone or Download the project repository.

2. Navigate into the directory containing your python file:

    bash

cd path/to/your/project-directory

3. Save the code into a file named `library_system.py`.

### Running the Project

Execute the script using the following command in your terminal:

bash

python library_system.py


## 🧪 Instructions for Testing

To ensure Mini Library Management System works perfectly execute the following test cases in order after launching the application:

1. Test Display Empty: Select option `2`, after launching. Mini Library Management System should display: "No books."

2. Test Adding a Book: Select option `1` type a book name (*The Great Gatsby*) and press Enter. Mini Library Management System should print: "Book added successfully!"

3. Test Inventory Display: Select option `2` again. Verify Mini Library Management System displays: `1. The Great Gatsby`

4. Test Searching: Select option `3` type *The Great Gatsby*. Mini Library Management System should confirm: "Book is available."
