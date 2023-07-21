import pygame as pg
from settings import *
from scene import Scene
from debug import Debug

class Window:
    def __init__(self):
        self.win = pg.display.set_mode(RES)

        self.dt = 0.0
        self.clock = pg.time.Clock()

        self.debug = Debug()

        self.scene = Scene()


    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

    def update(self):
        self.dt = self.clock.tick() / 1000

        self.scene.update(self.dt)

        pg.display.set_caption(f'{TITLE}')

    def draw(self):
        self.scene.draw()

        self.debug.render_fps(self.clock)

        pg.display.flip()

    def run(self):
        while True:
            self.events()
            self.update()
            self.draw()
