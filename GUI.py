#from __future__ import unicode_literals
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from functools import partial
from PIL import Image, ImageTk


stack = []

"""

Given a number of cents, return the least number of coins that sums to that amount

"""
#from typing import Iterables

def solve(cents):
    
    result = 0
    quarter = 25
    dime = 10
    nickel = 5
    penny = 1
    difference = abs(cents - result)
    
    if cents == 25:
            result += quarter
            return stack.append("25")
    if cents == 10:
            result += dime
            return stack.append("10")
    if cents == 5:
            result += nickel
            return stack.append("5")
    if cents == 1:
            result += penny
            return stack.append("1")
            
    while cents != result:
        
        while difference >= quarter:
                result += quarter
                stack.append("25")
                difference = abs(cents - result)

            
        while difference >= dime and difference < quarter:
            result += dime
            stack.append("10")
            difference = abs(cents - result)

            
        while difference >= nickel and difference < dime:
            result += nickel
            stack.append("5")
            difference = abs(cents - result)

            
        while difference >= penny and difference < nickel:
            result += penny
            stack.append("1")
            difference = abs(cents - result)
            
        newResult = output(stack)
        return newResult
            
            
        
def output(stack):       
    Quarter = 0
    Dime = 0
    Nickel = 0
    Penny = 0
    for num in stack:
        if num == "1":
            Penny += 1
        elif num == "5":
            Nickel += 1
        elif num == "10":
            Dime += 1
        elif num == "25":
            Quarter += 1
    #print(f"Minimum coins required are: {Quarter} Quarters, {Dime} Dimes, {Nickel} Nickels, {Penny} Pennies ")
    messagebox.showinfo('Result', f"Minimum coins required are:\n{Quarter} Quarters\n{Dime} Dimes\n{Nickel} Nickels\n{Penny} Pennies")
    


root = tk.Tk()
root.title('Minimum Coins Needed')
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

image_orig = Image.open(r"C:\Users\shant\Downloads\coins.png")
#image_orig = Image.open("./coins.png")
image = image_orig.copy()

photo = ImageTk.PhotoImage(image)
root.background_label = tk.Label(image=photo)
root.background_label.image = photo
root.background_label.place(x=0,y=0)

def on_resize(event):
    print('RESIZED')
    if not isinstance(event.widget, tk.Tk):
        return
    width = event.width
    height = event.height

    image = image_orig.copy().resize((width, height))

    root.background_label.image = photo
    root.background_label.place(x=0,y=0)

root.bind('<Configure>', on_resize)

label1 = tk.Label(root, text= "Enter an Amount", justify=CENTER)
label1.config(font=("Arial",20))
canvas1.create_window(200, 210, window=label1)
label1.place(relx = 0.8,rely = 0.2,anchor ='ne')


label2 = tk.Label(root, text= "Click Calculate to see the Result", font=("Arial",9))
canvas1.create_window(200, 230, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

button1 = tk.Button(text='Calculate',command= lambda: solve(int(entry1.get())), bg='palegreen2', font=('Arial', 11, 'bold'))
canvas1.create_window(200, 180, window=button1)
button1.pack()



root.mainloop()


