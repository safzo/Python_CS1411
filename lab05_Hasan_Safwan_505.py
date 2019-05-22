#Name: Safwan Ibne Hasan
#Course: 1411-505
#Date: 10/10/2017
#
#PROBLEM:
#Write a program to enable a user to create a web page. Prompt the user for the name of the webpage file and its contents.
#
#GIVEN:
#html conversion examples
#
#ANALYSIS:
#Input: Webpage filename, webpage title, text lines, images, bolded lines, lines with a new color and menu choices
#Output: Get a html based file with all the above inputs
#
#METHOD:
#Get a file name that does not exist
#Print menu and get user choice
#Prompt user for an image
#Carry out the main program
#Complete the html ending tags
#Print the results

#TEST CASES:
#(1)
#<html>
#<head>
#<title>helloworld</title>
#</head>
#<body>
#<p>
#Hello world!<br/>
#<img src = "pexels-photo-356830.jpeg"><br/>
#<b>Bright Lights!</b><br/>
#<font color = "indigo">Beautiful Sky</font><br/>
#</p>
#</body>
#</html>

#(2)
#<html>
#<head>
#<title>rockstar</title>
#</head>
#<body>
#<p>
#Post Malone<br/>
#<img src = "post-malone-rockstar-21-savage.jpeg"><br/>
#<b>Singles Album</b><br/>
#<font color = "Pink">21 Savage</font><br/>
#</p>
#</body>
#</html>


#Get a File name that does not exist
def creator(prompt):
    good_filename = False
    while not good_filename:
        filename = input(prompt)
        try:
            fileA = open(filename,'r')
            fileA.close()
            print("That file already exists - please try again")
            
        except IOError:
            good_filename = True
    return filename

#Print Menu and Get User Choice
def get_menu_choice ():
    print('\nWeb Page Additional Menu Choices')
    print('[t]ext line')
    print('[i]mage')
    print('[b]old text line')
    print('[c]olor text line')
    print('[e]xit')
    
    good_menu_choice = False
    while not good_menu_choice:
        choice = input('Enter menu choice [t,i,b,c,e]: ')
        if choice != 't' and choice != 'i' and choice != 'b' and choice != 'c' and choice != 'e':
            print(choice,'is invalid - please try again')
        else:
            good_menu_choice = True
    return choice

#Prompt user for an Image
def get_filename_for_image (prompt):
    good_filename = False
    while not good_filename:
        image = input(prompt)
        try:
            imgA = open(image, 'r')
            imgA.close()
            good_filename = True
        except IOError:
            print(image,'could not be found- please try again')
    return image

#Main Program
print ("Welcome to the Web-Page Creator program")
filename = creator("Please enter a filename for the name of the web-page: ")

body = '<html>\n<head>\n<title>'
web_page_title = input("Please enter the web page title: ")
body += web_page_title
body += '</title>\n'
body += '</head>\n'

body += '<body>\n'
body += '<p>\n'

user_menu_choice = ''
while user_menu_choice != 'e':
    user_menu_choice = get_menu_choice()
    if user_menu_choice == 't':
          body += input("Please Enter a line of text for your webpage: ")
          body += '<br/>\n'
          
    elif user_menu_choice == 'i':
          body += '<img src = "'
          body += get_filename_for_image("Please select an image for your webpage: ")
          body += '"><br/>\n'
          
    elif user_menu_choice == 'b':
          body += '<b>'
          body += input("Please enter a line of text to be bolded for your webpage: ")
          body += '</b><br/>\n'
          
    elif user_menu_choice == 'c':
          body += '<font color = "'
          body += input('Please enter a font color: ')
          body += '">'
          body += input('Please enter a line of text for the new font color: ')
          body += '</font><br/>\n'
          
    else:
         print("\nPreparing your webpage")

#html ending tags
body += '</p>\n'
body += '</body>\n'
body += '</html>\n'
file = open(filename, 'w')
file.write(body)
file.close()

#Print your results
print ("Your webpage is now in" ,filename)
print ("Enjoy your new webpage")
