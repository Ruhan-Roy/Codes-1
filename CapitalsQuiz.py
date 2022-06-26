def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Correct!')
            score = score + 1
            still_guessing = False

        else:
            if attempt < 2:
                guess = input('Sorry wrong answer.Try Again.')
            attempt = attempt + 1

    if attempt == 3:
        print('The correct Answer is ' + answer)
score = 0
print('Answer the following questions!')
guess1 = input('What is the capital of Canada?')
check_guess(guess1, 'Toronto')
guess2 = input('What is the capital of Egypt?')
check_guess(guess2, 'Cairo')
guess3 = input('What is the capital of Australia?')
check_guess(guess3, 'Canberra')
guess4 = input('What is the capital of Belgium?')
check_guess(guess4, 'Brussels')
guess5 = input('What is the capital of Switzerland?')
check_guess(guess5, 'Bern')
guess6 = input('What is the capital of Argentina?')
check_guess(guess6, 'Buenos-aires')
guess7 = input('What is the capital of New Zealand?')
check_guess(guess7, 'Auckland')
guess8 = input('What is the capital of Italy?')
check_guess(guess8, 'Rome')
guess9 = input('What is the capital of Greece?')
check_guess(guess9, 'Athens')
guess10 = input('What is the capital of Japan?')
check_guess(guess10, 'Tokyo')
print('Your score is:' + str(score), 'out of 10')