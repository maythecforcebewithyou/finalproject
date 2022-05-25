#complete CAPITALIZED sections

#AUTHOR: audi + sydney
#DATE:5/23

#import libraries
import time
import os
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
    #try:
#        repo = Repo('/home/pi/Documents/finalproject/.git/') #PATH TO YOUR GITHUB REPO
    full_local_path = "/home/pi/Documents/finalproject/"
    username = "maythecforcebewithyou@gmail.com"
    password = "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"
    remote = f"https://{username}:{password}@github.com/maythecforcebewithyou/finalproject.git"
    print(remote)
    #empty_repo = git.Repo.init(os.path.join(rw_dir, 'empty'))
    #origin = empty_repo.create_remote('origin', repo.remotes.origin.url)
    #origin.fetch()
    #empty_repo.create_head('master', origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
    #Repo.clone_from(remote, full_local_path)
    print('b')

    repo = Repo(full_local_path)
    print('a')
    repo.git.add('/home/pi/Documents/finalproject/pictures') #PATH TO YOUR IMAGES FOLDER WITHIN YOUR GITHUB REPO
    print('b')
    repo.index.commit('New Photo')
    print('made the commit')
    origin = repo.remote(name = 'origin')
    print('added remote')
    assert origin.exists()
    print("existence confirmed")
    origin.push().raise_if_error()
    #repo.git.push("origin", master)
    print('pushed changes')
    #except:
        #print('Couldn\'t upload to git')


    
#SET THRESHOLD
threshold = .5

timeStamp = time.time()
ready = True
#read acceleration
while True:
    accelX, accelY, accelZ = sensor.acceleration
    current = time.time()
    if current % 5 == 0:
        print(f"accelX: {accelX}, accelY: {accelY}, accelZ: {accelZ}")
    #CHECK IF READINGS ARE ABOVE THRESHOLD
    if (current - timeStamp) > 5:
        ready = True
        print("ready!")
        timeStamp = current
    if ready and (accelX > threshold or accelY > threshold or accelZ > threshold):
        ready = False
        #print("accelX>threshold")
        
        #PAUSE
        print("test")
        #TAKE/SAVE/UPLOAD A PICTURE 
        name = "ForceC"     #Last Name, First Initial  ex. FoxJ
        
        if name:
            t = time.strftime("_%H%M%S")      # current time string
            imgname = ('/home/pi/Documents/finalproject/pictures/%s%s.jpg' % (name,t)) #change directory to your folder
            camera.capture(imgname)
            #<YOUR CODE GOES HERE>#
            
    #if timeStamp % 1000000000 == 0:
        #git_push()

    #PAUSE