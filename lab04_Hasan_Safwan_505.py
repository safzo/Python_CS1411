#Name: Safwan Ibne Hasan
#Course:    1411-505
#Date:    9/26/2017
#
#PROBLEM:
#Write a program to prompt the user for a message that the program will encrypt
#and then decrypt (reverse the encryption process). Utilize the encryption method
#in a way that the ciphertext becomes the even letters followed by the odd letters
#in the message. In addition, write a function for inputting a 'y' or 'n' with
#incorrect input checking.
#

#GIVEN:
#Transposition cipher method explained
#

#ANALYSIS:
#Input: A string to be encrypted
#Output: > Encrypted string as a ciphertext with even letters followed by the odd letters
#        in the message.
#        > Decrypted string
#

#METHOD/ALGORITHM:
#Introduce the program
#Ask for a string to be encrypted
#Encrypt the string as a ciphertext using the transposition cipher method
#print the encryption result as even letters followed by the odd letters in the message
#Decrypt the string as well
#Ask if the user wants to input another string to be encrypted, with incorrect input checking
#Decrypt the string if input is "y"
#End the program if input is "n"
#
#
#TEST CASES:
#Input: abc
#Output: The ciphertext is: bac
#        The message decrypted is: abc
#
#Input: 
#Output: The ciphertext is: The World is a beautiful place!!!
#        The message decrypted is: h ol sabatflpae!TeWrdi  euiu lc!!
#
#Input: 
#Output: The ciphertext is: B A S K E T B A L L   I S   L I F E !
#        The message decrypted is: BASKETBALL IS LIFE!                   
#

#Main Program:
#Introduce the program
print("Welcome to the encryption program!")

#Repeats Program
repeat = True
while repeat:
    
    #Message Encryption
    message = input( "Enter a string to encrypt: ")
    even = message [1: :2]
    odd = message [0: :2]
    
    #Print results for Encryption
    print ("The ciphertext is:", even+odd)

    #Message Decryption
    decryption = ""
    count = 0
    while count < len(message):
        if count % 2 == 1:
            decryption = decryption + even[0]
            even = even[1:]
        else:
            decryption = decryption + odd[0]
            odd = odd[1:]
        count += 1
    #print results for Decryption
    print( "The message decrypted is: ", decryption)
        

    #incorrect input identifier
    again = input("Would you like to encrypt another message (Y/N) ? NOTE: USE A LOWER CASE LETTER : ")
    while again!= "y" and again!= "n":

        again =input("That is not a valid answer, is it 'y' or 'n'? ")
    repeat = again == "y"

#print a farewell statement if user doesn't want to encrypt another message
print("Alright then, have a good day!")







    
        
