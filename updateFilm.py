from connect import *
from readFilm import read
from time import sleep


def update():
    
    givenID = input("Enter the ID of the film you'd like to update:\n")
    title = input("Enter a film Title: ")
    yearReleased = input("Enter the year released Name: ")
    rating = input("Enter the age rating of the film: ")
    filmDuration = input("Enter the film duration: ")
    
    cursor.execute(
		f"""
		UPDATE tblFilms
		SET Title = "{title}", Year = "{yearReleased}", Rating = "{rating}", Duration = "{filmDuration}"
		WHERE filmID = {givenID}
		;
		"""
		
	)
    connect.commit()

    print(f"Film ID {givenID} has been successfully updated.")
    sleep(2)
    read()

if __name__ == "__main__":
	update()