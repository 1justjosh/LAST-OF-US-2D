import pygame as pg
from src.main.settings import *


class Raider_1:
    def __init__(self):
        self.win = pg.display.get_surface()
        self.status_type = None

        self.load_assets()
        self.status = 'idle_r'

        self.sprite = self.status_type[self.status][0].subsurface((0, 0, 128, 128))
        self.sprite_x = 100

        self.anim_timer = 1

        self.x, self.y = 0, 350
        self.direction = pg.math.Vector2()

        self.walk_speed = 300
        self.run_speed = 500
        self.speed = self.walk_speed

        self.flipped = False
        self.running = False

    def load_assets(self):
        self.status_type = {'idle_r': [pg.image.load(RAIDER_1_PATH + 'idle.png').convert_alpha(), 6],
                            'idle_l': [
                                pg.transform.flip(pg.image.load(RAIDER_1_PATH + 'idle.png').convert_alpha(), True,
                                                  False), 6],

                            'walk_r': [pg.image.load(RAIDER_1_PATH + 'Walk.png').convert_alpha(), 8],
                            'walk_l': [
                                pg.transform.flip(pg.image.load(RAIDER_1_PATH + 'walk.png').convert_alpha(), True,
                                                  False), 8],

                            'run_r': [pg.image.load(RAIDER_1_PATH + 'run.png').convert_alpha(), 8],
                            'run_l': [pg.transform.flip(pg.image.load(RAIDER_1_PATH + 'run.png').convert_alpha(), True,
                                                        False), 8]}

    def animate(self, dt):
        self.sprite = self.status_type[self.status][0].subsurface((int(self.sprite_x), 0, 128, 128))
        self.sprite = pg.transform.scale(self.sprite, (300, 300))

        self.sprite_x = 128 * int(self.anim_timer)

        self.anim_timer += 10 * dt

        if self.anim_timer >= self.status_type[self.status][1]:
            self.anim_timer = 0

    def inputs(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_d]:
            self.direction.x = 1
            self.flipped = False
            self.moving = True

        elif keys[pg.K_a]:
            self.direction.x = -1
            self.flipped = True
            self.moving = True
        else:
            self.direction.x = 0
            self.moving = False

        if keys[pg.K_LSHIFT]:
            self.running = True
            self.speed = self.run_speed
        else:
            self.running = False
            self.speed = self.walk_speed

    def move(self, dt):
        self.x += self.direction.x * self.speed * dt


        if not self.moving:
            if self.flipped:
                self.status = 'idle_l'
            else:
                self.status = 'idle_r'
        else:
            if not self.flipped:
                if self.running:
                    self.status = 'run_r'
                else:
                    self.status = 'walk_r'
            else:
                if self.running:
                    self.status = 'run_l'
                else:
                    self.status = 'walk_l'

    def draw(self):
        self.win.blit(self.sprite, (self.x, self.y))

    def boundaries(self):
        if self.x >= 800:
            self.x = 800
        if self.x <= -72:
            self.x = -72

    def update(self, dt):
        try:
            self.inputs()
            self.animate(dt)
            self.move(dt)
            self.boundaries()
        except Exception:
            self.sprite_x = 0
