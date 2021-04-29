# Program title

# Credits
# =================================
# icons from www.iconarchive.com
# ================================

import tkinter, os, webbrowser, schedule
from tkinter import PhotoImage, BOTH

def set_icon():
    """ Sets icons based on OS """
    if os.name == "nt":
        root.iconbitmap('schedule.ico')
    if os.name == 'posix':
        root_img = PhotoImage(file = 'schedule.png')
        root.iconphoto(False, root_img)

# define window
root = tkinter.Tk()
root.geometry("512x320")
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

def schedule_class():
    webbrowser.open(zoom_link)
#



# Layouts
input_frame = tkinter.LabelFrame(root, padx=5, pady=5)
output_frame = tkinter.LabelFrame(root, padx=5, pady=5)
input_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)
output_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)

# setting up input frame

# class title
class_title_label = tkinter.Label(input_frame, text="Class Title")
class_title = tkinter.Entry(input_frame, width=20)
class_title.insert(0, "Class Title")

# class start time 
class_start_time_label = tkinter.Label(input_frame, text="Start Time")
class_start_time = tkinter.Entry(input_frame, width=20)
class_start_time.insert(0, "e.g. 08:15")

# class end time
class_end_time_label = tkinter.Label(input_frame, text="End Time")
class_end_time = tkinter.Entry(input_frame, width=20)
class_end_time.insert(0, "e.g. 09:45")

# zoom link
zoom_link_label = tkinter.Label(input_frame, text="Zoom Link")
zoom_link = tkinter.Entry(input_frame, width=50)

# grid
class_title_label.grid(row=0, column=0, padx=5, pady=5)
class_title.grid(row=0, column=1, padx=5, pady=5, sticky="WE")
# grid
class_start_time_label.grid(row=1, column=0,  padx=5, pady=5)
class_start_time.grid(row=1, column=1, padx=5, pady=5,sticky="WE")
# grid
class_end_time_label.grid(row=2, column=0,  padx=5, pady=5)
class_end_time.grid(row=2, column=1, padx=5, pady=5,sticky="WE")
# grid
zoom_link_label.grid(row=3, column=0,  padx=5, pady=5)
zoom_link.grid(row=3, column=1, padx=5, pady=5,sticky="WE")



# Create utility buttons
shedule_button = tkinter.Button(input_frame, text="Shedule")
quit_button = tkinter.Button(input_frame, text="Quit", command=root.destroy)
shedule_button.grid(row=4, column=0, padx=1, pady=20, sticky="WE")
quit_button.grid(row=4, column=1, padx=1, pady=20, sticky="WE")









root.mainloop()
