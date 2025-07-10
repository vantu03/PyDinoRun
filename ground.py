import pygame
from game_object import GameObject

class Ground(GameObject):
    def __init__(self):
        animations = {"idle": [
            GameObject.sprite_sheet.subsurface(pygame.Rect(2, 54, 1200, 15)),
        ]}
        super().__init__(x=0, y=280, animations=animations, state="idle", layer=0)

        self.x2 = self.image.get_width()
        self.speed = 10

    def update(self):
        self.x -= self.speed
        self.x2 -= self.speed

        if self.x + self.image.get_width() < 0:
            self.x = self.x2 + self.image.get_width()
        if self.x2 + self.image.get_width() < 0:
            self.x2 = self.x + self.image.get_width()

        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y - self.image.get_height()))
        screen.blit(self.image, (self.x2, self.y - self.image.get_height()))
