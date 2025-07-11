import pygame
import random
from game_object import GameObject

class Moon(GameObject):
    def __init__(self):
        animations = {
            "defect_r1": [GameObject.sprite_sheet.subsurface(pygame.Rect(484, 2, 20, 40))],
            "defect_r2": [GameObject.sprite_sheet.subsurface(pygame.Rect(504, 2, 20, 40))],
            "defect_r3": [GameObject.sprite_sheet.subsurface(pygame.Rect(524, 2, 20, 40))],
            "round":      [GameObject.sprite_sheet.subsurface(pygame.Rect(564, 2, 40, 40))],
            "defect_l1": [GameObject.sprite_sheet.subsurface(pygame.Rect(584, 2, 20, 40))],
            "defect_l2": [GameObject.sprite_sheet.subsurface(pygame.Rect(604, 2, 20, 40))],
            "defect_l3": [GameObject.sprite_sheet.subsurface(pygame.Rect(624, 2, 20, 40))],
        }
        x = 300
        y = random.randint(50, 150)
        super().__init__(x, y, animations, random.choice(list(animations.keys())), layer=1)
        self.speed = 2

    def update(self):
        self.x -= self.speed
        if self.x + self.image.get_width() < 0:
            self.destroy()
        super().update()
