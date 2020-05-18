import tkinter
window = tkinter.Tk()
window.title("Queue Time Estimator")
   
#if they pressed yes
def yes():
    num = float(entry.get())
    num1 = (2.5 * num * 0.75)
    tkinter.Label(window, text = num1, fg = "black", bg = "white").grid(row = 2, column = 0, columnspan = 2, sticky = "we")
    tkinter.Label(window, text = "mins", fg = "black", bg = "white").grid(row = 2, column = 1, sticky = "we")

#if they pressed no
def no():
    num = float(entry.get())
    num1 = (2.5 * num * 0.9)
    tkinter.Label(window, text = num1, fg = "black", bg = "white").grid(row = 2, column = 0, columnspan = 3, sticky = "we")
    tkinter.Label(window, text = "mins", fg = "black", bg = "white").grid(row = 2, column = 2, sticky = "we")

#the labels
tkinter.Label(window, text = "How many in queue", fg = "black", bg = "white").grid(row = 0, sticky = "we")
tkinter.Label(window, text = "is it lunch time?", fg = "black", bg = "white").grid(row = 1, sticky = "we")

#entry window
entry = tkinter.Entry(window, fg = "black", bg = "white")
entry.grid(row = 0, column = 1, columnspan = 2)

#the buttons
tkinter.Button(window, text = "yes", command = yes, fg = "black", bg = "white").grid(row = 1, column = 1, sticky = "we")
tkinter.Button(window, text = "no", command = no, fg = "black", bg = "white").grid(row = 1, column = 2, sticky = "we")

window.mainloop()

