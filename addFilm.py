from connect import *
from readFilm import read
from time import sleep


def insertFilm():
    myFilm = []
    title = input("Enter a film Title: ")
    yearReleased = input("Enter the year released Name: ")
    rating = input("Enter the age rating of the film: ")
    filmDuration = input("Enter the film duration: ")

    myFilm.append(title)
    myFilm.append(yearReleased)
    myFilm.append(rating)
    myFilm.append(filmDuration)

    print(myFilm)
    cursor.execute(
	f"""
	INSERT INTO songs VALUES(NULL, "{myFilm[0]}", "{myFilm[1]}", "{myFilm[2]}", "{myFilm[3]}")
	"""
	)
    connect.commit()
    print(f"{title}, has been added successfully to the database.")
    sleep(3)
    read()

if __name__ == "__main__":
	insertFilm()