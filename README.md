# Customized-Calendar  
![image](https://user-images.githubusercontent.com/89577799/167335469-d17a9fae-d4cc-44aa-bcde-8d871bd006c7.png)
## Tutorial of this customized calendar
<details open="open">
  <summary><b>Table of Contents</b></summary>
  <ol>
    <li>
      <a href="#introduction">Introduction</a>
    </li>
    <li>
      <a href="#the-gui">The GUI</a> 
    </li>
    <li>
      <a href="#the-instructions-for-using-this-GUI">The Instructions for using this GUI</a>
      <ul>
        <li><a href="#right-hand-side">Right-hand-side</a></li>
        <li><a href="#left-hand-side">Left-hand-side</a>
          <ul>
            <li><a href="#buttons">Buttons</a></li>
          </ul>
        </li>  
      </ul>
    </li>
    <li><a href="#the-csv-file-used-in-this-calendar">The csv file used in this calendar</a></li>
    <li>
      <a href="#the-explanation-of-the-code">The explanation of the code</a>
      <ul>
        <li><a href="#the-package-and-the-frame">The package and the frame</a></li>
        <li><a href="#the-functions">The functions</a></li>
      </ul>
    </li>
  </ol>
</details>

# __Introduction__
This repository is a tutorial for the __Customized Calendar__ using python. Users can add, delete, modify, and search for the events they created in the GUI.
# __The GUI__
This __Graphical User Interface__ is convenient and easily used for every users.
# __The Instructions for using this GUI__
## __Right-hand-side__
* The right-hand-side of this interface is the calendar, default is today's date. As you can see, today's date is 2022/5/9.
* Below the calendar, there are two buttons. The __Add__ button is for adding new events into the calendar. Afetr pressing the __Add__ button, you will see the following window.  
![image](https://user-images.githubusercontent.com/89577799/167347447-0b204e9f-c9d9-47ec-9529-155ac1de7812.png)  
You can type up __the time slot__ and __the name of the event__    
![image](https://user-images.githubusercontent.com/89577799/167348835-614bc8ab-c69c-4984-a11b-8149ff4a4537.png)  
After adding the event into the calendar, the color of the date will change, and you can see the details of the event on the left-hand-side.
## __Left-hand-side__
* The left-hand-side of this interface is the details of the events at the specific date, and there are four buttons below.  
### __Buttons__
### __Delete__  
* Fist, select an event you want to delete, and press the delete button.
![image](https://user-images.githubusercontent.com/89577799/167351638-b38660d0-7503-41f3-ad22-efce9cf4e994.png)  
* After pressing the button, you will see the following window:  
![image](https://user-images.githubusercontent.com/89577799/167351832-2f24ab70-9338-4dca-849b-6c141ddf46e8.png)  
* Typing up the event name you want to delete, and press the __Delete__ button. The event on the left-hand-side is disappeared, and the color on 2022/5/9 is gone, too.  
![image](https://user-images.githubusercontent.com/89577799/167436578-8d0ee7f4-5dbe-4dc1-8b41-963406329fa8.png)  
### __Load__  
* If adding an event into the calendar at 2022/5/22, closing the program and re-running it again and pressing the __Load__ button, it will show the event you added and how many days left of the event.  
![image](https://user-images.githubusercontent.com/89577799/167354073-df236a5a-438f-46eb-abcc-d2ee45f6b5b1.png)  
### __Modify__  
After you add the new event to the calendar, but you want to modify the time slot, you can use this button to revise the time.  

* First, double-click with the left mouse button on the event. Second, you press the __Modify__ button.
![image](https://user-images.githubusercontent.com/89577799/167433357-08e0c8b8-5d88-4eb4-8a84-9c6e3740431b.png) 
* After pressing the __Modify__ button, the following window will show up, you can type up the time slot you want.  
__Note__: The name of the event's name should be the same  
![image](https://user-images.githubusercontent.com/89577799/167434398-fa261941-d611-43de-9d2e-ae72c8af6fd9.png)  
* After pressing the __Modify__ button, the time slot is changed.
![image](https://user-images.githubusercontent.com/89577799/167435229-6daa97b4-6acf-45c9-a980-7039ebae4103.png)  
### __Search__ 
After you add the events into so many days, but you forget which event is on which day, then you can use the __Search__ button to do that  
* As you can see, there are three days have the event on the calendar. You remember you have the shooting day, but you forget which day, so just press the __Search__ button 
![image](https://user-images.githubusercontent.com/89577799/167438743-f9fcac4c-0868-4979-a08e-b3f165481430.png)  
* After pressing the __Search__ button, you will see the folowing window:
![image](https://user-images.githubusercontent.com/89577799/167439592-7e4b6b43-0325-408f-bb46-1161418c9e80.png)  
* Then you type the event's name, and press the __Search__ button, it will tell you on what day and what time you will have the shooting day  
![image](https://user-images.githubusercontent.com/89577799/167439797-6b55c538-3edb-4b40-a7a5-89115ec33469.png)  
# __The csv file used in this calendar__
1. The csv file used in this calendar is to store the event on the specific date  
    * When you press the __Add__ button on the right-hand-side and adding the event on the specific date, the event will be stored in the csv file   
2. After you re-run the program, and press the __Load__ button, you will see the details of the event you already added  
# __The explanation of the code__  
## __The package and the frame__  
1. First, we import the __tkinter__, __tkcalendar__, __datetime__, __time__, and __pandas__
```python
from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkcalendar import Calendar, DateEntry
import tkinter.messagebox
from datetime import date, datetime, timedelta
from time import strftime
import os.path
import pandas as pd
```
2. This is for writing the csv file we need in this calendar
```python
global schedule
if os.path.isfile("./schedules_table.csv"):
    schedules = pd.read_csv("./schedules_table.csv", index_col=0)
else:
    schedules = pd.DataFrame(columns=["event", "date", "time"])
    schedules.to_csv("./schedules_table.csv")

global marked_day
marked_day = ''
global add_time
add_time = 0
```
3. This is the whole frame of the calendar
```python
root = Tk()
root.resizable(True, True)
space = " "
root.title(185 * space + "Customized Calendar")

root.geometry("1500x900+56+0")

MainFrame = Frame(root, bd=10, width=400, height=700, relief=RIDGE, bg="cadetblue")
MainFrame.grid()

TitleFrame = Frame(MainFrame, bd=7, width=400, height=100, relief=RIDGE)
TitleFrame.grid(row=0, column=0)

TopFrame3 = Frame(MainFrame, bd=5, width=400, height=500, relief=RIDGE)
TopFrame3.grid(row=1, column=0)
#Left-hand-side
LeftFrame = Frame(TopFrame3, bd=5, width=400, height=600, padx=2, bg="cadet blue", relief=RIDGE)
LeftFrame.pack(side=LEFT)
LeftFrame1 = Frame(LeftFrame, bd=5, width=200, height=180, padx=2, pady=4, relief=RIDGE)
LeftFrame1.pack(side=TOP, padx=10, pady=12)
#Right-hand-side
RightFrame1 = Frame(TopFrame3, bd=5, width=50, height=400, padx=2, bg="cadet blue", relief=RIDGE)
RightFrame1.pack(side=RIGHT, padx=2)
RightFrame1a = Frame(RightFrame1, bd=5, width=50, height=300, padx=2, pady=2, relief=RIDGE)
RightFrame1a.pack(side=TOP, padx=5, pady=6)
#The title on the top of the window
lblTitle = Label(TitleFrame, font=("arial", 35, "bold"), text="Customized Calendar in Python", bd=7)
lblTitle.grid(row=0, column=0, padx=88)
#To show how many days left for the specific event on the left-hand-side
lblCountDown = Label(LeftFrame1, font=("arial", 20, "bold"), text="Activity Countdown", bd=7)
lblCountDown.grid(row=1, column=0)
```
## __The functions__  
* The function for the __Exit__ button
```python
def iExit():
    iExit = tkinter.messagebox.askyesno(
        "Customized Calendar", "Confirm if you want to exit"
    )
    if iExit > 0:
        root.destroy()
        return
```
* The function for the __Load__ button
```python
todos = {}

def insert_Data_timetable():
    global marked_day
    day = str(cal.selection_get())
    
    if day != marked_day:
        countdown_label.config(text = "No schedules")
        for index, row in schedules.iterrows():
            if day == row["date"]:
                treev.insert("", index , values = (row['time'], row['event']))
                Days = (cal.selection_get() - date.today()).days
                countdown_label.config(text = str(Days)+ " days left")
                marked_day = day
    else:
        pass 
      
countdown_label = Label(LeftFrame1, text = " ", font = ("Helvetica", 14))
countdown_label.grid(row=8, column=0, sticky=W, padx=5)
```
