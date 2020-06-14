#    One of the simplest but most important things you need that ability to do in programming is display text.
    #For displaying text in Python you use the print() statement.
   # Your text inside prints brackets must be enclosed with quotes, Python accepts both single ‘ and double “ quotes.
   # For printing on multiple lines you could use multiple print statements or you can use \n which declares a new line for the text that follows it.
    #You can you triple quotes for the text to display, as you have typed it into the editor this is not a recommended method as most other programming languages don’t support it.
   # You will make mistakes when programming all programmers make mistakes from typing mistakes to logic mistakes, it is not something to stress over.
 #   Recommend solutions to fixing mistakes you can’t find or having trouble with: -# Walk away and come back to it,  # - Have another coder look at it; # Step though your code with your debugger. #you can use either single or double quotes within the bracket but be sure to be consistent. #\n brings the part after it to the next line


print ('hello world ')
print ("I am trying to program")

#displaying text in different ways
print ('look here and there and \nyou will find it')

#you can also produce the same effect as \n by typing it on diff lines. You must enclose it in triple quotes for this to happen

print ("""the horse clears the hurdle
but falls into the stream""")

#you can join two strings with a + and get it to act like one long string. Example

print ( 'I love to read books'+'it matters not whether it is a physical book or an e-book')

# let's see how diff set of quotes work within the bracket--back slash is an escape and a special character
print (' I want to see this work" + "but wll it is the question')
print (' hi there! \" " hope ur okay')

#this inserts the slash inside the string
print (' hope this works \ and you see the slash')

#what happens with a \\--here \n is treated as a new line whereas we wanted near----on the nxt line. To do this use a \\ -double backslash


print (' I wonder if a double slash \near the other  will do the same thing')
print ('this keeps getting quirkier \\nearer the new one')



#expecting input and intro to variables


#collect name from user
name = input ('what is your name')
name= 'mini'
#display the name
print (name)

#update value
name= 'preethu'
print (name)

name='kutti preethu'
print (name)


#this challenge requires you to print the poem on different lines--I used \n and it worked. 

print( ' There was once a movie star icon \n who preferred to sleep with the light on \nThey learned how to code \nA device that sure glowed \nAnd lit up the night using python')

print (' how many times do we look at the sky \n how many times do we say goodbye \n how many times do we sing in the rain \n how many times do we walk in the plain')


#using the input command in strings
firstName = input('what is your first name')
lastName = input ('what is your last name')
birthplace = input ('where do you live')
destination = input ( 'where do you go every week')
print ('come here' + firstName + lastName)
print ('copy ' + 'and add' + firstName +lastName + ' to the clipboard')
print (firstName + " " +lastName + " "  'lives in' " " + birthplace + " " 'but goes away every week to'+destination)



#calculating the volume of a room in sq feet
width   = 10
length =12

print (width * height)




