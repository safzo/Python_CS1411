#Name: Safwan Ibne Hasan
#Course: 1411-505
#Date: 10/31/2017
#
#PROBLEM:
#Write a Python program to read the lottotexas.csv file into a dictionary
#Write a function to return a randomly generated 6-element integer set which represents one lotto ticket
#For each drawing in the dictionary, check the matching numbers between the randomly generated ticket and the drawing
#Total the winnings and report to the customer what s/he would have won had that ticket been played since the first reported 
#drawing in 1992
#Also let the customer know what they would have spent on the lotto tickets by checking the length of the dictionary

#GIVEN:
#csv file
#

#ANALYSIS:
#Input: Lotto ticket 6-integer set
#Output: Winnings and amount of money spent
#
#METHOD:
#Import modules
#Create a dictionary
#Fill in the dictionary with data from csv file
#Let the customer know if file could not be opened
#Write a function to return a randomly generated 6-element integer set
#Check the matching numbers between the randomly generated ticket and the drawing
#total the winnings
#Print out to the customer what s/he would have won


#TEST CASES:
#
#input: Your Texas Lotto ticket {1, 2, 3, 10, 43, 52}
#output: Your total winning from 1992 till 2017 is: $ 920
#       You would have spent $ 2605 on Texas lotto tickets from 1992 to 2017

#input:  Your Texas Lotto ticket {32, 2, 8, 11, 44, 49}
#output: Your total winning from 1992 till 2017 is: $ 892
#        You would have spent $ 2605 on Texas lotto tickets from 1992 to 2017

#input:  Your Texas Lotto ticket {35, 48, 51, 21, 22, 24}
#output: Your total winning from 1992 till 2017 is: $ 1034
#        You would have spent $ 2605 on Texas lotto tickets from 1992 to 2017

#Test case without csv file:
#input:  Your Texas Lotto ticket {35, 48, 51, 21, 22, 24}
#output: Sorry, the file could not be opened
#        Your total winning from 1992 till 2017 is: $ 0
#        You would have spent $ 0 on Texas lotto tickets from 1992 to 2017


#Main Program:

#Import modules
import csv
import random

#Create a dictionary
dictionary = {}
try:    
    lottotexas = open('lottotexas.csv','r')
    reader = csv.reader(lottotexas)

#Fill in the dictionary with data from csv file
    for row in reader:
        month = row [1]
        day = row [2]
        year = row [3]
        date = month + '/' +day + '/'+ year
        my_set = set ()
        for i in range(4,10):
            my_set.add(int(row[i]))
        dictionary [date] = my_set

#Let the customer know if file could not be opened
except:
    print("Sorry, the file could not be opened")

#Write a function to return a randomly generated 6-element integer set
def ticketmaker():
    ticket = set()
    for i in range(4,10):
        ticket.add(random.randint(1,54))

    return ticket

#Check the matching numbers between the randomly generated ticket and the drawing
ticket = ticketmaker()
print ("Your Texas Lotto ticket", ticket)
#total the winnings
money = 0
for value in dictionary.values():
    matchmaker = value.intersection(ticket)
    if len(matchmaker) == 2:
        money += 2
    elif len(matchmaker) == 3:
        money += 10
    elif len(matchmaker) == 4:
        money += 100
    elif len(matchmaker) == 5:
        money += 10000
    elif len(matchmaker) == 6:
        money += 100000

#Print out to the customer what s/he would have won
print("Your total winning from 1992 till 2017 is: $", money)
print("You would have spent $", len(dictionary) , "on Texas lotto tickets from 1992 to 2017")



    
