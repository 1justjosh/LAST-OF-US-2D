from src.engine.settings import *
from src.engine.loader import *
from src.entities.player import Player

class World:
    def __init__(self):
        self.win = pg.display.get_surface()

        self.visible_sprites = pg.sprite.Group()
        self.character = "Raider_2"
        self.load_assets()

        self.player = Player(pg.Rect(0,0,100,100),self.visible_sprites,self.assets["player"])


    def load_assets(self):
        self.assets = {
            "player":{
                "idle":load_time_map(f"res/character/{self.character}/Idle.png",(128,128),size=(256,256)),
                "walk": load_time_map(f"res/character/{self.character}/Walk.png", (128, 128), size=(256, 256)),
                "attack1": load_time_map(f"res/character/{self.character}/Attack_1.png", (128, 128), size=(256, 256)),
            }
        }

    def render(self):
        self.visible_sprites.draw(self.win)

    def update(self, dt):
        self.visible_sprites.update(dt)
