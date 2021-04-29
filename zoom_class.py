import datetime, time, schedule, webbrowser, os

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

def join_class():
    ''' To join classes'''
    print(f"{zoom_class} by {class_time}")
    print(f"\nJoining in {seconds} secs ...")
    countdown(seconds)
    webbrowser.open(zoom_link)
    #print("Opens webbrowser in newtab") #debug
def exit_script():
    '''closes the script'''
    print(f"Closing script in {seconds} seconds")
    countdown(seconds)
    clear_screen()
    exit()

'''Runs Main program - Zoom_Class'''
zoom_class = input("Enter Class Name:: \n")
class_time = input("Enter Time\n24 hour format, e.g. 16:45:: \n")
zoom_link = input("Enter Zoom Link:: \n")
end_class = input("Enter class end time:: \n")
time.sleep(1)
print("Saved")
time.sleep(1)
print(f"You will join {zoom_class} by {class_time} automatically.\n")
time.sleep(2)
print("Sit back and leave this terminal open\n")
schedule.every().day.at(class_time).do(join_class) 
schedule.every().day.at(end_class).do(exit_script)

while True:
    schedule.run_pending()
    time.sleep(1)
