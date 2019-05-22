#Name: Safwan Ibne Hasan
#Course:    1411-505
#Date:    9/19/2017
#
#PROBLEM:
#Implement the Russian Peasant or Ancient Egyptian method for multiplication
#
#GIVEN:
#None
#
#ANALYSIS:
#Input: Two integers
#Output: Product of the two integers
#
#METHOD/ALGORITHM:
#Introduce the program
#Prompt an integer A from the user
#Prompt an integer B from the user
#Everytime (B/2) is odd, add integer A to the result untill B is zero
#Multiply A by 2
#Print the result and prompt user if they want to multiply again
#
#TEST CASES:
#Input:  Integer A: 2
#        Integer B: 2
#Output: 2 times 2 is 4 in 2 iteration(s)
#
#Input:  Integer A: 25
#        Integer B: 18
#Output: 25 times 18 is 450 in 5 iteration(s)
#
#Input:  Integer A: 70
#        Integer B: 48
#Output: 70 times 48 is 3360 in 6 iterations(s) 
#
#PROGRAM:

#inputs an integer from the user
def input_integer (prompt_str):
    requested_bool = False
    while not requested_bool:
        in_str = input(prompt_str)
        if (in_str[0] == '+' or in_str[0] == '-') and in_str[1:].isdigit():
            number_int = int(in_str)
            requested_bool = True
        elif in_str.isdigit():
            number_int = int(in_str)
            requested_bool = True
        else:
            print(in_str, "is not an integer - try again!")
    return number_int

#Main Program:
#Introduce the program
print("This program is about implementing the Russian Peasant or Ancient Egyptian method for multiplication")

#Repeats Program
repeat = True
while repeat:
    #Collects Input
    int_A = input_integer ('Enter an integer A: ')
    int_B = input_integer ('Enter an integer B: ')

    A = int_A
    B = int_B
    result = 0
    iteration = 0

    #Algorithm
    while B > 0:
        if B % 2 == 1:
            result = result + A
        A = A * 2
        B = B / 2
        B = int( B )
        iteration = iteration + 1

    #Print results
    print (int_A, "times", int_B, "is", result, "in", iteration, "iteration(s)")
    repeat = input("Do you want to do this again (Y/N) ? NOTE: USE A LOWER CASE LETTER : ") == "y"

print("Alright then, have a good day!")







    
        
