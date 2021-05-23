import pygame 
import pygamebg
import tkinter
from tkinter import messagebox

pygame.init()

(sirina, visina) = (1000,600)
prozor = pygamebg.open_window(sirina, visina, "Test")
prozor.fill(pygame.Color("white"))
pygame.draw.rect(prozor, pygame.Color("black"), (0,100,1000,100))
pygame.draw.rect(prozor, pygame.Color("yellow"), (650,0,10,1000))
pygame.draw.rect(prozor, pygame.Color("black"), (0,350,1000,100))
x = 50
y= 150
x1 = 50
y1 = 400
velocity = 1
velocity1 = 1
def update():
    global x,y,velocity,x1,y1,velocity1
    pressed = pygame.key.get_pressed()
    prozor.fill(pygame.Color("white"))
    pygame.draw.rect(prozor, pygame.Color("black"), (0,100,1000,100))
    pygame.draw.rect(prozor, pygame.Color("black"), (0,350,1000,100))
    pygame.draw.rect(prozor, pygame.Color("yellow"), (650,0,10,1000))
    if y>100 and y<200:
        velocity = 4
    else:
        velocity = 1
    if pressed[pygame.K_RIGHT]:
        x+=velocity
    if pressed[pygame.K_LEFT]:
        x-=velocity
    if pressed[pygame.K_DOWN]:
        y+=velocity
    if pressed[pygame.K_UP]:
        y-=velocity
    if x>690:
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showinfo("Pobeda!", "Prvi igrač je pobedio")
        raise Exception()
    pygame.draw.circle(prozor, pygame.Color("red"), (x,y), 30)
    if y1>350 and y1<450:
        velocity1 = 4
    else:
        velocity1 = 1
    if pressed[pygame.K_d]:
        x1+=velocity1
    if pressed[pygame.K_a]:
        x1-=velocity1
    if pressed[pygame.K_s]:
        y1+=velocity1
    if pressed[pygame.K_w]:
        y1-=velocity1
    if x1>690:
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showinfo("Pobeda!", "Drugi igrač je pobedio")
        raise Exception()
    pygame.draw.circle(prozor, pygame.Color("magenta"), (x1,y1), 30)
pygamebg.frame_loop(30, update)
'''
while running:
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x0+=1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x0-=1
        
    prozor.fill(pygame.Color("white"))
    pygame.draw.circle(prozor, pygame.Color("red"), (x0,y0), 10)
    pygame.display.update()
    '''
