import urllib2
import time
import mechanize
from selenium import webdriver


def getResponse(websiteAddress):
	response = urllib2.urlopen(websiteAddress[0])
	return response

def openPage(websiteAddress):
	driver = webdriver.Chrome(executable_path=r"C:/ChromeDriver/chromedriver.exe")  # Optional argument, if not specified will search path.
	driver.get('http://www.google.com/xhtml')
	return driver

def closeDriver(driver)
	driver.quit()

def findElementByName(elementName, driver)
	myElement = driver.find_element_by_name(elementName)
	return myElement

def sendKeystroke(element, keystrokes)
	element.send_keys()
	element.submit()

def openAsText():
	url = "http://www.registrar.usf.edu/ssearch/search.php"
	br = mechanize.Browser()
	
	# Browser options
	br.set_handle_redirect(True)
	br.set_handle_robots(False)
	br.addheaders = [('User-agent', 'Firefox')]
	br.open(url)

	for form in br.forms():
		print form

