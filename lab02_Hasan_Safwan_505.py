#Name : Safwan Ibne Hasan
#Course : 1411-505
#Date : 09/12/17

#Problem:
#Write a program that takes as input month and year, determines how many days are
#in the  month, and outputs the number of days

#Given:
#Thirty days are in April, June, September, and November.
#All the rest are 31 except for February which could be 28 or 29 depending 
#upon whether the year is a leap year or not.
#In general, a year is a leap year when it is evenly divisible by 4.
#Exceptions occur when the year is 
#also evenly divisible by 100 in which case the year would not be a leap year 
#unless it is evenly divisible by 400.

#Analysis:
#input: a month and a year
#output: the number of days in the month of the year

#Method/Algorithm:
#Introduce the Program
#Ask for a month and year
#Determine how many days are in the month
#accounting for leap year conditions
#Find the number of days in the input month of the input year
#Print the number of days in the input month of the input Year

#TEST CASES:
#Input: month - February
#       year  - 2000              
#Output: February 2000 has 28 days
#
#Input: month - February
#       year  - 2012
#Output: February 2012 has 28 days
#
#Input: month - February
#       year  - 2100
#Output: February 2100 has 29 days
#
#Input: month - September
#       year  - 2008
#Output: September 2008 has 30 days
#
#Input: month - August
#       year  - 2010
#Output: August 2010 has 31 days
#

#Program:
#introduce the program
print ("This program inputs the month and year, determines how many days are in the month, and outputs the number of days in that month of that year")
print (" Note: Use Capital letter for the first letter of the month")
#input user month and year from user
Month_stri = input('Enter a month: ')
Year_stri = int(input("Enter a year: "))


if Month_stri == 'January' or Month_stri == 'March' or Month_stri == 'May' or Month_stri == 'July' or Month_stri == 'August' or Month_stri == 'October' or Month_stri == 'December':
  days_int = 31
  
if Month_stri == 'April' or Month_stri == 'June' or Month_stri == 'September' or Month_stri == 'November':
  days_int = 30
  
if Month_stri == 'February':
  
#Account for Leap Year
  
  if (Year_stri % 4 == 0 and Year_stri % 100 !=0) or Year_stri % 400 == 0 :
   days_int = 28
  else:
    days_int = 29

#Print the output
print (Month_stri, Year_stri, "has", days_int, "days")

