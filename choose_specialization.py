#Provide the user with a list of specialization - ask for which he wants to apply
#Provide the course list for that specialization - ask for the courses for which he wants to apply
#In case the application is already applied or the login credentials are wrong or the verification is not provided, handle the exception and display the error message
#

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time, sqlite3


		
conn = sqlite3.connect('coursera.sqlite')
cur = conn.cursor()

while True:
	specialization = input("Enter the name of the specialization for which you want to apply the financial aid: ")
	query = '%'+specialization+'%'
	cur.execute('''SELECT  * FROM  Specializations WHERE   name  LIKE ? ''',(query,))

	choices = cur.fetchall()
	print("****************************Available Courses***************************\n")
	for index,row in enumerate(choices):
		print(index+1,". ", row[0])
	print("\n************************************************************************")


	choice = int(input("Enter the row number(Between 1 and "+str(len(choices))+") or -1 if you didn't find the course: "))
	if choice != -1: 
		print("Go to this url: ", choices[choice-1][1])
		break
	else:		
		print("Change the query terms and try again\n\n")
