#!/bin/python3
from turtle import *
from random import randint
speed(10)
penup()
goto(-140, 140)

for step in range(14):
  write(step, align='center')
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)
  
ada=Turtle()
ada.color('green')
ada.shape('turtle')


ada.penup()
ada.goto(-160, 100)
ada.pendown()

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()
  
sue=Turtle()
sue.color('red')
sue.shape('turtle')

sue.penup()
sue.goto(-160, 50)
sue.pendown()

for turn in range(90):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  sue.forward(randint(1,5))

  