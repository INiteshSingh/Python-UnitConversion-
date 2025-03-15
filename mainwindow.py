import tkinter as tk
import datetime as dt
try:
    window = tk.Tk()   
    window.geometry("800x500")
    window.title("Goods Tracker")
except:
    print("Something Went Wrong With Generating Tkinter Gui")

try:
#Label for the heading of the window
    label = tk.Label(master=window,text="Goods Tracker with Date and Amount of Goods Bought for Store"
                     ,foreground="white",background="#ba71ee")
    label.pack()
#Label to display the current date and time in the GUI
    dateTime = dt.datetime.now() #datetime variable to get the current date and time when the gui is opened
    datetimeLable = tk.Label(window,text=dateTime,font=("Arial",10),foreground="green",background="black")    
    datetimeLable.palce(x=20,y=20)
except:
    print("Something Went Wrong With Tkinter label Generation")

window.mainloop()

print("Tkinter Window Closed")