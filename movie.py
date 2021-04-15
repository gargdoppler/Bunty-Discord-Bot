from bs4 import BeautifulSoup
import requests
import random
from googlesearch import search
import imdb

def addMovie(msg):
	words = msg.split("\"")
	mov = words[1]
	with open("./movie_list.txt", "r+") as f:
		mov_list = f.readlines()
		if mov in mov_list:
			return False
		else:
			f.write(mov.lower() + "\n")
			return True
			
def showMovie():
	with open("./movie_list.txt", "r") as f:
		mov_list = f.readlines()
		embed = ""
		for movie in mov_list:
			embed += movie.capitalize() + "\n"		
	return embed


def get_imd_summary(url):
	movie_page = requests.get(url)
	soup = BeautifulSoup(movie_page.text, 'html.parser')
	return soup.find("div", class_="summary_text").contents[0].strip()

def findCode(link):
	tags = link.split("/")
	tot = tags[-2]
	code = ""
	for char in tot:
		if char.isdigit():
			code += char
	
	return code

def findLink(name):
	query = name + "imdb"
	for i in search(query, num_results=0):
		return i
  
def fetchMovieName(msg):
	words = msg.split("\"")
	print(words)
	return words[1]

def fetchMovieTitle(msg):
	ia = imdb.IMDb()
	series = ia.get_movie(findCode(findLink(fetchMovieName(msg))))
	rating = series.data['rating']
	print(series['cover url'])
	return str(str(series) + "\n\nIMDb: " + str(rating))

def fetchPosterUrl(msg):
	ia = imdb.IMDb()
	series = ia.get_movie(findCode(findLink(fetchMovieName(msg))))
	rating = series.data['rating']
	return series['cover url']
