from src.engine.settings import *
from src.engine.world import World

class Screen:
    def __init__(self):
        self.world = World()

    def render(self):
        self.world.render()

    def update(self,dt):
        self.world.update(dt)
