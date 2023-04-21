winning_number = int(input("Enter winning number:-"))
guess = 1
number = int(input("guess a number between 1 and 100:-"))
game_over = False
while not game_over:
    if number==winning_number:
        print("you win and you guessed this number in %d times"%guess)
        game_over=True
    else:
        if number<winning_number:
            print("too low")
            guess = guess+1
            number = int(input("guess again:-"))
        else:
            print("too high")
            guess = guess+1
            number = int(input("guess again:-"))
            
