from connect import *

def read():
	cursor.execute("SELECT * FROM  tblFilms")
	rows = cursor.fetchall()

	print("\nFilm List:")
	for record in rows:
		print(record)

if __name__ == "__main__":
	read()
