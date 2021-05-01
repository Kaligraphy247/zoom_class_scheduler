# Program title

# Credits
# =================================
# icons from www.iconarchive.com
# ================================

import tkinter, os, webbrowser, schedule, time, os
from tkinter import PhotoImage, BOTH, END, messagebox

# HIGH LEVEL-ish FUNCTION
def set_icon():
    """ Sets icons based on OS """
    if os.name == "nt":
        root.iconbitmap('img/schedule.ico')
    if os.name == 'posix':
        root_img = PhotoImage(file = 'img/schedule.png')
        root.iconphoto(False, root_img)

# define window
root = tkinter.Tk()
root.geometry("520x320")
root.resizable(0,0)
root.title("Zoom Class Scheduler")
set_icon()

# Define fonts and colors 
# None: Using system defaults


# FUNCTIONS
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system("clear")

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = "{:02d}:{:02d}".format(mins,secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1 # decrements timer by 1 second(obviously)
# set sceonds for timer
seconds = 3


def reset():
    class_title.delete(0, END)
    class_start_time.delete(0, END)
    zoom_link.delete(0, END)
    messagebox.showinfo("Reset", "Cleared!")

def get_zoom_link():
    ''' gets zoom link , used as a command for the Schedule Button'''
    zoomLink = zoom_link.get()
    classStartTime = str(class_start_time.get()) # converts class_start_time.get() to string
    # open link
    def open_link():
        ''' Opens link in zoomLink'''
        webbrowser.open(zoomLink)

    def cancelJob():
        ''' remove a job from the scheduler '''
        return schedule.CancelJob

    schedule.every().day.at(classStartTime).do(open_link)
    messagebox.askokcancel("Schedule", f"{class_title.get()} will start automatically at {class_start_time.get()}")
    #schedule.every().day.at(classStartTime).do(cancelJob)
    while True:
        schedule.run_pending()
        time.sleep(1)
        

# Layouts
input_frame = tkinter.LabelFrame(root, padx=5, pady=5)
output_frame = tkinter.LabelFrame(root, padx=5, pady=5)
input_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)
output_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)

# setting up input frame

# class title
class_title_label = tkinter.Label(input_frame, text="Class Title")
class_title = tkinter.Entry(input_frame, width=20)
class_title.insert(0, "Maths 1")

# class start time 
class_start_time_label = tkinter.Label(input_frame, text="Start Time")
class_start_time = tkinter.Entry(input_frame, width=20)
#class_start_time.insert(0, "08:15")
#get_start_time()

# class end time
class_end_time_label = tkinter.Label(input_frame, text="End Time")
class_end_time = tkinter.Entry(input_frame, width=20)
##class_end_time.insert(0, "e.g. 09:45")
#get_end_time()

# zoom link
zoom_link_label = tkinter.Label(input_frame, text="Zoom Link")
zoom_link = tkinter.Entry(input_frame, width=50)
zoom_link.insert(0, "https://www.google.com/")


# grid
class_title_label.grid(row=0, column=0, padx=5, pady=5)
class_title.grid(row=0, column=1, padx=5, pady=5, sticky="WE")
# grid
class_start_time_label.grid(row=1, column=0,  padx=5, pady=5)
class_start_time.grid(row=1, column=1, padx=5, pady=5,sticky="WE")
# grid
'''class_end_time_label.grid(row=2, column=0,  padx=5, pady=5)
class_end_time.grid(row=2, column=1, padx=5, pady=5,sticky="WE")'''
# grid
zoom_link_label.grid(row=3, column=0,  padx=5, pady=5)
zoom_link.grid(row=3, column=1, padx=5, pady=5,sticky="WE")


# Create utility buttons
shedule_button = tkinter.Button(input_frame, text="Schedule", command=get_zoom_link, underline=0,relief="groove")
quit_button = tkinter.Button(input_frame, text="Quit", command=root.destroy, underline=0,relief="groove")
reset_button = tkinter.Button(input_frame, text="Reset", command=reset, underline=0,relief="groove")
shedule_button.grid(row=4, column=1, padx=1, ipady=5, pady=20, sticky="WE")#sticky="WE"
quit_button.grid(row=4, column=0,ipadx=5, ipady=5, padx=1, pady=20, sticky="WE")
reset_button.grid(row=5, column=0, padx=1, pady=1, ipadx=5, ipady=5, columnspan=2)


# run's Root window's mainloop
root.mainloop()