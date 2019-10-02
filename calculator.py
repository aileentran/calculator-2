"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

# No setup
# repeat forever:

#     read input
#     tokenize input
#     if the first token is "q":
#         quit
#     else:
#         decide which math function to call based on first token



#mental dump 



#loop through - asking USER for calculations 
while True:
    #split the string --> individual (math op, num1, num2- maaaybe)
    user_input = input("> ")
    tokens = user_input.split(" ") #[op, num1, num2 -maybe]
    op = tokens[0]
    
    if len(tokens) == 3:
        num1 = float(tokens[1])
        num2 = float(tokens[2])
    
    elif len(tokens) == 1:
        num1 = None

    elif len(tokens) < 3:
        num2 = None


    if op == "+":
        print(add(num1, num2))
    elif op == "-":
        print(subtract(num1, num2))
    elif op == "*":
        print(multiply(num1, num2))
    elif op == "/":
        print(divide(num1, num2))
    elif op == "square":
        print(square(num1))
    elif op == "cube":
        print(cube(num1))
    elif op == "pow":
        print(power(num1, num2))
    elif op == "mod":
        print(mod(num1, num2))
    elif op == "q":
        break






#checking for operator AND q
#string[0] <-- operator, match with approp. function in arith
#feed num1 and num2 into functions (how?? forgot lol!)
#PRINT(?) the value 
#if user inputs q -> break or return (?)


