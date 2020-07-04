import re

print ("The Basic Calculator")
print ("Type 'q' to quit\n")

previous = 0	#Taking the initial equation to solve
run = True	#execute the equation until 'q' is pressed

def performMath():
	global run
	global previous
	equation = ""		#Taking the equation from user
	if previous == 0:	#Equation at starting point
		equation = input("Enter equation: ")	#Take input from user
	else:
		equation = input(str(previous))		#Equating problem with the passage of inputs from user

	if equation == 'q':
		print ("Thanks for using The Basic Calculator, Bye Bye! :)")
		run = False	#Stoping the working of calculator
	else:
		equation = re.sub('[a-zA-Z,:""'']', '', equation) 	#Eliminating the keywords not required in solving equation [a-zA-Z,:""'']

		if previous == 0:	#Again taking the previous=0 value for initial stage
			previous = eval(equation)	#evaluation of the equation given by the user
		else:
			previous = eval(str(previous) + equation)	#Accepting the other input values after 'previous' statement from the user

while run:
	performMath()
