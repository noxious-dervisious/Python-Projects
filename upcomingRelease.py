from __future__ import print_function
import requests
from bs4 import BeautifulSoup
from subprocess import call

class release:
	def __init__(self,url = 'https://www.imdb.com/calendar/?ref_=nv_mv_cal',schedule = {}):
		self.response = requests.get(url)
		self.html_parsed = BeautifulSoup(self.response.text,'html.parser')
		self.main_division = self.html_parsed.find('div',id='main')
		self.country_name =  self.html_parsed.find('div',class_="aux-content-widget-3")
		self.countryTag = self.country_name.find_all('a',href=True)

	def listMaker(self,possible_dates = {}):
		for child in self.main_division.descendants:
			if child.name == 'h4':
				date = child.text
				possible_dates[date] = ''
			if child.name == 'li':
				movie_name = child.text
				possible_dates[date] = possible_dates[date]+'\n'+movie_name.strip()
		return possible_dates

	def countryDict(self,countryList = {}):
		for tags in self.countryTag:
			countryList[tags.text] = tags['href']
		return countryList

	def SchedulePrinterDateWise(self,serial = 1,datesAvailable = []):
		self.schedule = self.listMaker()
		call('clear')
		if len(self.schedule.keys()) ==  0:
			return False
		maxLen = max([len(dates) for dates in self.schedule.keys()])
		print("\t\tHere is the list of all the movie release dates")
		print("\t\t------------------------------------------------")
		for dates in self.schedule.keys():
			datesAvailable.append(dates)
			print('\t\t'+'    '+'-'*(maxLen+4))
			print('\t\t'+'{:3d}'.format(serial),'|',dates+' '*(maxLen-len(dates)),'|')
			print('\t\t'+'    '+'-'*(maxLen+4))
			serial += 1
		selectedDate = input("\nSelect Your Desired Date (1-{:d}): ".format(len(datesAvailable)))
		print("\n[+] Movies Releasing on ",datesAvailable[selectedDate-1])
		movieList = self.schedule[datesAvailable[selectedDate-1]].split('\n')
		for movies in movieList[1:]:
			print('\t=>',movies)
		return True

	def SchedulePrinterAllMovie(self):
		self.schedule = self.listMaker()
		call('clear')
		if len(self.schedule.keys()) ==  0:
			return False
		for dates in self.schedule.keys():
			print("\n[-] Date : ",dates)
			movie = self.schedule[dates].split('\n')
			maxLen = max([len(_) for _ in movie])
			print("[+] Movies to be released")
			print('\t\t'+'-'*(maxLen+4))
			for movie_in in movie[1:]:
				print('\t\t'+'|',movie_in+' '*(maxLen-len(movie_in)),'|')
			print('\t\t'+'-'*(maxLen+4))
		return True

def countryListPrinter(countryWiseTags= {},serial = 1,conName =[]):
	maxLen = max([len(countries) for countries in countryWiseTags.keys()])
	print('\t\t   '+'-'*(maxLen+9))
	for countries in countryWiseTags.keys():
		conName.append(countries)
		print('\t\t   '+'|{:3d}.'.format(serial),countries,' '*(maxLen-len(countries)),'|')
		serial += 1
	print('\t\t   '+'-'*(maxLen+9))
	return conName

def CountryWiseRelease():
	obj = release()
	countryWiseTags = obj.countryDict()
	conName = countryListPrinter(countryWiseTags)
	serial = input("Enter your choice [1-{}] : ".format(len(countryWiseTags)))
	conUrl = 'https://imdb.com'+countryWiseTags[conName[serial-1]]
	obj_new = release(conUrl)
	print("Now that you have choice to filter your search")
	print("We again offer you two path @DateWise @AllMovieList")
	choice = raw_input("Now I will again ask you for your choice : ")
	if "DateWise" in choice:
		if not obj_new.SchedulePrinterDateWise():
			print("Sorry no movie for you :P ")
	elif "AllMovieList" in choice:
		if not obj_new.SchedulePrinterAllMovie():
			print("Sorry no movie for you :P ")

def IMDBdefaultPage():
	obj = release()
	if not obj.SchedulePrinterDateWise():
		print("Sorry no movie for you :P ")

def poster():
	print('\t\t-------------------------------------------------------------')
	print("\t\t|Welcome Everyone to the IMDB scrapper for upcoming releases|")
	print('\t\t-------------------------------------------------------------')
	print("\t\t\t\tCreated by - th3d0ct0r")

def starter():
	call("clear")
	poster()
	print("From here we offer we two surffing options @IMDBchoice @CountryFilter")
	print("So how would you like to proccede.")
	choice = raw_input("Enter your choice : ")
	if "IMDBchoice" in choice:
		IMDBdefaultPage()
	elif "CountryFilter" in choice:
		CountryWiseRelease()

starter()