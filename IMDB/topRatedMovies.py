from __future__ import print_function
import requests
from bs4 import BeautifulSoup
from subprocess import call

class parser:
	def __init__(self):
		self.url = 'https://www.imdb.com/chart/top/'
		self.response = requests.get(self.url)
		self.html_parsed = BeautifulSoup(self.response.text,'html.parser')
		self.movie_name = self.html_parsed.find_all('td',class_='titleColumn')
		self.rating_movie = self.html_parsed.find_all('td',class_='ratingColumn imdbRating')

	def printTag(self,pageno=1):
		self.maker(pageno)
		print("--------------------")
		print("|  Page No. - ",pageno,'  |')
		print("--------------------")
		nameTag = 'Name of the movie'
		yearTag = ' Year'
		ratingTag = 'Rating'
		print('   '+' '*((self.maxLen-len(nameTag))/2)+nameTag+' '*((self.maxLen-len(nameTag))/2),'  '+yearTag,'  '+ratingTag)

	def printTable(self,serial = 1):
		for name,year,rate in zip(self.nameList,self.yearList,self.rating):
			print('{:2d}'.format(serial),name + ' '*(self.maxLen-len(name)),' ',year,' ',rate)
			serial += 1

	def maker(self,pageno=1):
		self.nameList = []
		self.yearList = []
		self.rating = []
		for name,rate in zip(self.movie_name[10*(pageno-1):10*pageno],self.rating_movie[10*(pageno-1):10*pageno]):
			self.nameList.append(name.a.text)
			self.yearList.append(name.span.text)
			self.rating.append(rate.strong.text)
		self.maxLen = max([len(c) for c in self.nameList])
	
def lable():
	print("\t---------------------------------")
	print("\t|	IMDB Scrapper		|")
	print("\t---------------------------------")
	print("-----------------------------------------------------------------")
	print("|This is a IMDB top rated movie scrapper made with BeautifulSoup|")
	print("-----------------------------------------------------------------")
	print("\t---------------------------------")
	print("\t|******Creator - th3d0ct0r******|")
	print("\t---------------------------------")

parObj = parser()
pageno = 1

while True:
	call('clear')
	lable()
	parObj.printTag(pageno)
	parObj.printTable()
	print("\n\n{:d} (go back)\t\t\t\t\t\t(next page){:d}".format(pageno-1,pageno+1))
	pageno =  pageno+1  if int(input()) == pageno+1 else pageno-1
	if pageno == 0 or pageno == 25:
		break

	