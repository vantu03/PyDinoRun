import pygame
import random
from game_object import GameObject, global_objects

class Cloud(GameObject):
    def __init__(self):
        animations = {"idle": [
            GameObject.sprite_sheet.subsurface(pygame.Rect(86, 2, 46, 14)),
        ]}
        x = random.randint(1100, 1600)
        y = random.randint(50, 150)
        super().__init__(x, y, animations, "idle", layer=1)
        self.speed = 3

    def update(self):
        self.x -= self.speed
        if self.x + self.image.get_width() < 0:
            self.destroy()
        super().update()
