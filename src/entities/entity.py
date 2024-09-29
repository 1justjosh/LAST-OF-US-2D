from src.engine.settings import *


class Entity(pg.sprite.Sprite):
    def __init__(self, rect, group, assets=None):
        super().__init__(group)
        self.status = "idle"
        self.flipped = False

        self.direction = pg.math.Vector2()
        self.speed = 400

        self.assets = assets
        self.index = 0
        self.anim_speed = 7

        self.attacking = False

        self.image = pg.Surface((rect.width, rect.height))
        self.rect = self.image.get_rect(center=(rect.x, rect.y))

    def animate(self, dt):
        if self.assets:
            self.index += self.anim_speed * dt

            if self.index >= len(self.assets[self.status]):
                if self.attacking:
                    self.attacking = False
                self.index = 0

            self.image = pg.transform.flip(self.assets[self.status][int(self.index)],self.flipped,False)

    def move(self,dt):
        self.rect.x += self.direction.x * self.speed * dt
        self.rect.x += self.direction.y * self.speed * dt
