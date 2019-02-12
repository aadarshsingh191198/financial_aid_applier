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
class PythonOrgSearch(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_fetch_specializations(self):
		driver = self.driver
		# input("Enter the name of the specialization for which you want to apply the financial aid: ")
		driver.get("https://www.coursera.org/directory/specializations")
		courses = []
		
		# nextPage = driver.find_elements_by_class_name("label-text")[1]
		# print(nextPage.size())
		# count = 1
		try:
			for count in range(11):
				for i in range(2):
					elem = driver.find_elements_by_xpath("//*[@id='rendered-content']/div/div/div/div[2]/div[2]/div/div[1]/div/div["+str(i+1)+"]/ul/li")
					try:
						# print(type(el
						n = len(elem)
						print(n)
						print("Executed Successfully")
					except:
						n = 15
					for j in range(n):
						elem = driver.find_element_by_xpath("//*[@id='rendered-content']/div/div/div/div[2]/div[2]/div/div[1]/div/div["+str(i+1)+"]/ul/li["+str(j+1)+"]/a")
						course = dict()
						course['name']=elem.text
						course['url']=elem.get_attribute("href")
						courses.append(course)
				print("Page "+ str(count+1) +" Done")	
				# count=count+1
				nextPage = driver.find_elements_by_class_name("label-text")[1]
				print(type(nextPage))
				if "arrow-disabled" in nextPage.get_attribute("class"):
					break
				else :
					nextPage.click()

				time.sleep(10)	
		except:
			pass
		print(courses,len(courses))

	# def test_database_fill(self):
		try:
			conn = sqlite3.connect('coursera.sqlite')
			cur = conn.cursor()

			cur.execute('''CREATE TABLE if not exists Specializations (Specialisation_id integer not null primary key autoincrement, Name TEXT, URL TEXT)''')

			for course in courses:
				cur.execute('''INSERT OR IGNORE INTO Specializations (Name,URL)  VALUES ( ? ,?)''', (course['name'], course['url'] ) )

			conn.commit()
		except:
			fh = open('temp.txt','w+',encoding='utf-8')
			fh.write(str(courses))
			fh.close()
			print("Some error occured. Saved the scraped data in temp.txt file")
			
	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()				