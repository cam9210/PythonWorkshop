wrong_guesses = list()
correct_guesses = list()

word = "something"
word = word.lower()
word_letters = [x for x in word]
correct_letters = ['*'] * len(word_letters)

num_of_correct = 0
num_of_guesses = 5

while True:
    print('')
    if num_of_correct == len(word_letters):
        print("You win!")
        break
    elif num_of_guesses == 0:
        print("You lose!")
        print("The word was: " + word)
        break

    counter = 0
    print("wrong guesses: ",end='')
    print(' '.join(wrong_guesses))
    print("number of guesses left: ", end='')
    print(num_of_guesses)
    print("your word: ", end='')
    print(''.join(correct_letters))

    letter = input("Please choose your next letter: ")
    letter = str(letter)
    letter = letter.lower()

    if not letter.isalpha():
        print(letter + " is not a valid letter.")
        continue
    elif len(letter) > 1:
        print("Only input one letter at a time.")
        continue
    elif letter in wrong_guesses:
        print("You already guessed that letter.")
        continue

    for index, item in enumerate(word_letters):
        if item == letter:
            counter += 1
            correct_letters[index] = letter

    if counter == 0:
        print("Letter does not exist in word.")
        wrong_guesses.append(letter)
        num_of_guesses -= 1
    else:
        num_of_correct += counter
