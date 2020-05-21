import random

def main():
    print("Hello, what is your name?")
    name = input("Enter your name here: ")
    rang = input("This is a guess-the-number game - enter a range, comma separated: ")
    rang = rang.split(',')
    rang[0],rang[1] = int(rang[0]),int(rang[1])
    print("\nWell, %s, I am thinking of a number between 1 and 20. Take a guess.\n"%name)
    correct = random.randint(rang[0],rang[1])
    try:
        guess = int(input("Enter guess here: "))
    except:
        print("Invalid - not a number, try again\n")
    if guess==correct:
        print("YOU'RE RIGHT!!!")
    elif guess > correct:
        print("Your guess is too high, try again.\n")
    elif guess < correct:
        print("Your guess is too low, try again.\n")
    while(True):
        if guess==correct:
            print("YOU'RE RIGHT!!!")
            break
        elif guess > correct:
            print("Your guess is too high, try again.\n")
        elif guess < correct:
            print("Your guess is too low, try again.\n")
        try:
            guess = int(input("Enter guess here: "))
        except:
            print("Invalid - not a number, try again\n")


main()