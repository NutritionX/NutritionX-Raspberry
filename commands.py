#!/usr/bin/python

import sys
import subprocess

#function for taking and storing the raspberry camera module photo
def take_photo(filename) :
	process = subprocess.call(['raspistill',  '-o' , filename])
	if process == 0:
		print("Photo taken and saved as " + filename + ".")
	else:
		print("An error occured while trying to take a photo.")

#checks if the threshold argument is valid and returns it
def parse_image_threshold(threshold) :
	if threshold > 0 and threshold < 100:
		print("Threshold of " + str(threshold) + " is valid.")
		return threshold
	else:
		print("Threshold of " + str(threshold) + " is invalid. Setting threshold to 20.")
		return 20

#image recongnition funcion
def ssocr_image(filename, threshold) :
	process = subprocess.call(['ssocr',  '-d',  '-1', '-t', str(threshold), filename])
	if process == 0:
		print("Photo taken and saved as " + filename + ".")
	else:
		print("An error has occured while taking the photo.")

filename = '/home/pi/cam.jpg'
if len(sys.argv) < 2: 
	print("Enter a threshold.")
else:
	try:
		threshold = int(sys.argv[1])
		threshold = parse_image_threshold(threshold)
		take_photo(filename)
		ssocr_image(filename, threshold)
	except ValueError:
		print("That's not an int!")
