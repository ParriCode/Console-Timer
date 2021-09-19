# Console-Timer
A little python console program with the capacity of create, modify and save personalize timer.
## What do this software ? 
 The original idea was count the time spent doing activities, you can create a timer and see the time that it runnig, when you finish your activity stop the       timer to save it in a csv file, to reload it after when you want.
## Requirements
 This software is developed on Ubuntu 18.04 if you are using windows probably they don't run correctly.
 Its a Console program , all you need is the console.
## How to use
 Fist you must run the program, after that the program will be init.
![](https://github.com/ParriCode/Console-Timer/blob/main.py/images/img2.png)

At first seen you have a list of commands.
 Let see some examples commands.
### help
 The command **help** show a menu with a description of each command
![help_image](https://github.com/ParriCode/Console-Timer/blob/main.py/images/img.png)

### new [new timer name]
 The command **new** create a new timer , and it is save with 0 seconds and the date of the day
![new image](https://github.com/ParriCode/Console-Timer/blob/main.py/images/img4.png)

### start [saved timer name]
 The command **start** start a save timer to star counting time
![new image](https://github.com/ParriCode/Console-Timer/blob/main.py/images/img6.png)
 ```
start python
```
Also you can start all saved timers
 ```
start all
```
### see [startet timer_name]
 The command **see** show a menu of a started timer with the diferents time measurements
 ![new image](https://github.com/ParriCode/Console-Timer/blob/main.py/images/img13.png)
 
  _The menu has two parts , the left numbers is the time since we started the timer for the last time_
  _The right part is the sum of every time that the timer was started _
### save [saved timer_name]
 The command **save** saves an exist and started timer with the time that has passed since it started
### exist [timer_name]
 The command **exist** check if the called name is saved in the data file, if exist return True, else return False.

 
 Also you can write **exist all**, this command return a list of existing timers 
 ```
exist all
```
![exist image](https://github.com/ParriCode/Console-Timer/blob/main.py/images/img12.png)

### stop [started timer]
The command **stop** stop and saves properties of a timer
Also you can stop all started timers
 ```
stop all
```
### delete [existing timer_name]
 The command **delete** delete a save timer from the data file forever
 Also you can delete all timers from data files
### quit
 stop the program , this command not save the timers that its running
## contact
You can contact with me using:
 - Email: theparri@protonmail.com
 - Discord: parri#6160

