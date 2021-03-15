import random
import os
import time

x = 1
print("Type 'help' for more info")
"""
User name and password
Root access
{Not completed}

username = input("Enter your betterthan@bash username:")
password = input("Enter the password for your user name:")

if bash == "root":
	enter = input("Enter the password for " + username + ":")
	if enter == password:
		print("Access Granted")
	else:
		print("Access Denied")
"""

while x == 1:
	bash = input("betterthan@bash:>")
	salutation = "Hello !", "I am fine, how are you?", "What's up!"
		
	if bash == "exit":
		break 
	
	elif bash == "Hi":
		print(random.choice(salutation))
	elif bash == "help":
		print("Here are the commands:-")
		time.sleep(0.5)
		print("help   -  Type this command for help")
		time.sleep(0.5)
		print("Hi     -  Type this command for salutation")
		time.sleep(0.5)
		print("clear  -  Type this command for clearing the screen")
		time.sleep(0.5)
		print("notepad - To open notepad")
		time.sleep(0.5)
		print("python - To open Python3")
		time.sleep(0.5)
		print("ls     -  List directory")
		time.sleep(0.5)
		print("shutdown - To shutdown the computer")
		time.sleep(0.5)
		print("reboot -  Reboot the Computer")
		time.sleep(0.5)
	elif bash == "clear":
		os.system("cls")
	elif bash == "notepad":
		os.startfile("C://Windows//System32//notepad.exe")
	elif bash == "python":
		os.system("python")
	elif bash == "wsl":
		os.system("wsl")
	elif bash == "shutdown":
		os.system("shutdown /s /t 1")
	elif bash == "ls":
		os.system("dir")
	elif bash == "cd":
		path = input("Enter the path where you want to go:")
		os.chdir(path)
	elif bash == "calc":
		term_gui = int(input("Do you want:\n1.)Terminal Calculator\n2.)GUI Calculator\n(1/2)\n:"))
		if term_gui == 1:	
			import calc 
		elif term_gui == 2:
			os.startfile("C://Windows//System32//calc.exe")
		else:
			print("Invalid Input!")
	elif bash == "telnet towel.blinkenlights.nl":
		os.system("telnet towel.blinkenlights.nl")
	elif bash == "reboot":
		time.sleep(2)
		print("Rebooting you computer ....")
		time.sleep(2)
		print("Reboot")
		os.system("shutdown /r /t 1")

	else:
		print("No command" + "-: " + bash + ":" + " found")