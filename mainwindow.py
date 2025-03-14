import tkinter as tk

window = tk.Tk()
window.geometry("800x500")

#Label for the heading of the window
label = tk.Label(master=window,text="Goods Tracker with Date and Amount of Goods Bought for Store",foreground="black",background="green")
label.pack()
window.mainloop()