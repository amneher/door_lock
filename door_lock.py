# RFID Door Lock System 
#
# v.0.1
#
# Andrew Neher for UCBC
# 
# MIT licensed
#
# 1. October 2018

import time
import gpiozero

# import employee list & rfids
def import_people():
	pass
	#import from portal db and refresh weekly.
	
# receive and parse rfid signal
def get_rfid():
	pass
	
# check rfid against employee list, return employee & info
def find_employee():
	pass
	
# receive employee info, check access permissions and current time, return go or no go.
# if go, call emp_is_allowed(), if not, call no_soup_for_you().
def emp_is_allowed():
	pass
	
# recieve go signal, send appropriate signal to lock.
def open_sesame():
	pass
	
# recieve no go signal, send email to a list
def no_soup_for_you():
	pass
