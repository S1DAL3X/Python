from tkinter import *

#This is full screen app
root = Tk()
root.title('Window')

maxSizeWindow = root.maxsize()

#in 1920 and 1080 write you weight and height monitor screen
weight = (maxSizeWindow[0] // 2) - 1920 // 2 - 9
height = (maxSizeWindow[1] // 2) - 1080 // 2

root.geometry('1920x1080+' + str(weight) + '+' + str(height))

def button_click():
    print('Hello World!')

def close_window():
    root.destroy()
    root.quit()


#button = Button(root, text = 'Press Button', width = 10, height = 5, command = button_click )
#button.place(x = 300, y = 100)

root.protocol('WM_DELETE_WINDOW', close_window)

root.mainloop()
