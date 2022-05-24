#complete CAPITALIZED sections

#AUTHOR: audi + sydney
#DATE:5/23

#import libraries
import time
#import os
import board
import busio
import adafruit_bno055
from git import Repo
from picamera import PiCamera

#setup imu and camera
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055_I2C(i2c)
camera = PiCamera()

#import numpy as np
#import cv2 as cv
#print (cv2.__version__)


#bonus: function for uploading image to Github
def git_push():
    try:
#        repo = Repo('/home/pi/Documents/finalproject/.git/') #PATH TO YOUR GITHUB REPO
        full_local_path = "/home/pi/Documents/finalproject/"
        username = "maythecforcebewithyou@gmail.com"
        password = "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"
        remote = f"https://{username}:{password}@github.com/maythecforcebewithyou/finalproject.git"
        print('a')
        #Repo.clone_from(remote, full_local_path)
        print('b')

        repo = Repo(full_local_path)
        print('a')
        repo.git.add('/home/pi/Documents/finalproject/pictures') #PATH TO YOUR IMAGES FOLDER WITHIN YOUR GITHUB REPO
        print('b')
        repo.index.commit('New Photo')
        print('made the commit')
        origin = repo.remote('origin')
        print('added remote')
        origin.push()
        print('pushed changes')
    except:
        print('Couldn\'t upload to git')


    
#SET THRESHOLD
threshold = .5

timeStamp = -1
ready = True
#read acceleration
while True:
    accelX, accelY, accelZ = sensor.acceleration
    timeStamp = timeStamp + 1
    if timeStamp % 100 == 0:
        print(f"accelX: {accelX}, accelY: {accelY}, accelZ: {accelZ}")
    #CHECK IF READINGS ARE ABOVE THRESHOLD
    if timeStamp % 1000000 == 0:
        ready = True
    if accelX > threshold or accelY > threshold or accelZ > threshold and ready:
        ready = False
        #print("accelX>threshold")
        
        #PAUSE

        #TAKE/SAVE/UPLOAD A PICTURE 
        name = "ForceC"     #Last Name, First Initial  ex. FoxJ
        
        if name:
            t = time.strftime("_%H%M%S")      # current time string
            imgname = ('/home/pi/Documents/finalproject/pictures/%s%s.jpg' % (name,t)) #change directory to your folder
            camera.capture(imgname)
            #<YOUR CODE GOES HERE>#
            
    if timeStamp % 1000000000 == 0:
        git_push()

    #PAUSE