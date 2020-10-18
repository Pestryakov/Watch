from tkinter import *
import time

def tick():
    watch.after(200, tick)
    watch['text'] = time.strftime('%H:%M:%S')

root = Tk()
watch = Label(font='Arial 70', bg='pink')
watch.pack(fill=X)
tick()

root.mainloop()
