import time
import os

def isUpper (ascii):
	if ascii>=65 and ascii<=90:
		return True
	return False

def isLower (ascii):
	if ascii>=97 and ascii <=122:
		return True
	return False

newFile = open('mensagem.txt', 'r')
text = str()
os.system('clear')
for key in range(1,26):
	for line in newFile:
		for letter in line:
			if isUpper(ord(letter)):
				text += chr((((ord(letter)-65)-key)%26)+65)
			elif isLower(ord(letter)):
				text += chr((((ord(letter)-97)-key)%26)+97)
			else:
				text += letter
	print(text)
	print("CHAVE: %d" %(key))
	time.sleep(2)
	os.system('clear')
	newFile.seek(0)
	text = str()
####



	

