# assignment: programming assignment 1
# author: Shreya Hiremath
# date: 06/27/2022
# file: hello.py is a program that asks the user to enter user's name,
#       age, and favorite movie and outputs a greeting message that
#       include the information about the user
# input: string data
# output: string data

# use input statements to make prompts (ask questions)
# use a variable age as an integer data type (you should use integer casting)

# use print statements to output user data

# use f-strings or string formatting methods
# use string concatenation and string casting

name = input("Hello! What is your name? \n")


age = int(input("What is your age? \n"))


favorite_movie = input("What is your favorite movie? \n")


print(f'Nice to meet you, {name}.\n')


print("You will be", str(age+1), "years old next year, and your favorite movie is",favorite_movie+".")
