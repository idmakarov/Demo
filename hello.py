"""

This is module performing simple scenario.
Bot asks you and you can write some answers in prompt.

"""

def hello():
    print("Hello, what is your name?")
    name = input("My name is ")
    print("Nice to meet you, {}!".format(name))

def hoay():
    print("How old are you?")
    b = 1
    while b:
        age = int(input("I'm "))
        if age <= 0:
            print("Nice joke, bro! Try again")
        elif age < 20:
            print("Cool, you're a teenager like me!")
            b = 0
        elif age >= 20 and age < 70:
            print("What are your favorite movies?")
            b = 0
        elif age < 120:
            print("Have you seen Elvis Presley?")
            b = 0
        else:
            print("You are either telling the truth (and you're quite old man)")
            print("or you are lying.")
            print("So, show me your papers, please!")
            # Need delay 5 sec
            print("Ok.")
            b = 0
