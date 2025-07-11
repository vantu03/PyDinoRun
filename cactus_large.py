import pygame
import random
from game_object import GameObject

class CactusLarge(GameObject):
    def __init__(self):
        animations = {"idle": [
            GameObject.sprite_sheet.subsurface(pygame.Rect(332, 2, 25 * random.randint(1, 4), 50)),
        ]}

        x = 1200
        y = 280

        super().__init__(x, y, animations, "idle", layer=2)
        self.speed = 10

    def update(self):
        self.x -= self.speed
        if self.x + self.image.get_width() < 0:
            self.destroy()

        super().update()
