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
```python
```
