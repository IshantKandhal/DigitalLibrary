import webbrowser
print("Welcome to Library Management System!!!!!!!")
print("Choose 0 for exit and 1 for continue")
a = int(input("Enter your choice : "))
def choice(choice):
    if choice == 0:
        print("Thanks for visiting!!!")
        quit()
    elif choice == 1:
        pass
        print("1 = Atomic Habit")
        print("2 = Mahabharata")
        print("3 = Ramayana")
        print("4 = Bhagavad Gita")
        print("5 = The Power of Now by Eckhart Tolle")
        b = int(input("Enter number from 1-5 : "))
        def book(n):
            if n == 1:
                print("Choose 1 for basic description and 2 for online reading")
                c = int(input("Enter your choice : "))
                if c==1:
                    print("Atomic Habit:-")
                    print("Atomic Habits by James Clear explains how small, consistent changes lead to remarkable results. It focuses on building good habits, breaking bad ones, and mastering the tiny behaviors that drive lasting personal and professional growth through the power of compounding improvement.")
                elif c==2:
                    webbrowser.open("https://drive.google.com/file/d/1eAZMdXO-Zn4_90TV365KMpIqfxUy7J0t/view")
                else:
                    print("Invalid Choice!!!!")
            elif n == 2:
                print("Choose 1 for basic description and 2 for online reading")
                c = int(input("Enter your choice : "))
                if c==1:
                    print("Mahabharata:-")
                    print("One of the greatest epics of ancient India, the Mahabharata explores the moral struggles, family conflicts, and spiritual lessons surrounding the Kurukshetra war. It delves deeply into themes of duty, justice, fate, and the complexity of human nature, offering timeless wisdom for every generation.")
                elif c == 2:
                    webbrowser.open("https://www.holybooks.com/mahabharata-all-volumes-in-12-pdf-files/")
                else:
                    print("Invalid Choice!!!!")
            elif n == 3:
                print("Choose 1 for basic description and 2 for online reading")
                c = int(input("Enter your choice : "))
                if c==1:
                    print("Ramayana:-")
                    print("The Ramayana narrates the life of Lord Rama, his exile, the abduction of his wife Sita by Ravana, and the ultimate triumph of good over evil. It beautifully illustrates the values of righteousness, loyalty, devotion, and sacrifice, serving as a guide for ethical and spiritual living.")
                elif c==2:
                    webbrowser.open("https://ancient-buddhist-texts.net/English-Texts/Ramayana/Ramayana.pdf")
                else:
                    print("Invalid Choice!!!!")
            elif n == 4:
                print("Choose 1 for basic description and 2 for online reading")
                c = int(input("Enter your choice : "))
                if c==1:
                    print("Bhagavad Gita:-")
                    print("A philosophical dialogue between Lord Krishna and warrior Arjuna on the battlefield of Kurukshetra, the Bhagavad Gita imparts profound teachings on duty, selflessness, and spiritual enlightenment. It inspires individuals to find purpose, maintain balance, and act with wisdom amidst life’s challenges.")
                elif c==2:
                    webbrowser.open("https://drive.google.com/file/d/0B7JIaJnDZOlWdjE4OFNpanNUNXE5UHlrX0J6MWFyYW5vamlJ/view?resourcekey=0-f3vM8Vt27HiiNgeWMaXV6A")
                else:
                    print("Invalid Choice!!!!")
            elif n == 5:
                print("Choose 1 for basic description and 2 for online reading")
                c = int(input("Enter your choice : "))
                if c==1:
                    print("The Power of Now by Eckhart Tolle:-")
                    print("A modern spiritual classic, this book emphasizes the importance of living in the present moment to free oneself from anxiety and past regrets. Through practical insights and mindfulness, Tolle guides readers toward inner peace, clarity, and a deeper connection with their true selves.")
                elif c==2:
                   webbrowser.open("https://dn790003.ca.archive.org/0/items/ThePowerOfNowEckhartTolle_201806/The%20Power%20Of%20Now%20-%20Eckhart%20Tolle.pdf")
                else:
                    print("Invalid Choice!!!!")
            else:
                print("Invalid choice chosen!")
        book(b)
        print()
        print("Thanks for Visiting!!!!")
    else:
        print("Invalid choice chosen!")
        quit()
choice(a)
