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

import time
import sys
class PythonOrgSearch(unittest.TestCase):

	def setUp(self):
		profile = webdriver.FirefoxProfile()
		# 1 - Allow all images
		# 2 - Block all images
		# 3 - Block 3rd party images 
		profile.set_preference("permissions.default.image", 2)

		self.driver = webdriver.Firefox(firefox_profile=profile)
		# self.driver = webdriver.Firefox()

	def test_search_in_python_org(self):
		driver = self.driver

		driver.get("https://www.coursera.org/?authMode=login")

		email = 'asingh191198@outlook.com'
		password = 'aadarshcoursera@123'

		inp = driver.find_element_by_xpath("//*[@name='email']")
		inp.send_keys(email)

		pas = driver.find_element_by_xpath("//*[@name='password']")
		pas.send_keys(password)

		elem = driver.find_element_by_xpath("//*[@id='authentication-box-content']/div/div[2]/div/div[1]/form/div[1]/button")
		elem.click()
		
		url = input("Enter the url of the specialization: ")

		driver.get(url)


		# try:
		# 	self.assertIn("Interaction Design | Coursera", driver.title)
		# except:
		# 	print("Could not find the title")
		try:
			elem = driver.find_element_by_xpath("//*[@id='root']/div[1]/div/div[4]/div/div/div[2]/ul/li/div[2]/button")
			elem.click()
		except:
			print("Less than or equal to 4 courses in the specialization")
			
		link_divs = driver.find_elements_by_class_name("CourseItem")
		print(len(link_divs))
		courses=[]
		for i in range(min(4,len(link_divs))):
			link_a = driver.find_element_by_xpath("//*[@id='root']/div[1]/div/div[4]/div/div/div[2]/div["+str(i+1)+"]/div[2]/a")
			link = link_a.get_attribute("href")
			print(link)
			courses.append(link)

		if len(link_divs) >4:
			for i in range(len(link_divs)-4):
				link_a = driver.find_element_by_xpath("//*[@id='root']/div[1]/div/div[4]/div/div/div[2]/ul/li/div[1]/div/div["+str(i+1)+"]/div[2]/a")
				link = link_a.get_attribute("href")
				print(link)
				courses.append(link)


		print("****************************Available Courses***************************\n")
		for index,row in enumerate(courses):
			print(index+1,". ", row)
		print("\n************************************************************************")

		choices = list(int(i) for i in input("Enter the courses that you want to enroll in <space separated>: ").split())
		for choice in choices:

			driver.get(courses[choice-1])	
			# try:
			#     element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")) )
			
			time.sleep(30)

			print("Going to click the financial aid button")
			try:
				elem = driver.find_elements_by_class_name("button-link")[2]
				print(driver.find_elements_by_class_name("button-link")[0],"Hello")
				elem.click()
				print("Successful")
			except:
				# driver.implicitly_wait(30)
				# corr= True
				try : 
					elem = driver.find_elements_by_class_name("button-link")[1]
					elem.click()
					print("Successful")
				except: 
					print("Unsuccessful, click manually")
					time.sleep(20)
			
			print("Going to click the continue button")
			try:
				elem = driver.find_element_by_xpath("//button[contains(text(),'Continue to the application')]")
				elem.click()
				print("Successful")
			except:
				print("Unsuccessful, click manually")
				time.sleep(20)

			time.sleep(30)
			elem = driver.find_element_by_id("info_checkbox")
			elem.click()
			elem = driver.find_element_by_id("completion_checkbox")
			elem.click()
			elem=driver.find_element_by_id("accept-terms-field")
			elem.send_keys("I agree to the terms above")
			

			print("Going to click the 1st submit button")
			try:
				elem =driver.find_element_by_xpath("//*[@id='rendered-content']/div/div/div[1]/div/div/div[2]/button")
				elem.click()
				print("Successful")
			except Exception as e:
				print("Unsuccessful, click manually")
				time.sleep(10)

			print("In the final phase")
			keyword = input("Enter a keyword for your course: ")
			# institution = input("Enter the name of your college: ")
			# curr_course = input("Enter the current course that you are pursuing: ")
			try:
				elem = driver.find_element_by_xpath("//*[@id='finaid-educationalBackground']/option[3]")
				elem.click()
				elem = driver.find_element_by_xpath("//*[@id='finaid-income']")
				elem.send_keys("0")
				elem = driver.find_element_by_xpath("//*[@id='finaid-employmentStatus']/option[5]")
				elem.click()
				elem = driver.find_element_by_xpath("//*[@id='finaid-amount-can-pay']")
				elem.send_keys("0")
				elem = driver.find_element_by_xpath("//*[@id='would-not-take-loan']")
				elem.click()
				elem = driver.find_element_by_xpath("//*[@id='finaid-reason']")
				elem.send_keys("The biggest reason that I am applying for a financial reason is that I can't afford to pay for this course. I come from a financially weak family. My parents' annual income is just sufficient to pay for the college fees and the hostel mess. They can't afford to pay for anything more than that. Although the course can be audited for free, in that case, there will be no deadlines for assignment submission and no certificate of course completion as well. These two factors are very important and motivate one to complete the course, that too on time. Without these, I may start the course fully motivated but I will surely lose my motivation with time. Also, I will not be able to judge my performance as there will be no scale to measure it.  This stands as a secondary reason why I am applying for the financial aid.")
				elem = driver.find_element_by_xpath("//*[@id='finaid-goal']")
				elem.send_keys("I have been a bright student and had a very good academic performance since my early school days. Currently, I am pursuing Bachelor of Technology in one of the top-notch engineering colleges of India, Indian Institute of Technology (Indian School of Mines) Dhanbad and I have had an Overall Grade Point Average of 9.7 out of 10 up to the 5th semester. My branch of study is Computer Science and Engineering and I love to enhance my skills in this field as much as possible. In today’s world, "+keyword+" has a vast scope and an excellent future. I personally believe that completing this course would be a good head start for stepping into the world of "+keyword+".  Moreover, the certificate provided on course completion will be a motivating factor for me and also a sign of proof. If I am being granted this financial aid, I assure that I will complete all my assignments on time.  Also, it will help me in expanding my skill set.")
				elem = driver.find_element_by_xpath("//*[@id='finaid-loanReason']")
				elem.send_keys("As I have already mentioned, that the financial condition of my family is not that strong, so it would not be possible for me to pay for the loan. The loan would come as a pressure not only on my parents but also on me and that may affect my academic performance as a whole. Moreover, if I am provided with the financial aid, I promise to complete my assignments on time and even help my peers, who are taking the same course, in clearing their doubts. Not only this, but I will also spread mass awareness about Coursera in my college; mostly among my juniors and batchmates, so that they can learn from such an amazing platform as this. Although I am not able to pay for the course with money, I will try to compensate for the same through indirect contribution in the form of promotions of the Coursera platform.")
				confirm = input("Should I finally submit the application? 1 or 0: ")
				if confirm=='1':
					elem = driver.find_element_by_xpath("//button[contains(text(),'Submit Application')]")
					elem.click()
				else:
					print("Didn't fill the applcation")
				print("All done successfully for current course!")

			except:
				print("Could not find element",elem)
				time.sleep(20)

	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()
