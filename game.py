import pygame, sys
import time
import random


pygame.init()
pygame.font.init()

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
car_width=100

gameDisplay=pygame.display.set_mode((1000,800))
pygame.display.set_caption('RACE RALLY!')
clock=pygame.time.Clock()

carimg=pygame.image.load('C:/users/harshal/Desktop/car.png')




myfont=pygame.font.SysFont('Comic Sans MS',70)


def car(x,y):
      gameDisplay.blit(carimg,(x,y))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])  
    

def crash():
    display_msg('GAME OVER!')

def play():
  crashed = False    
  x=(800 * 0.6)
  y=(600 * 0.7)
  x_change=0
  thing_startx = random.randrange(0, 800)
  thing_starty = -600
  thing_speed = 6
  thing_width = 100
  thing_height = 100

  while not crashed:

     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0   
      
     x=x + x_change     
     gameDisplay.fill(white)
     car(x,y)
     things(thing_startx, thing_starty, thing_width, thing_height, black)
     thing_starty += thing_speed
     car(x,y)

     if thing_starty > 600:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,800)
     if y==100+thing_starty and thing_startx<x<thing_startx+100:
        crash()
     if y==100+thing_starty and thing_startx<x+200<thing_startx+100:
         crash()
     if  x > 820 or x < 0:
       crash()
     pygame.display.update() 
     clock.tick(200)

def display_msg(text):
    textsurface = myfont.render('GAME OVER!', False, (0, 0, 0))
    gameDisplay.blit(textsurface,(320,50))
    pygame.display.update()

    time.sleep(1)
    play() 

play()        
pygame.quit()
quit()
