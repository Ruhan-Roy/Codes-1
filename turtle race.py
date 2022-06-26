#!/bin/python3

from turtle import *
from random import randint

speed(0)
penup()
goto(-140 , 140)

for step in range(16):
  write(step, align='center')
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)
  
ada = Turtle()
ada.color('dark orange')
ada.shape('turtle')

ada.penup()
ada.goto(-160 , 100)
ada.pendown()

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160 , 70)
bob.pendown()

tim = Turtle()
tim.color('red')
tim.shape('turtle')

tim.penup()
tim.goto(-160 , 40)
tim.pendown()

jim = Turtle()
jim.color('green')
jim.shape('turtle')

jim.penup()
jim.goto(-160 , 10)
jim.pendown()

for turn in range(100):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  tim.forward(randint(1,5))
  jim.forward(randint(1,5))
