import pygame
import random
from game_object import GameObject

class Star(GameObject):
    def __init__(self):
        animations = {"idle": [
            GameObject.sprite_sheet.subsurface(pygame.Rect(644, 2, 10, 9)),
            GameObject.sprite_sheet.subsurface(pygame.Rect(644, 11, 10, 9)),
            GameObject.sprite_sheet.subsurface(pygame.Rect(644, 20, 10, 9)),
        ]}
        x = 300
        y = random.randint(50, 150)
        super().__init__(x, y, animations, "idle", layer=1)
        self.speed = 2

    def update(self):
        self.x -= self.speed
        if self.x + self.image.get_width() < 0:
            self.destroy()
        super().update()
