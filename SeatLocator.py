import urllib2
import time
import mechanize
import requests
from selenium import webdriver

# Script to find empty seats in USF classes. 

def openAsText():
	url = "http://www.registrar.usf.edu/ssearch/search.php"
	br = mechanize.Browser()
	
	# Browser options
	br.set_handle_redirect(True)
	br.set_handle_robots(False)
	br.addheaders = [('User-agent', 'Firefox')]
	br.open(url)
	for form in br.forms():
    		print form.name
    
   	br.select_form("frmSearch")

	for control in br.form.controls:
		#print control
		print "type=%s, name=%s value=%s" % (control.type, control.name, br[control.name])
		for item in control.items:
    	#print " name=%s values=%s" % (item.name, str([label.text  for label in item.get_labels()]))
    			print "Hello"

def findElementByName(elementName, driver):
	myElement = driver.find_element_by_name(elementName)
	return myElement

 openAsText()