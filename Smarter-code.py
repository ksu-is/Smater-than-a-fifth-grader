def main():
    print("Hello!")
    userName = input("Enter your name: ")
    print(userName + ", are you smarter than a fifth grader?")
    print(
        "You'll be tested on your math skills today. Please confirm this by "
        "entering the subject you're interested in below.")
    subject = input("Your subject today is: ")
    while subject not in ("math", "Math"):
        print(
            "That is not the subject you're being tested on. Please choose "
            "again.")
