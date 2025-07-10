import pygame
import random
from game_object import GameObject

class Bird(GameObject):
    def __init__(self):
        bird_images = [
            GameObject.sprite_sheet.subsurface(pygame.Rect(134, 2, 46, 40)),
            GameObject.sprite_sheet.subsurface(pygame.Rect(180, 2, 46, 40)),
        ]
        animations = {"fly": bird_images}

        x = 1200
        y = random.choice([180, 260])
        super().__init__(x, y, animations, "fly", layer=2)

        self.speed = 10

    def update(self):
        self.x -= self.speed
        if self.x + self.image.get_width() < 0:
            self.destroy()
        super().update()
