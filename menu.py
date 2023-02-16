from time import sleep
from readFilm import read
from addFilm import insertFilm
from updateFilm import update
from deleteFilm import delete


def menuOptions():
	menuUI = \
	"""
	Welcome to Film Database 

	Please Select an Option Below:
		1. Display films in the Database
		2. Add a new film to the Database
		3. Update an existing film
		4. Delete an existing film
		5. Exit Application

	"""
	options = ["1", "2", "3", "4", "5"]
	choice = 0
	while choice not in options:
		print(menuUI)
		choice = input("Enter Select an option from the menu: ")
		if choice not in options:
			print(choice, "is not a valid option, try again.")
			sleep(1)
	return choice
	

mainProgram = True
while mainProgram:
	userChoice = menuOptions() 
	if userChoice == "1":
		read()
	elif userChoice == "2":
		insertFilm()
	elif userChoice == "3":
		update()
	elif userChoice == "4":
		delete()
	else:
		mainProgram = False

input("Press Enter to Exit the Application.")
