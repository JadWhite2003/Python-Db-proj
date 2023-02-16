from connect import *
from readFilm import read
from time import sleep

def delete():
	read()
	sure = False
	while sure == False:
		givenID = input("\nEnter the ID of the film you'd Like to delete:\n")
		print(f"You've selected film of ID {givenID}.")
		confirm = input(f"Are you sure you want to Delete film {givenID}?\n")
		if confirm == "yes" or confirm == "y" or confirm == "Y":
			sure = True

	cursor.execute(f"DELETE FROM tblFilms WHERE filmID = {givenID}")
	connect.commit()

	print(f"The film of ID {givenID} has been deleted.")
	sleep(2)
	read()

if __name__ == "__main__":
	delete()