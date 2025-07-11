import pygame
import random
import cloud, game_object, dino, ground, cactus_small, bird, cactus_large, number_font, star, moon

class GameController:

    high_score = 0

    def __init__(self):
        self.SCREEN_WIDTH = 1200
        self.SCREEN_HEIGHT = 300
        self.FPS = 60

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Dino Run")

        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False

        self.score = 0
        self.background_is_dark = True
        self.game_tick = 0
        self.bg_color = [20, 20, 20]

        self.myBg = ground.Ground().add_to_game()
        self.myTrex = dino.Dino().add_to_game()
        self.scoreFont = number_font.NumberFont(x=1050).add_to_game()
        self.hscoreFont = number_font.NumberFont(x=900).add_to_game()
        self.hscoreFont.number = GameController.high_score
        self.myObstacle = None

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

            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if self.game_over and keys[pygame.K_SPACE]:
                    self.restart_game()

    def update(self):
        self.game_tick += 1

        if not self.game_over:
            for obj in game_object.global_objects:
                obj.update()

            #Kiểm tra va chạm
            if self.myObstacle and self.myTrex.is_colliding_with(self.myObstacle):
                self.game_over = True
                self.myTrex.change_state("dead")
                pass

            if not self.game_over:

                #+ điểm
                if self.game_tick % 10 == 0:
                    self.scoreFont.number += 1

                # Điểm cao nhất
                if self.scoreFont.number > self.hscoreFont.number:
                    GameController.high_score = self.hscoreFont.number = self.scoreFont.number

                # đổi màu
                if self.game_tick % 2000 == 0:
                    self.background_is_dark = not self.background_is_dark

                for i in range(3):
                    if self.background_is_dark:
                        self.bg_color[i] -= 1
                    else:
                        self.bg_color[i] += 1

                    if self.bg_color[i] < 20:
                        self.bg_color[i] = 20
                    if self.bg_color[i] > 255:
                        self.bg_color[i] = 255


                # Tăng tốc
                self.myBg.speed = 10 + self.scoreFont.number / 100

                # Sinh cloud, star
                if self.game_tick % 200 == 0:
                    cloud.Cloud().add_to_game()
                    if self.background_is_dark:
                        random.choice([star.Star(), moon.Moon()]).add_to_game()

                # Sinh chướng ngại vật

                if self.scoreFont.number > 25 and self.myObstacle not in game_object.global_objects:
                    self.myObstacle = random.choice([
                        cactus_small.CactusSmall(),
                        cactus_small.CactusSmall(),
                        bird.Bird(),
                        cactus_large.CactusLarge()
                    ])
                    self.myObstacle.speed = self.myBg.speed
                    self.myObstacle.add_to_game()

    def draw(self):

        self.screen.fill(tuple(self.bg_color))

        for obj in game_object.global_objects:
            obj.draw(self.screen)

        pygame.display.flip()

    def restart_game(self):
        game_object.global_objects.clear()
        self.__init__()