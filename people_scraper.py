import sqlite3
import urllib2
from bs4 import BeautifulSoup


def get_people():

	# scrape info from portal, add to db.
	db = sqlite3.connect(employees.db)
	user_page = 'https://portal.urbanchestnut.com/admin/users'
	page = urllib2.urlopen(user_page)
	soup = BeautifulSoup(page, 'html.parser')
	
	# for each employee, get rfid.
	
