import pygame as pg
import pygamebg

(sirina, visina) = (800, 500)
prozor = pygamebg.open_window(sirina, visina, "test")
prozor.fill(pg.Color("white"))

pygamebg.wait_loop()