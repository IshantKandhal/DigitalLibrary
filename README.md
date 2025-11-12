📚 Library Management System (Python CLI)

A simple command-line-based Library Management System built in Python.
It allows users to explore a list of famous books, read short summaries, or open their online versions directly in the browser.

🧩 Project Breakdown


1️⃣ Import Section
import webbrowser


The webbrowser module is used to open book links (PDFs or online versions) in the default browser.

2️⃣ Welcome Section
print("Welcome to Library Management System!!!!!!!")
print("Choose 0 for exit and 1 for continue")
a = int(input("Enter your choice : "))


Displays a welcome message.

Asks user whether they want to continue (1) or exit (0).

3️⃣ Main Function: choice(choice)

This function manages the overall flow of the program.

Case 1 → User enters 0
if choice == 0:
    print("Thanks for visiting!!!")
    quit()


Exits the system gracefully.

Case 2 → User enters 1
elif choice == 1:
    print("1 = Atomic Habit")
    print("2 = Mahabharata")
    print("3 = Ramayana")
    print("4 = Bhagavad Gita")
    print("5 = The Power of Now by Eckhart Tolle")


Displays a list of available books.

Prompts user to pick a book (1–5).

Calls the nested book(n) function.

Invalid Choice
else:
    print("Invalid choice chosen!")


Shows error message if user input is not 0 or 1.

4️⃣ Nested Function: book(n)

Handles all logic related to a selected book.
Each book gives two options:

print("Choose 1 for basic description and 2 for online reading")
c = int(input("Enter your choice : "))


1 → Prints a summary of the book.

2 → Opens the online reading link using webbrowser.open().

5️⃣ Book Options Breakdown
Option	Book Title	Description Summary	Online Reading Link
1	Atomic Habits	Small, consistent habits lead to massive success. Focuses on self-improvement and habit formation.	Read Online

2	Mahabharata	Ancient Indian epic exploring duty, morality, and human nature.	Read Online

3	Ramayana	Story of Lord Rama, Sita, and the triumph of good over evil.	Read Online

4	Bhagavad Gita	Conversation between Lord Krishna and Arjuna about life, duty, and wisdom.	Read Online

5	The Power of Now	Teaches mindfulness and being present to overcome anxiety and regret.	Read Online


6️⃣ Invalid Input Handling

The program checks for invalid inputs in multiple stages:

Invalid main menu choice

Invalid book number

Invalid description/reading option

Each displays a friendly error message:

print("Invalid choice chosen!")

7️⃣ Exit Message

At the end of the flow:

print("Thanks for Visiting!!!!")


Displays a thank-you note when user finishes browsing.

🚀 How to Run the Program

Clone or download this repository.

Make sure Python 3.x is installed.

Run the script in your terminal:

python Library.py


Follow the on-screen menu.

🛠️ Requirements

Python 3.x

Internet connection (to open book links)

👨‍💻 Author - Ishant Kandhal
