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
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'


import random
import os
import time

from pygame import mixer
import pygame
import keyboard
import time

x = 1
print("Type 'help' for more info")
#Help
def help():
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
	print("music player - Play Music on the command line")
#Music Player
def music_help():
	print("music path")
	print("music player")
	print("music --help")

def music_player():
	songname = input("Enter the path of the song that you want to play:")
	pygame.init()
	pygame.mixer.init()


	def playsound():
	    print("\n")
	    time.sleep(0.5)
	    print("Currently Playing: " + songname)
	    time.sleep(0.5)
	    print("Press Control to stop the music")
	    time.sleep(0.5)
	    print("Press Space to pause the music")
	    time.sleep(0.5)
	    print("Press Enter to unpause the music")

	    pygame.mixer.music.load(songname)
	    pygame.mixer.music.play()
	    while True:  
	        try:  
	            if keyboard.is_pressed('control'):   
	                pygame.mixer.music.stop()
	                
	                break  
	            elif keyboard.is_pressed('space'):
	                pygame.mixer.music.pause()
	                
	            elif keyboard.is_pressed('enter'):
	                pygame.mixer.music.unpause()
	                
	        except:
	            break 


	playsound()


def music_path():
	print("Path for all the music files in the directory:\n")
	def mp3gen():
	    for root, dirs, files in os.walk('.'):
	        for filename in files:
	            if os.path.splitext(filename)[1] == ".mp3":
	                yield os.path.join(root, filename)

	for mp3file in mp3gen():
	    print(mp3file)

#Calculator
def calculator():
	term_gui = int(input("Do you want:\n1.)Terminal Calculator\n2.)GUI Calculator\n(1/2)\n:"))
	if term_gui == 1:	
		import calc 
	elif term_gui == 2:
		os.startfile("C://Windows//System32//calc.exe")
	else:
		print("Invalid Input!")
while x == 1:
	bash = input("betterthan@bash:>")
	salutation = "Hello !", "I am fine, how are you?", "What's up!"
		
	if bash == "exit":
		break 
	
	elif bash == "Hi":
		print(random.choice(salutation))

	elif bash == "help":
		help()

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
		calculator()
	elif bash == "telnet towel.blinkenlights.nl":
		os.system("telnet towel.blinkenlights.nl")
	elif bash == "reboot":
		time.sleep(2)
		print("Rebooting you computer ....")
		time.sleep(2)
		print("Reboot")
		os.system("shutdown /r /t 1")
	elif bash == "bash":
		os.system("bash")
	elif bash == "google":
		print("Google services are not yet developed in this program")
	#Music Section
	elif bash == "music player":
		music_player()
	elif bash == "music --help":
		music_help()
	elif bash == "music path":
		music_path()
	else:
		print("No command" + "-: " + bash + ":" + " found")
