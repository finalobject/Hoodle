
from tkinter import *
import random
import time
class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        self.x=0
        self.canvas_width=self.canvas.winfo_width()
        #按键绑定！
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
        
    def turn_left(self,evt):
        self.x = -5
    def turn_right(self,evt):
        self.x = 5
    def draw(self):
        self.canvas.move(self.id,self.x,0)
        
        pos = self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x=1
        if pos[2]>=self.canvas_width:
            self.x=-1
