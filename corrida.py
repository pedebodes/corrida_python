#!/bin/python3

from turtle import *
from random import randint

speed(0)
penup()
goto(-140,140)
# Plota Pista
for step in range(15):
  write(step, align = "center")
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)


# competidores #############################################
ada = Turtle()
# gerador cor automatica
ada.color([randint(0,255),randint(0,255),randint(0,255)])
ada.shape('turtle')

ada.penup()
ada.goto(-160,120)
ada.pendown()
ada.right(360)

bob = Turtle()
# gerador cor automatica
bob.color([randint(0,255),randint(0,255),randint(0,255)])
bob.shape('turtle')

bob.penup()
bob.goto(-160,100)
bob.pendown()
bob.right(360)

juca = Turtle()
juca.color([randint(0,255),randint(0,255),randint(0,255)])
juca.shape('turtle')
juca.penup()
juca.goto(-160,80)
juca.pendown()
juca.right(360)

opa = Turtle()
# gerador cor automatica
opa.color([randint(0,255),randint(0,255),randint(0,255)])
opa.shape('turtle')
opa.penup()
opa.goto(-160,60)
opa.pendown()
opa.right(360)

zica = Turtle()
# gerador cor automatica
zica.color([randint(0,255),randint(0,255),randint(0,255)])
zica.shape('turtle')
zica.penup()
zica.goto(-160,40)
zica.pendown()
zica.right(360)

epa = Turtle()
# gerador cor automatica
epa.color([randint(0,255),randint(0,255),randint(0,255)])
epa.shape('turtle')
epa.penup()
epa.goto(-160,20)
epa.pendown()
epa.right(360)


oxi = Turtle()
# gerador cor automatica
oxi.color([randint(0,255),randint(0,255),randint(0,255)])
oxi.shape('turtle')
oxi.penup()
oxi.goto(-160,0)
oxi.pendown()
oxi.right(360)
#########################################################


# gera valor aleatorio para corrida para cara competidor
for turn in range(100):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  juca.forward(randint(1,5))
  opa.forward(randint(1,5))
  zica.forward(randint(1,5))
  epa.forward(randint(1,5))
  oxi.forward(randint(1,5))
  
# faz girar no final da corrida  





