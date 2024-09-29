from src.engine.settings import *
from src.engine.screen import Screen

class Window:
    def __init__(self):
        self.win = pg.display.set_mode(RES)

        self.clock = pg.time.Clock()
        self.screen = Screen()

        self.running = True

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        dt = self.clock.tick(FPS) / 1000

        self.screen.update(dt)

    def render(self):
        self.win.fill((20,40,80))

        self.screen.render()

        pg.display.flip()

    def run(self):
        while self.running:
            self.event_handler()
            self.update()
            self.render()
