import pygame
from game_object import GameObject

class NumberFont(GameObject):
    def __init__(self, x = 400, y = 20, width=5):
        start_x = 654
        start_y = 2
        digit_width = 10
        digit_height = 12

        animations = {
            "0": [GameObject.sprite_sheet.subsurface(pygame.Rect(start_x, start_y, digit_width, digit_height))],
        }

        super().__init__(x, y, animations, "0", layer=2)

        self.number = 0
        self.spacing = 2
        self.width = width

        self.digits = {}
        for i in range(10):
            rect = pygame.Rect(start_x + i * digit_width, start_y, digit_width, digit_height)
            img = GameObject.sprite_sheet.subsurface(rect).copy()
            if self.scale != 1:
                img = pygame.transform.scale(img, (digit_width * self.scale, digit_height * self.scale))
            self.digits[str(i)] = img

    def draw(self, screen):
        num_str = str(self.number).zfill(self.width)  # thêm số 0 cho đủ chiều rộng
        for i, char in enumerate(num_str):
            digit_img = self.digits.get(char)
            if digit_img:
                screen.blit(digit_img, (self.x + i * (digit_img.get_width() + self.spacing), self.y))
