from tkinter import *
import math

#intial window

root = Tk()
root.title('Pomodoro')
root.config(padx=75,pady=45,bg='white')

#variables---fonts,colors required

font_style = 'courier'
bg_color = 'orange'
WORK_TIME =25
SHORT_BREAK=5
LONG_BREAK=20
repetitions=0

#creating UI part

canvas= Canvas(width=1000,height=1080)
tomato_img=PhotoImage(file="pls.jpg")
canvas.create_image(500,540,image=tomato_img)
#canvas.grid(row=1,column=1)
canvas.pack()





#mianloop for events
root.mainloop()