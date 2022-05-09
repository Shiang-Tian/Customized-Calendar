# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkcalendar import Calendar, DateEntry
import tkinter.messagebox
from datetime import date, datetime, timedelta
from time import strftime
import os.path
import pandas as pd

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

#Frame
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

LeftFrame = Frame(TopFrame3, bd=5, width=400, height=600, padx=2, bg="cadet blue", relief=RIDGE)
LeftFrame.pack(side=LEFT)
LeftFrame1 = Frame(LeftFrame, bd=5, width=200, height=180, padx=2, pady=4, relief=RIDGE)
LeftFrame1.pack(side=TOP, padx=10, pady=12)

# LeftDownFrame = Frame(LeftFrame, bd=5, width=200, height=180, padx=2, pady=4, relief=RIDGE)
# LeftDownFrame.pack(side=LEFT, padx=10, pady=12)

RightFrame1 = Frame(TopFrame3, bd=5, width=50, height=400, padx=2, bg="cadet blue", relief=RIDGE)
RightFrame1.pack(side=RIGHT, padx=2)
RightFrame1a = Frame(RightFrame1, bd=5, width=50, height=300, padx=2, pady=2, relief=RIDGE)
RightFrame1a.pack(side=TOP, padx=5, pady=6)

lblTitle = Label(TitleFrame, font=("arial", 35, "bold"), text="Customized Calendar in Python", bd=7)
lblTitle.grid(row=0, column=0, padx=88)

lblCountDown = Label(LeftFrame1, font=("arial", 20, "bold"), text="Activity Countdown", bd=7)
lblCountDown.grid(row=1, column=0)
# ==========================================================================================================
#Variables
# RDays = StringVar()
# RYears = StringVar()
# RMonths = StringVar()
# RWeeks = StringVar()

# =======================================================================================================================
# Functions
# def Reset():
#     RDays.set("")
#     RYears.set("")
#     RMonths.set("")
#     RWeeks.set("")

def iExit():
    iExit = tkinter.messagebox.askyesno(
        "Customized Calendar", "Confirm if you want to exit"
    )
    if iExit > 0:
        root.destroy()
        return

# def Result():
#     FutureDate = DentFDate.get_date()
#     CurrentDate = DentCDate.get_date()

#     Day = abs((FutureDate - CurrentDate).days)
#     RDays.set(str(Day))

#     Year = int(RDays.get())
#     Yearss = Year / 365
#     # No decimal required
#     RYears.set(str("%.0f" % (Yearss)))

#     RWeeks.set(str(int(Year / 7)))

#     Month = int(RYears.get())
#     RMonths.set(str("%.0f" % (Month * 12)))


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


def stationary(cb=None):
    selectedItem = treev.focus()
    global selectedIndex
    selectedIndex = treev.item(selectedItem)['text']

# def LoadTodo():
#     global todos
#     f = open("class_time_table.dat", "r")
#     data = f.read()
#     f.close()
#     todos = eval(data)
#     ListTodo()

def ListTodo(cb=None):
    for i in treev.get_children():
        treev.delete(i)

    tanggal = str(cal.selection_get())
    if tanggal in todos:
        for i in range(len(todos[tanggal])):
            treev.insert(
                "",
                "end",
                text=i,
                values=(todos[tanggal][i]["time"], todos[tanggal][i]["event"]),
            )

#Add
def addTodo(win, key, start_hour, minute1, end_hour, minute2, event, day):
    global add_time
    global schedules
    add_time = add_time + 1
    timerange = "{:02d}:{:02d}~{:02d}:{:02d}".format(start_hour.get(), minute1.get(), end_hour.get(), minute2.get())
    newTodo = {
        "time": timerange,
        "date": str(cal.selection_get()),
        "event": event.get()
    }
    check_date = 1
    for data_index in range(len(schedules['date'])):
        start_old = schedules['time'][data_index].split('~')
        starttime_list = start_old[0].split(':')
        endtime_list = start_old[1].split(':')

        starttime_int = [int(i) for i in starttime_list]
        starthour = starttime_int[0]
        endtime_int = [int(i) for i in  endtime_list]
        endhour = endtime_int[0]
        start_new = start_hour.get()
        end_new = end_hour.get()
        
        if schedules['date'][data_index] == str(cal.selection_get()):
            if start_new == starthour and end_new == endhour:
                tkinter.messagebox.showinfo("Schedules", "You can't add the event because this timerange already has a event !")
                check_date = 99
                break
            if end_new > starthour and start_new < starthour:
                tkinter.messagebox.showinfo("Schedules", "You can't add the event because this timerange already has a event !")
                check_date = 99
                break
            if start_new > starthour and end_new < endhour:
                tkinter.messagebox.showinfo("Schedules", "You can't add the event because this timerange already has a event !")
                check_date = 99
                break
            if start_new > starthour and end_new > endhour:
                tkinter.messagebox.showinfo("Schedules", "You can't add the event because this timerange already has a event !")
                check_date = 99
                break
            if start_new < starthour and end_new > endhour:
                tkinter.messagebox.showinfo("Schedules", "You can't add the event because this timerange already has a event !")
                check_date = 99
                break
    if check_date != 99:
        schedules = schedules.append(newTodo, ignore_index=True)
        schedules.to_csv("schedules_table.csv")
                    

        cal.calevent_create(day, "Add schedule", "reminder4")
        cal.tag_config("reminder4", background="indianred", foreground="white")
                        
                        

        if key in todos:
            todos[key].append(newTodo)
        else:
            todos[key] = [newTodo]
        
    win.destroy()
    ListTodo()

def AddForm():
    win = Toplevel()
    win.wm_title("+")
    start_hour = IntVar()
    minute1 = IntVar()
    end_hour = IntVar()
    minute2 = IntVar()

    event = StringVar(value="")
    Label(win, text="Time:").grid(row=0, column=0)
    Label(win, text="From:").grid(row=1, column=0)
    Spinbox(win, from_=00, to=23, increment = 1, format="%02.0f", textvariable=start_hour, width=3).grid(row=1, column=1)
    Label(win, text=":").grid(row=1, column=2)
    Spinbox(win, from_=00, to=59, increment = 1, format="%02.0f",textvariable=minute1, width=3).grid(row=1, column=3)
    Label(win, text="To:").grid(row=2, column=0)
    Spinbox(win, from_=00, to=24, increment = 1, format="%02.0f",textvariable=end_hour, width=3).grid(row=2, column=1)
    Label(win, text=":").grid(row=2, column=2)
    Spinbox(win, from_=00, to=59, increment = 1, format="%02.0f",textvariable=minute2, width=3).grid(row=2, column=3)
    Label(win, text="Event:").grid(row=3, column=0)
    Entry(win, textvariable=event).grid(row=3, column=1, columnspan=2)

    event_date = cal.selection_get()

    tanggal = str(cal.selection_get())
    Button(
        win,
        text="Add",
        command=lambda: addTodo(
            win, tanggal, start_hour, minute1, end_hour, minute2, event, event_date
        ),
    ).grid(row=6, column=0)
#Delete
def delTodo(event):
    global add_time
    global schedules
    add_time = add_time - 1
    event_date = cal.selection_get()
    tanggal = str(cal.selection_get())
    selectedItem = treev.focus()
    todos[tanggal].pop(treev.item(selectedItem)["text"])
    if len(todos[tanggal])==0:
        cal.calevent_create(event_date, "No schedule", "reminder5")
        cal.tag_config("reminder5", background="white", foreground="black")
    for index, row in schedules.iterrows():
        if row['event'] == event.get():
            schedules = schedules.drop(labels = index, axis = 0) 
    schedules = schedules.reset_index(drop = True)
    schedules.to_csv("schedules_table.csv")
    ListTodo()

def DeleteForm():
    win = Toplevel() 
    win.wm_title("Delete")
    event = StringVar(value="")
    Label(win, text="Event:").grid(row=3, column=0)
    Entry(win, textvariable=event).grid(row=3, column=1, columnspan=2)
    Button(win, text="Delete", command=lambda: delTodo(event)).grid(row=6, column=0)
#Modify
def Modified(win, key, start_hour, minute1, end_hour, minute2, event):
    global schedules
    timerange = "{:02d}:{:02d}~{:02d}:{:02d}".format(start_hour.get(), minute1.get(), end_hour.get(), minute2.get())
    newTodo = {
        "time": timerange,
        "date": str(cal.selection_get()),
        "event": event.get()
    }

    for index, row in schedules.iterrows():
        if row['event'] == event.get():
            schedules.at[index, 'date'] = str(cal.selection_get())
            schedules.at[index, 'time'] = timerange
    schedules.to_csv("schedules_table.csv")

    if key in todos:
        todos[key][selectedIndex] = newTodo
    else:
        todos[key].append(newTodo)
    win.destroy()
    ListTodo()

def ModifiedForm():
    win = Toplevel() 
    win.wm_title("Modified")
    start_hour = IntVar()
    minute1= IntVar()
    end_hour = IntVar()
    minute2= IntVar()
    
    event = StringVar(value="")
    Label(win, text ="Time:").grid(row=0, column=0)
    Label(win, text ="From:").grid(row=1, column=0)
    Spinbox(win, from_=0, to=23, textvariable=start_hour, width=3).grid(row=1, column=1)
    Label(win, text =":").grid(row=1, column=2)
    Spinbox(win, from_=0, to=59, textvariable=minute1, width=3).grid(row=1, column=3)
    Label(win, text ="To:").grid(row=2, column=0)
    Spinbox(win, from_=0, to=24, textvariable=end_hour, width=3).grid(row=2, column=1)
    Label(win, text =":").grid(row=2, column=2)
    Spinbox(win, from_=0, to=59, textvariable=minute2, width=3).grid(row=2, column=3)
    Label(win, text="Event:").grid(row=3, column=0)
    Entry(win, textvariable=event).grid(row=3, column=1, columnspan=2)

    tanggal = str(cal.selection_get())
    Button(win, text="Modify", command=lambda: Modified(win, tanggal, start_hour, minute1, end_hour, minute2, event)).grid(row=6, column=0)

#Search
def search(gui, event):
    global schedules
    index = 0
    for _, row in schedules.iterrows():
        if row['event'] == event.get():
            # put name in the first column
            gui.insert("", index , values = (row['event'], row['date'], row['time']))
            index += 1

def SearchForm():
    win = Toplevel()
    win.wm_title("Search for event")
    
    event = StringVar(value="")
    Label(win, text = "Search: ").grid(row = 0, column = 0, sticky="w", pady = 5) 
    Entry(win, textvariable=event).grid(row = 0, column = 1, sticky="w", pady = 5)
    search_gui = ttk.Treeview(win)
    search_gui.grid(row=1, column=0, sticky="WNE", rowspan=4, columnspan=2)
    scrollBar1 = Scrollbar(win, orient="vertical", command=search_gui.yview)
    scrollBar1.grid(row=1, column=2, sticky="ENS", rowspan=4)
    search_gui.configure(yscrollcommand=scrollBar1.set)
    search_gui["columns"] = ("1", "2", "3")
    search_gui["show"] = "headings"
    search_gui.column("1", width=100)
    search_gui.heading("1", text="Event")
    search_gui.heading("2", text="Date")
    search_gui.heading("3", text="Time")
    Button(win, text="Search", command=lambda: search(gui = search_gui, event= event)).grid(row=6, column=0)
    #Clear things in treeview
    def Refresh():
        search_gui.delete( * search_gui.get_children())
    Button(win, text="Refresh", command=Refresh).grid(row=6, column=1)




    
# ================================================================================================================================================
cal = Calendar(RightFrame1a,firstweekday="sunday", selectmode="day", weekendforeground="red", date_pattern="dd/mm/y", font=("arial", 16, "bold"))
cal.bind("<<CalendarSelected>>", ListTodo)
tanggal = str(cal.selection_get())
#左下角Lable及Button
lblEvent = Label(LeftFrame1, font=("arial", 14, "bold"), text="Today's Event", anchor="w", justify=LEFT)
lblEvent.grid(row=0, column=0, sticky=W, padx=5)
btnDel = Button(LeftFrame1, text="Delete", width=10, command=DeleteForm)
btnDel.grid(row=5, column=0, sticky=W, padx=5)
btnMod = Button(LeftFrame1, text="Modify", width=10, command=ModifiedForm)
btnMod.grid(row=5, column=1, sticky=W, padx=5)
btnSearch = Button(LeftFrame1, text="Search", width=10, command = SearchForm)
btnSearch.grid(row=6, column=1, sticky=W, padx=5)
btnLoad = Button(LeftFrame1, text="Load", width=10, command=insert_Data_timetable)
btnLoad.grid(row=6, column=0, sticky=W, padx=5)
# btnCalculate = Button(LeftFrame1, text="Calculate", width=10, command=Result)
# btnCalculate.grid(row=7, column=0, sticky=W, padx=5)
# btnLoad = Button(LeftFrame1, text="Timetable", width=10, command=LoadTodo)
# btnLoad.grid(row=7, column=0, sticky=W, padx=5)

#左下角的視窗可以看到當天活動
treev = ttk.Treeview(LeftFrame1)
treev.grid(row=1, column=0, sticky="WNE", rowspan=4, columnspan=2)
scrollBar = Scrollbar(LeftFrame1, orient="vertical", command=treev.yview)
scrollBar.grid(row=1, column=2, sticky="ENS", rowspan=4)
treev.configure(yscrollcommand=scrollBar.set)

treev.bind("<Double-1>",stationary )
treev["columns"] = ("1", "2")
treev["show"] = "headings"
treev.column("1", width=100)
treev.heading("1", text="Time")
treev.heading("2", text="Event")

#National Holiday
date_year_begin1 = date(2021, 1, 1)
date_year_begin2 = date(2021, 1, 2)
date_year_begin3 = date(2021, 1, 3)

date_spring1 = date(2021, 2, 10)
date_spring2 = date(2021, 2, 11)
date_spring3 = date(2021, 2, 12)
date_spring4 = date(2021, 2, 13)
date_spring5 = date(2021, 2, 14)
date_spring6 = date(2021, 2, 15)
date_spring7 = date(2021, 2, 16)

date_228a = date(2021, 2, 27)
date_228b = date(2021, 2, 28)
date_228c = date(2021, 3, 1)

date_child1 = date(2021, 4, 2)
date_child2 = date(2021, 4, 3)
date_child3 = date(2021, 4, 4)
date_child4 = date(2021, 4, 5)

date_work1 = date(2021, 4, 30)
date_work2 = date(2021, 5, 1)
date_work3 = date(2021, 5, 2)

date_dra1 = date(2021, 6, 12)
date_dra2 = date(2021, 6, 13)
date_dra3 = date(2021, 6, 14)

date_mid1 = date(2021, 9, 18)
date_mid2 = date(2021, 9, 19)
date_mid3 = date(2021, 9, 20)
date_mid4 = date(2021, 9, 21)

date_coun1 = date(2021, 10, 9)
date_coun2 = date(2021, 10, 10)
date_coun3 = date(2021, 10, 11)

date_111begin = date(2021, 12, 31)
# 國定假日標顏色
cal.calevent_create(date_year_begin1, "元旦", "reminder1")
cal.calevent_create(date_year_begin2, "元旦", "reminder1")
cal.calevent_create(date_year_begin3, "元旦", "reminder1")

cal.calevent_create(date_spring1, "春節", "reminder1")
cal.calevent_create(date_spring2, "春節", "reminder1")
cal.calevent_create(date_spring3, "春節", "reminder1")
cal.calevent_create(date_spring4, "春節", "reminder1")
cal.calevent_create(date_spring5, "春節", "reminder1")
cal.calevent_create(date_spring6, "春節", "reminder1")
cal.calevent_create(date_spring7, "春節", "reminder1")

cal.calevent_create(date_228a, "228", "reminder1")
cal.calevent_create(date_228b, "228", "reminder1")
cal.calevent_create(date_228c, "228", "reminder1")

cal.calevent_create(date_child1, "兒童", "reminder1")
cal.calevent_create(date_child2, "兒童", "reminder1")
cal.calevent_create(date_child3, "兒童", "reminder1")
cal.calevent_create(date_child4, "兒童", "reminder1")

cal.calevent_create(date_work1, "勞動", "reminder1")
cal.calevent_create(date_work2, "勞動", "reminder1")
cal.calevent_create(date_work3, "勞動", "reminder1")

cal.calevent_create(date_dra1, "端午", "reminder1")
cal.calevent_create(date_dra2, "端午", "reminder1")
cal.calevent_create(date_dra3, "端午", "reminder1")

cal.calevent_create(date_mid1, "中秋", "reminder1")
cal.calevent_create(date_mid2, "中秋", "reminder1")
cal.calevent_create(date_mid3, "中秋", "reminder1")
cal.calevent_create(date_mid4, "中秋", "reminder1")

cal.calevent_create(date_coun1, "國慶", "reminder1")
cal.calevent_create(date_coun2, "國慶", "reminder1")
cal.calevent_create(date_coun3, "國慶", "reminder1")

cal.calevent_create(date_111begin, "111元旦", "reminder1")

cal.tag_config("reminder1", background="gold", foreground="black")
# 上課日期標顏色
date_1 = date(2021, 9, 6)
date_2 = date(2021, 9, 7)
for i in range(1, 17):
    cal.calevent_create(date_1 + cal.timedelta(days=7 * i), "論文研討", "reminder2")

for i in range(1, 17):
    cal.calevent_create(date_2 + cal.timedelta(days=7 * i), "資料科學", "reminder3")
cal.tag_config("reminder2", background="skyblue", foreground="black")
cal.tag_config("reminder3", background="pink", foreground="black")

cal.grid(row=0, column=0, padx=10)

# =======================================================================================================================
# # 左上視窗的Label and Entry
# lblCDate = Label(LeftFrame1, font=("arial", 16, "bold"), text="Current Date", bd=7, anchor="w", justify=LEFT)
# lblCDate.grid(row=2, column=0, sticky=W, padx=5)
# # Drop down calendar
# DentCDate = DateEntry(LeftFrame1, font=("arial", 16, "bold"), bd=5, width=43, borderwidth=2, date_pattern="dd/mm/yyyy")
# DentCDate.grid(row=2, column=1)

# lblFDate = Label(LeftFrame1, font=("arial", 16, "bold"), text="Future Date", bd=7, anchor="w", justify=LEFT)
# lblFDate.grid(row=3, column=0, sticky=W, padx=5)
# # Drop down calendar
# DentFDate = DateEntry(LeftFrame1, font=("arial", 16, "bold"), bd=5, width=43, borderwidth=2, date_pattern="dd/mm/yyyy")
# DentFDate.grid(row=3, column=1)

# lblRDays = Label(LeftFrame1, font=("arial", 16, "bold"), text="Remaining Days", bd=7, anchor="w", justify=LEFT)
# # sticky = W 是靠左邊
# lblRDays.grid(row=4, column=0, sticky=W, padx=5)
# entRDays = Entry(LeftFrame1, font=("arial", 16, "bold"), bd=5, width=44, justify="left", textvariable=RDays)
# entRDays.grid(row=4, column=1)

# lblRYear = Label(LeftFrame1, font=("arial", 16, "bold"), text="Remaining Year", bd=7, anchor="w", justify=LEFT)
# lblRYear.grid(row=5, column=0, sticky=W, padx=5)
# entRYear = Entry(LeftFrame1, font=("arial", 16, "bold"), bd=5, width=44, justify="left", textvariable=RYears)
# entRYear.grid(row=5, column=1)

# lblRMonths = Label(LeftFrame1, font=("arial", 16, "bold"), text="Remaining Months", bd=7, justify=LEFT)
# lblRMonths.grid(row=6, column=0, sticky=W, padx=5)
# entRMonths = Entry(LeftFrame1, font=("arial", 16, "bold"), bd=5, width=44, justify="left", textvariable=RMonths)
# entRMonths.grid(row=6, column=1)

# lblRWeeks = Label(LeftFrame1, font=("arial", 16, "bold"), text="Remaining Weeks", bd=7, justify=LEFT)
# lblRWeeks.grid(row=7, column=0, sticky=W, padx=5)
# entRWeeks = Entry(LeftFrame1, font=("arial", 16, "bold"), bd=5, width=44, justify="left", textvariable=RWeeks)
# entRWeeks.grid(row=7, column=1)
# ======================================================================================================================================================
# 右邊視窗Button
btnAdd = Button(RightFrame1a, padx=18, bd=7, font=("Helvetical", 18, "bold"), width=23, text="Add", bg="cadetblue", command=AddForm)
btnAdd.grid(row=2, column=0, padx=10, pady=2)

# btnReset = Button(RightFrame1a, padx=18, bd=7, font=("Helvetical", 18, "bold"), width=23, text="Reset", bg="cadetblue", command=Reset)
# btnReset.grid(row=3, column=0, padx=10, pady=2)

btnExit = Button(RightFrame1a, padx=18, bd=7, font=("Helvetical", 18, "bold"), width=23, text="Exit", bg="cadetblue", command=iExit)
btnExit.grid(row=4, column=0, padx=10, pady=2)

root.mainloop()
