#for/while loop problem - (Hint use both)
# Write a program that takes in a line of text as input, and outputs that line of text in reverse. 
# The program repeats, ending when the user enters "Quit", "quit", or "q" for the line of text.

# Ex: If the input is:

# Hello there
# Hey
# quit

# then the output is:

# ereht olleH
# yeH

#Try this yourself! if you are stuck, the solution is commented on line 35
#to uncomment, highlight the code and press Ctrl + k + u (only works for visual studio code)

















# #Solution
# user_text = input()

# while(user_text != 'Quit' and user_text != 'quit' and user_text != 'q'):
#     rev = list(reversed(user_text))
#     for i in rev:
#         print(i, end="")
#     print()
#     user_text = input()