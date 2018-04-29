# README #

### Repository info ###

* Version
* https://bitbucket.org/pong_avans/pong2d

### Notes ###
* Storing Pong code from repository on Raspberry Pi
* 1) Place the pong code in the following location:
*    '/home/pi/Desktop/pong2d'
*    Because the sound files in 'main.py' and 'pongGame.py' are directed to this location

* Start Pong from terminal:
* 1) Use the following terminal command to start Pong
     'python3 /path/to/main.py'

* How to start Pong at Raspberry Pi startup:
* 1) Open /home/pi/.config/lxsession/LXDE-pi/autostart as superuser (sudo nano)
* 2) Paste the following code between '@pcmanfm..' and '@xscreensaver..'
     '@sudo /usr/bin/python3 /home/pi/Desktop/pong2d/main.py'
