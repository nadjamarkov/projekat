import pygame as pg
import pygamebg
import time

(sirina, visina) = (500, 600)
prozor = pygamebg.open_window(sirina, visina, "test")
pg.key.set_repeat(50,25)

#definisanje loptice
r = 20
y = 500
y0 = 500
a = 3
dt = 0
i = 0
trenje = 0.8

def crtanje():
    prozor.fill(pg.Color("white"))
    pg.draw.circle(prozor, pg.Color("red"), (250,y), r)

def obradi_dogadjaj(dogadjaj):
    global x, y, dt
    if dogadjaj.type == pg.KEYDOWN:  
        if dogadjaj.key == pg.K_UP:
            y = y - a*dt 
            dt = dt + 0.05         
            return True  
    elif dogadjaj.type == pg.KEYUP:
        if dogadjaj.key == pg.K_UP:
            '''
            i = 0
            while i<3:
                y = y - (a*dt - trenje) 
                prozor.fill(pg.Color("white"))
                pg.draw.circle(prozor, pg.Color("red"), (250,y), r) 
                i = i + 1  
                time.sleep(1)
            '''

pygamebg.event_loop(crtanje, obradi_dogadjaj)