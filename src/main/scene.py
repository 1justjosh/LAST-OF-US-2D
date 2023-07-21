import pygame as pg
from settings import *
from src.characters.raider_1 import Raider_1

class Scene:
    def __init__(self):
        self.win = pg.display.get_surface()
        self.bg = pg.image.load('res/nature/nature_1/orig.png').convert()
        self.bg = pg.transform.scale(self.bg,(WIDTH*3,HEIGHT))

        self.raider_1 = Raider_1()

        self.bg_x = 0

    def draw(self):
        self.win.blit(self.bg,(self.bg_x,0))
        self.raider_1.draw()

    def update(self,dt):
        self.raider_1.update(dt)

        if self.raider_1.x >= 800:
            if not self.bg_x <= - WIDTH*2:
                self.bg_x -= self.raider_1.speed * dt

        if self.raider_1.x <= -72:
            if not self.bg_x >= -72:
                self.bg_x += self.raider_1.speed * dt