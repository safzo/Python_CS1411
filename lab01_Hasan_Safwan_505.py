#Name: Safwan Ibne Hasan
#Course: 1411-505
#Date: 09/05/2017
#
#PROBLEM:
#Given a number which is an integer, add 2 to that number, multiply by
#3, substract 6, and divide by 3.
#Finally, output the result of EACH calculation. You should get the number
#with which you started.
#
#GIVEN:
#The number is an integer
#
#ANALYSIS:
#Input: integer number
#Output: user integer input
#
#METHOD/ALGORITHM:
#introduce the program
#get input user_integer from user
#add 2 to the user_integer
#print user_integer
#multiply user_integer by 3
#print user_integer
#substract user_integer by 6
#print user_integer
#divide user_integer by 3
#print user_integer
#99009
#TEST CASES:
#Input: 5
#Output: 7, 21, 15, 5.0
#
#Input: 7
#Output: 9, 27, 21, 7.0
#
#Input:15
#Output: 17, 51, 45, 15.0
#
#PROGRAM:
#introduce the program
print ('This program inputs the integer number from the user and')
print ('adds 2, multiplies it by 3, substracts it by 6 and divides it by 3 and')
print ('outputs the result of EACH calculation')
#input user integer from user
integer = int(input( 'Enter any integer number: '))
integer = integer + 2
print (integer)
integer = integer* 3
print (integer)
integer = integer - 6
print (integer)
integer = integer / 3
print (integer)
print ('You got the number your started with!')




