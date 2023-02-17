import tkinter as tk
import random
import pygame
from tkinter import *
from PIL import ImageTk, Image
from playsound import playsound
from pygame import mixer


#Function to swap two bars that will be animated
def swap(pos_0, pos_1):
    bar11, _, bar12, _ = canvas.coords(pos_0)
    bar21, _, bar22, _ = canvas.coords(pos_1)
    canvas.move(pos_0, bar21-bar11, 0)
    canvas.move(pos_1, bar12-bar22, 0)

worker = None 

#Insertion Sort
def _insertion_sort():
    global barList
    global lengthList

    for i in range(len(lengthList)):
        cursor = lengthList[i]
        cursorBar = barList[i]
        pos = i

        while pos > 0 and lengthList[pos - 1] > cursor:
            lengthList[pos] = lengthList[pos - 1]
            barList[pos], barList[pos - 1] = barList[pos - 1], barList[pos]
            swap(barList[pos],barList[pos-1])   
            yield                                      
            pos -= 1                                   

        lengthList[pos] = cursor
        barList[pos] = cursorBar
        swap(barList[pos],cursorBar)

#Selection Sort            
def _selection_sort():
    global barList    
    global lengthList

    for i in range(len(lengthList)):
        min = i
        for j in range(i + 1 ,len(lengthList)):
            if(lengthList[j] < lengthList[min]):
                min = j
        lengthList[min], lengthList[i] = lengthList[i] ,lengthList[min]
        barList[min] , barList[i] = barList[i] , barList[min]
        swap(barList[min] , barList[i])        
        yield

#Bubble Sort
def _bubble_sort():
    global barList
    global lengthList

    for i in range(len(lengthList) - 1):
        for j in range(len(lengthList) - i - 1):
            if(lengthList[j] > lengthList[j + 1]):
                lengthList[j] , lengthList[j + 1] = lengthList[j + 1] , lengthList[j]
                barList[j], barList[j + 1] = barList[j + 1] , barList[j]
                swap(barList[j + 1] , barList[j])
                yield 

#Triggering Fuctions

def insertion_sort():     
    global worker
    worker = _insertion_sort()
    animate()

def selection_sort():     
    global worker
    worker = _selection_sort()
    animate()

def bubble_sort():     
    global worker
    worker = _bubble_sort()
    animate()  


#Animation Function
def animate():      
    global worker
    if worker is not None:
        try:
            next(worker)
            window.after(10, animate)    
        except StopIteration:            
            worker = None
        finally:
            window.after_cancel(animate) 


#Generator function for generating data
def generate():
    global barList
    global lengthList
    canvas.delete('all')
    barstart = 5
    barend = 15
    barList = []
    lengthList = []

    #Creating a rectangle
    for bar in range(1, 60):
        randomY = random.randint(1, 360)
        bar = canvas.create_rectangle(barstart, randomY, barend, 375, fill='sky blue')
        barList.append(bar)
        barstart += 10
        barend += 10

    #Getting length of the bar and appending into length list
    for bar in barList:
        bar = canvas.coords(bar)
        length = bar[3] - bar[1]
        lengthList.append(length)

    #Maximum is colored Red
    #Minimum is colored Black
    for i in range(len(lengthList)-1):
        if lengthList[i] == min(lengthList):
            canvas.itemconfig(barList[i], fill='yellow')
        elif lengthList[i] == max(lengthList):
            canvas.itemconfig(barList[i], fill='violet')



#Making a window using the Tk widget
window = tk.Tk()
window.title('Sorting Visualizer')
window.geometry('600x450')

#Making a Canvas within the window to display contents
canvas = tk.Canvas(window, width='600', height='400')
canvas.grid(column=0,row=0, columnspan = 50)

#Buttons
insert = tk.Button(window, text='Insertion Sort', command=insertion_sort)
select = tk.Button(window, text='Selection Sort', command=selection_sort)
bubble = tk.Button(window, text='Bubble Sort', command=bubble_sort)
shuf = tk.Button(window, text='Shuffle', command=generate)
bubble.grid(column=1,row=1)
insert.grid(column=2,row=1)
select.grid(column=3,row=1)
shuf.grid(column=0, row=1)

#Display Icon
photo = PhotoImage(file = "c:/Users/abby/Desktop/PYTHON/Sorting-Visualizer/icon.png")
window.iconphoto(True, photo)

# def play_sound():
#    pygame.mixer.music.load("c:/Users/abby/Desktop/PYTHON/Sorting-Visualizer/bg.mp3")
#    pygame.mixer.music.play()

# # # Add a Button widget
# # b1 = Button(window, text="Play Music", command=play_sound)
# # b1.pack(pady=600)

mixer.init()
mixer.music.load("c:/Users/abby/Desktop/PYTHON/Sorting-Visualizer/bg.mp3")
mixer.music.play()


generate()
window.mainloop()




