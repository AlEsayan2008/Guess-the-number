import random
def guess_number(n):
    random_number = random.randint(0, n)
    User_guess = int(input("\nEnter your number:\n"))
    if User_guess != random_number:
        if User_guess > random_number:
            print("\nOhh your guess is wrong: Too high\n")
        elif User_guess < random_number:
            print("\nOhh your guess is wrong: Too low\n")
    else:
        print(f"\nYeah man.Your number: {User_guess} is equal to random number: {random_number}.\n")
#for example i give "n" => 10
n = 10

#Now I create infinity loop using while loop for infinity play.
while True:
    guess_number(n)
