import pygame as pg

class Debug:
    def __init__(self):
        self.win = pg.display.get_surface()

        pg.font.init()

        self.font = pg.font.Font('res/fonts/DigitalDisco-Thin.ttf',30)

    def render_fps(self,clock):
        text = self.font.render(f'[{clock.get_fps() :.0f}] FPS',True,(255,255,255))

        self.win.blit(text,(0,0))