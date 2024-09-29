from src.engine.settings import *
from src.entities.entity import Entity

class Player(Entity):
    def __init__(self,rect,group,assets):
        super().__init__(rect,group,assets)

        self.image = assets["idle"][0]

    def input(self):
        key = pg.key.get_pressed()

        if key[pg.K_SPACE]:
            if not self.attacking:
                self.attacking = True
                self.index = 0
                self.status = "attack1"

        if key[pg.K_d]:
            self.direction.x = 1
            self.flipped = False
        elif key[pg.K_a]:
            self.direction.x = -1
            self.flipped = True
        else:
            self.direction.x = 0

    def get_status(self):
        if not self.attacking:
            if self.direction.x == 0:
                self.status = "idle"
            else:
                self.status = "walk"

    def update(self,dt):
        self.input()
        self.get_status()

        if not self.attacking:
            self.move(dt)

        self.animate(dt)
