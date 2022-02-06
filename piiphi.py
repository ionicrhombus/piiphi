import os
import re
import csv
from datetime import datetime

now=datetime.now()

dt_string=now.strftime("%d%m%y%H%M%S")

root_dir=input('Type the directory you would like to search here:')

ssn='[0-9]{3}-[0-9]{2}-[0-9]{4}'
dob='^([1][12]|[0]?[1-9])[\/-]([3][01]|[12]\d|[0]?[1-9])[\/-](\d{4}|\d{2})$'
mastercard='^(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}$'
visa='\b([4]\d{3}[\s]\d{4}[\s]\d{4}[\s]\d{4}|[4]\d{3}[-]\d{4}[-]\d{4}[-]\d{4}|[4]\d{3}[.]\d{4}[.]\d{4}[.]\d{4}|[4]\d{3}\d{4}\d{4}\d{4})\b'
amex= '^3[47][0-9]{13}$'
password='/(pass(word|phrase)?|secret): \S+/gi;'
email='/([a-z0-9_\-.+]+)@\w+(\.\w+)*/gi;'

validfiles=[]
matches=[]
for directory, subdirectories, files in os.walk(root_dir):
	for file in files:
		if file.endswith('.txt'):
			validfiles.append(os.path.join(directory,file))
		elif file.endswith('.csv'):
			validfiles.append(os.path.join(directory,file))
		elif file.endswith('.doc'):
			validfiles.append(os.path.join(directory,file))
		elif file.endswith('.ppt'):
			validfiles.append(os.path.join(directory,file))
		elif file.endswith('.xls'):
			validfiles.append(os.path.join(directory,file))

for item in validfiles:

	filer=item
	e=open(filer,'r', errors='ignore')
	for line in e.readlines():
		liner=line.strip()
		if re.match(ssn,line):
			match=(item,'SSN',liner)
			matches.append(match)
		elif re.match(mastercard,line):
			match=(item,'Mastercard',liner)
			matches.append(match)
		elif re.match(visa,line):
			match=(item,'Visa',liner)
			matches.append(match)
		elif re.match(amex,line):
			match=(item,'American Express',liner)
			matches.append(match)
		elif re.match(dob,line):
			match=(item,'Date of birth',liner)
			matches.append(match)
		elif re.match(password,line):
			match=(item,'Password',liner)
			matches.append(match)
		elif re.match(email,line):
			match=(item,'Email',liner)
			matches.append(match)
	e.close()

fields = ['File','Data type','Data']

reportname='report'+dt_string+'.csv'

with open(os.path.join(root_dir,reportname),'w',newline='') as f:
	write=csv.writer(f)
	write.writerow(fields)
	write.writerows(matches)
