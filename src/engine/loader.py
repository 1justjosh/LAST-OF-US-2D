from src.engine.settings import *

def load_time_map(path,tile_size,size=None):
    base_image = pg.image.load(path)

    images = []

    for row in range(base_image.height // tile_size[1]):
        for col in range(base_image.width // tile_size[0]):
            img = base_image.subsurface(col * tile_size[0], row * tile_size[1],tile_size[0],tile_size[1])

            if size:
                img = pg.transform.scale(img,size)

            images.append(img)

    return images