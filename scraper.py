import os , sys
from selenium  import webdriver
from selenium.webdriver.common.keys import Keys
import re
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import errno
browser = webdriver.Firefox()
str1=[]
#yearList=['2018','2017','2016','2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000,1999,1998,1997,1996,1995]
def start():
	name=sys.argv[2]
	make_directory(name)
	url=sys.argv[1]
	print(url)
	browser.get(url)
	elem = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[6]/form/div/div[2]/div[2]/div/div[2]/div[4]/table')))
	source = browser.page_source
	scrape(source,name)

def scrape(source,name):
	soup = BeautifulSoup(source,'html.parser')
	
	file=open('./'+name+'/'+sys.argv[3]+'.json',"w")
	str1=[]
	str1.append("{")
	for tr in soup.findAll("tr",{"class":"RA-NEWRAresultsEvenRow"}):
		tds = tr.find_all('td')
		str1.append("\"")
		str1.append(tds[1].text)
		str1.append("\"")
		str1.append(":")
		str1.append("\"")
		str1.append(tds[2].text.strip())
		str1.append("\"")
		str1.append(",")
	for tr in soup.findAll("tr",{"class":"RA-NEWRAresultsOddRow"}):
		tds = tr.find_all('td')
		str1.append("\"")
		str1.append(tds[1].text)
		str1.append("\"")
		str1.append(":")
		str1.append("\"")
		str1.append(tds[2].text.strip())
		str1.append("\"")
		str1.append(",")
	var = ''.join(str1)
	file.write(var)
	file.close()
	correct_json_data(name)

def correct_json_data(name):
	instituteFileRead=open('./'+name+'/'+sys.argv[3]+'.json',"r")
	finalstr=(instituteFileRead.read())
		finalstr = finalstr[:-1]
	finalstr+="}"
	instituteFileRead.close()
	instituteFileWrite=open('./'+name+'/'+sys.argv[3]+'.json',"w")
	var = ''.join(finalstr)
	instituteFileWrite.write(var)
	instituteFileWrite.close()	
		
def make_directory(name):
    path = "./"+name
    os.makedirs(path, exist_ok=True)
    print ("Path is created")

start()
