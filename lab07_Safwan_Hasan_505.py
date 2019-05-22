#Name: Safwan Ibne Hasan
#Course: 1411-505
#Date: 10/24/2017
#
#PROBLEMS:
#Write a function to take a 70-character string of Myers Briggs responses and return a list of the percentage of B's in each dimension.
#Write another function to take a list of percentages and return the Myers Briggs 4-Dimension types as single letters


#Given:
#Test cases for percentages and 4_dimensional types as single letters of Myers Briggs test


#ANALYSIS:
#Input: 70 character strings
#Output: Conversion of the strings into percentages and personality traits


#METHOD:
#Calculate percentage
#Count number of B's
#Find percentage
#Assign personality traits
#Type in the given inputs
#Prints out Percentage of B's in each dimension
#Prints out 4-Dimensional types as single letters

#TEST CASES:
#
#input: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#output: [0.0, 0.0, 0.0, 0.0]
#        ISTJ        
#
#input: BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
#output: [100.0, 100.0, 100.0, 100.0]
#        EIFP
#
#input: BABAAAABAAAAAAAABAAAABBAAAAAABAAAABABAABAAABABABAABAAAAAABAAAAAABAAAAA
#output: [30.0, 45.0, 10.0, 10.0]
#        ISTJ
#

#Program:

#Calculating Percentage
def percent_finder (count, total):
    percentage = ((count/total)*100)
    return percentage

#FIRST FUNCTION:
#Counting number of B's
def countBs(response):
    counter = 0
    for i in range (0, len(response)):
        if response[i] == 'B':
            counter += 1
    return counter

#Finding percentages
def find_response_percentages (response):
    first_dimension = countBs (response[::7])
    second_dimension = countBs (response[1::7] + response[2::7])
    third_dimension = countBs (response[3::7] + response[4::7])
    fourth_dimension = countBs (response[5::7] + response[6::7])
    
    return [percent_finder(first_dimension,10), percent_finder(second_dimension,20), percent_finder(third_dimension,20), percent_finder(fourth_dimension,20)]

#SECOND FUNCTION:
#Assigning the traits
def assigning_traits (alist):
    trait = ''
    if alist[0] < 50:
        trait += "I"
    else:
        trait += "E"
        
    if alist[1] < 50:
        trait += "S"
    else:
        trait += "I"

    if alist[2] < 50:
        trait += "T"
    else:
        trait += "F"

    if alist[3] < 50:
        trait += "J"
    else:
        trait += "P"
    return trait

#Given inputs
input01 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
input02 = "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
input03 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
input04 = "ABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABAB"
input05 = "BABAAAABAAAAAAAABAAAABBAAAAAABAAAABABAABAAABABABAABAAAAAABAAAAAABAAAAA"
input06 = "BABAAAABAAAAAAABAAAABBAAAAAABAAAABABAABAAABABAABAAABABABAABAAAAAABAAAA"
input07 = "AABBAABBBBBABABAAABAABABBAABBAAAABBBAAABAABAABABAAAABAABBBBAAABBAABABB"

#Prints out Percentage of B's in each dimension
print('Test 1:'+input01)
print('Result 1:',find_response_percentages(input01))
print('Test 2:'+input02)
print('Result 2:',find_response_percentages(input02))
print('Test 3:'+input03)
print('Result 3:',find_response_percentages(input03))
print('Test 4:'+input04)
print('Result 4:',find_response_percentages(input04))
print('Test 5:'+input05)
print('Result 5:',find_response_percentages(input05))
print('Test 6:'+input06)
print('Result 6:',find_response_percentages(input06))
print('Test 7:'+input07)
print('Result 7:',find_response_percentages(input07),'\n')

#Prints out 4-Dimensional types as single letters
print('Test 1:',find_response_percentages(input01))
a = assigning_traits(find_response_percentages(input01))
print('Result 1:',a)
print('Test 2:',find_response_percentages(input02))
a = assigning_traits(find_response_percentages(input02))
print('Result 2:',a)
print('Test 3:',find_response_percentages(input03))
a = assigning_traits(find_response_percentages(input03))
print('Result 3:',a)
print('Test 4:',find_response_percentages(input04))
a = assigning_traits(find_response_percentages(input04))
print('Result 4:',a)
print('Test 5:',find_response_percentages(input05))
a = assigning_traits(find_response_percentages(input05))
print('Result 5:',a)
print('Test 6:',find_response_percentages(input06))
a = assigning_traits(find_response_percentages(input06))
print('Result 6:',a)
print('Test 7:',find_response_percentages(input07))
a = assigning_traits(find_response_percentages(input07))
print('Result 7:',a)












