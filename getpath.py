import platform
from pathlib import Path
import os

def getpath():
	if(os.path.exists("dirname.txt")):
		f = open("dirname.txt","r")
		path=os.path.abspath(f.read())
		f.close()
	else:
		if platform.system()=='Windows':
			print("Hello Windows User!")
			dtop= os.path.join(str(Path.home()),"Desktop")
		elif platform.system()=='Linux':
			print("Hello Linux User!")
			dtop= os.path.join(str(Path.home()))
		elif platform.system()=='Darwin':
			print("Hello MacOS User!")
			dtop= os.path.join(str(Path.home()))
		print("Please enter the address for the folder 'Sample'. This will be stored on your computer in dirname.txt")
		print("For example : D:\IBAC Research Group\Data\Sample")
		f = open("dirname.txt","x")
		path=os.path.abspath(input())
		f.write(path)
		f.close()
	return path