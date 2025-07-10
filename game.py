import pygame
from dino import Dino

class GameController:
    def __init__(self):
        # Cấu hình cơ bản
        self.SCREEN_WIDTH = 1100
        self.SCREEN_HEIGHT = 600
        self.FPS = 60

        # Tạo cửa sổ game
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Chrome Dino Game")

        self.clock = pygame.time.Clock()
        self.running = True

        # Khởi tạo Dino
        self.dino = Dino()

    def run(self):
        while self.running:
            self.clock.tick(self.FPS)
            self.handle_events()
            self.update()
            self.draw()

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.dino.update()

    def draw(self):
        self.screen.fill((255, 255, 255))  # Nền trắng
        self.dino.draw(self.screen)
        pygame.display.flip()
