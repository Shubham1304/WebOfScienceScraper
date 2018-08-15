import os , sys
import json
from pprint import pprint

def make_directory():
    path = "./MIT/CitingInstitutes"
    os.makedirs(path, exist_ok=True)
    print ("Path is created")

def makeitwork():
	institutesNameList=['UNIVERSITY OF CALIFORNIA SYSTEM','MASSACHUSETTS INSTITUTE OF TECHNOLOGY MIT','UNITED STATES DEPARTMENT OF ENERGY DOE','ISTITUTO NAZIONALE DI FISICA NUCLEARE','HARVARD UNIVERSITY','CHINESE ACADEMY OF SCIENCES','CONSEJO SUPERIOR DE INVESTIGACIONES CIENTIFICAS CSIC','UNIVERSITY OF CHICAGO','UNIVERSITE PARIS SACLAY','RUSSIAN ACADEMY OF SCIENCES','CEA','SORBONNE UNIVERSITE','UNIVERSITY OF CALIFORNIA BERKELEY','CNRS NATIONAL INSTITUTE OF NUCLEAR PARTICLE PHYSICS IN2P3','GODDARD SPACE FLIGHT CENTER','SAPIENZA UNIVERSITY ROME','UNIVERSITE SORBONNE PARIS CITE USPC COMUE','UNIVERSITY OF MICHIGAN','OHIO STATE UNIVERSITY','JOHNS HOPKINS UNIVERSITY','EUROPEAN ORGANIZATION FOR NUCLEAR RESEARCH CERN','ISTITUTO NAZIONALE GEOFISICA E VULCANOLOGIA INGV','UNIVERSITY OF TORONTO','UNIVERSITY OF OXFORD','DEUTSCHES ELEKTRONEN SYNCHROTRON DESY','STANFORD UNIVERSITY','UNIVERSITY OF WASHINGTON','UNIVERSITY OF WISCONSIN MADISON','NORTHWESTERN UNIVERSITY','INDIAN INSTITUTE OF TECHNOLOGY SYSTEM IIT SYSTEM','JOINT INSTITUTE FOR NUCLEAR RESEARCH RUSSIA','UNIVERSITY OF LONDON','UNIVERSITY OF BIRMINGHAM','CALIFORNIA INSTITUTE OF TECHNOLOGY','PENNSYLVANIA COMMONWEALTH SYSTEM OF HIGHER EDUCATION PCSHE']
	stringToWriteInFile=[]
	for i in range (1998,2019): 
		make_directory()
		yearFile=open('./MIT/'+str(i)+'.json',"r")
		str1=(yearFile.read())
		with open('./MIT/'+str(i)+'.json') as f:
	    		data = json.load(f)
		for j in range (35):
			try:
				if (i==1998):
					stringToWriteInFile.append("{")
				instituteFile=open('./MIT/CitingInstitutes/'+institutesNameList[j]+'.json',"a")
				stringToWriteInFile.append("\""+str(i)+"\""+":"+"\""+data[institutesNameList[j]]+"\",")
				var = ''.join(stringToWriteInFile)
				instituteFile.write(var)
				instituteFile.close()
			except:
				print ("Exception handled")
			stringToWriteInFile=[]

	""" 	In the code below I have written the code to automatically remove the last comma ',' in the json data and place a '}' in place 			of it using some of the string operations		
	"""

	for i in range (35):	#35 because I have considered only 35 institutes as of now to get the no of citations from them to MIT and the 					#35 institutes are mentioned in the string institutesNameList
		instituteFileRead=open('./MIT/CitingInstitutes/'+institutesNameList[i]+'.json',"r")
		finalstr=(instituteFileRead.read())
		print (finalstr)
		finalstr = finalstr[:-1]
		finalstr+="}"
		instituteFileRead.close()
		instituteFileWrite=open('./MIT/CitingInstitutes/'+institutesNameList[i]+'.json',"w")
		var = ''.join(finalstr)
		instituteFileWrite.write(var)
		instituteFileWrite.close()			
makeitwork()
