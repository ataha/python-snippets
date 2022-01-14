from tkinter import *
from tkinter import messagebox
import os

#In this function, we have stored the value of the entry box in the task variable
def newTask():
    task = my_entry.get()                    #get() method is used to pull the value provided by the user in the entry box
    if task != "":                           #If entry box not empty
        lb.insert(END, task)                 #add you to-do ( entry ) into the listbox
        my_entry.delete(0, "end")            #you need to remove the text from your entry box after its value added to the listbox
        with open('tasks.txt', 'a') as f:    #store your to-do list in a local file.
            f.write(task + "\n")
            f.close()
    else:
        messagebox.showwarning("warning", "Please enter some task.")


def deleteTask():
    lb.delete(ANCHOR)                         # Here ANCHOR refers to the selected item in the Listbox.
    with open('tasks.txt', 'w') as f:         # Delete unwanted to-do from the local file
        f.write(''.join(lb.get(0, END)))
        f.close()

#Functions to used Enter and delete keys from keyboard
def newTaskEnterKey(e):
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
        with open('tasks.txt', 'a') as f:
            f.write(task + "\n")
            f.close()
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTaskDelkey(e):
    lb.delete(ANCHOR)
    with open('tasks.txt', 'w') as f:
        f.write(''.join(lb.get(0, END)))
        f.close()


ws = Tk()
ws.geometry('500x450+500+200')  # (Width x height + x-position + y-position)
"""
x-position refers to the position of the window on the display over x-axis.
y-position refers to the position of the window on the display over y-axis
"""

ws.title('My To-do List')
ws.config(bg='Black')                       # background color
ws.resizable(width=False, height=False)     # accepts boolean values, False means the window can not be resized

Label(ws,
      text='My Python To Do List',
      bg='Gold',
      font=("Comic Sans MS", 15),
      wraplength=300).place(x=20, y=0)

#Creating a frame
frame = Frame(ws)       #Frame widgets are used to hold other widgets
"""They help in keeping & maintaining user interface(UI) & user experience (Ux) clean & organized"""
frame.pack(pady=40)      #means we have add extra padding around the frame from outside.

#we will place Listbox. sctollbars & buttons inside the frame
lb = Listbox(
    frame,
    width=40,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='Black',
    bg='dim gray',
    highlightthickness=0, #
    selectbackground='Gold',
    activestyle="none",         #Removes the undreline  that appears when the item is selected or focused

)
lb.pack(side=LEFT, fill=BOTH)  #Geometry manager used is pack()
"""side=LIFT --> This will keep the Listbox to the left side of the frame,  coz right positon is for the scrollbars
fill=BOTH --> this will fill the blank space in both the directions that are x and y"""

# the below try and except is to  get all the to-do list entries if it exists in the local file and send it to the Listbox
#This command stacks the items in Listbox.

task_list = []
try:
    with open('tasks.txt', 'r') as tasks_list:
        lines = tasks_list.readlines()
        tasks_list.close()

    for line in lines:
        task_list.append(line)
    for item in task_list:
        lb.insert(END, item)        #insert is a built-in method of the listbox to insert data, END signifies that a new item will be added in the end

    raw = open('tasks.txt', "r+")
    contents = raw.read().split("\n")
    raw.seek(0)
    raw.truncate()
    for item in task_list:
        with open('tasks.txt', 'a+') as f:
            f.write(item)
        f.close()

except FileNotFoundError:
    pass



#Step 5 addding scrollbars

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)  # geometry methog used is a pack() so that everything remains dynamic and in a sequence.
#RIGHT: we have placed scrollbars on the right side of the frame
#BOTH will fill the blank space in both direction that are x and  y

lb.config(yscrollcommand=sb.set)  #bind Listbox with scrollbar
sb.config(command=lb.yview) #yview means scrollbar will go in the vertical direction
#if xview then the scrollbar would have worked in the horizontal direction.


#Step7: Adding Entry Box
#Entry box is used to take input from the user
my_entry = Entry(
    ws,              # entery box is placed on the parent window
    font=('times', 24)
)
my_entry.configure(bg='Gray')
my_entry.place(x=120, y=250)


#Setp 8: Adding another frame for buttons
button_frame = Frame(ws)
button_frame.pack(pady=60)


#Step 9: Adding Buttons
addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask         #When button is clicked the the function mentioned in command is called.
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask      #When button is clicked the the function mentioned in command is called.
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

#Bind the Enter & Delete Keys to Call an event
ws.bind('<Return>',newTaskEnterKey)
ws.bind('<Delete>', deleteTaskDelkey)


ws.mainloop()               #Holds the screen so the we can see the window it is an infinite loop


