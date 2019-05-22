#Name: Safwan Ibne Hasan
#Course: 1411-505
#Date: 10/17/2017
#
#PROBLEM:
#Write a recursive helper function called writeChars that accepts an integer parameter n and prints out a string returned by another recursive method that is called by writeChars 
#
#GIVEN:
#recursive helper function test examples
#
#ANALYSIS:
#Input: Entering an integer number for string size
#Output: Resulting string
#
#METHOD:
#Write a function to help print recursive calls
#Write a recursive function to create string
#Prompt user for a valid size
#Print out results
#prompt user to use program again

#TEST CASES:
#input: 5
#ouput: <<*>>

#input: 8
#output: <<<**>>>

#input: -10
#output:

#input: 50
#output: <<<<<<<<<<<<<<<<<<<<<<<<**>>>>>>>>>>>>>>>>>>>>>>>>

#Program:
#function to help print recursive calls:

def printstring(n):
    print('The string is:', printstringrecur(n,0))
    
#recursive function to create string:
    
def printstringrecur (n,index):
    if index >= n:
        return ''
    elif index == n//2 or (index == n/2-1 and n % 2 == 0):
        return ('*' + printstringrecur(n,index+1))
    elif index < n//2:
        return ('<' + printstringrecur(n,index+1))
    elif index > n//2:
        return ('>' + printstringrecur(n,index+1))

#Prompt user for a valid size:            
def get_valid_size (prompt):
    valid_size = False
    while not valid_size:
        size = input(prompt)
        #Exception handling:
        try:
            size = int(size)
            valid_size = True
        except ValueError:
            print(size,'is not valid- please try again')
    return size
    

#Main Program:
print("Welcome to the string printing program!")
       
#repeating the program
repeat = True
while repeat:
    #ask user for a integer number:
    size = get_valid_size("Enter an integer for the string size:")
    printstring(size)
    #ask if user wants to enter another number:
    again = input("Would you like to enter another number (y/n) ? NOTE: USE A LOWER CASE LETTER : ")
    while again!= "y" and again!= "n":

    #incorrect input identifier:
        again =input("That is not a valid answer, is it 'y' or 'n'? ")
    repeat = again == "y"

#print a farewell statement if user doesn't want to enter another number:
print("Alright then, have a good day!")




                   

