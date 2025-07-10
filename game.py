import pygame
import random
import cloud, game_object, dino, ground, cactus_small, bird, cactus_large
from cactus_large import CactusLarge


class GameController:

    high_score = 0

    def __init__(self):
        self.SCREEN_WIDTH = 1200
        self.SCREEN_HEIGHT = 300
        self.FPS = 60

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Chrome Dino Game")

        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False

        self.score = 0

        self.cloud_spawn_timer = 0
        self.next_cloud_spawn = random.randint(60, 180)

        self.obstacle_spawn_timer = 0
        self.next_obstacle_spawn = 100

        ground.Ground().add_to_game()
        self.myTrex = dino.Dino().add_to_game()
        cloud.Cloud().add_to_game()

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
        if not self.game_over:
            for obj in game_object.global_objects:
                obj.update()

            #Kiểm tra va chạm
            for obj in game_object.global_objects:
                if isinstance(obj, (bird.Bird, CactusLarge, cactus_small.CactusSmall)):
                    if self.myTrex.is_colliding_with(obj):
                        self.game_over = True
                        self.myTrex.change_state("dead")

            if not self.game_over:

                for obj in game_object.global_objects:
                    if isinstance(obj, (bird.Bird, cactus_small.CactusSmall, cactus_large.CactusLarge)):
                        if not obj.scored and obj.x + obj.image.get_width() < self.myTrex.x:
                            obj.scored = True
                            self.score += 1

                # Sinh cloud
                self.cloud_spawn_timer += 1
                if self.cloud_spawn_timer >= self.next_cloud_spawn:
                    cloud.Cloud().add_to_game()
                    self.cloud_spawn_timer = 0
                    self.next_cloud_spawn = random.randint(60, 180)

                # Sinh chướng ngại vật
                self.obstacle_spawn_timer += 1
                if self.obstacle_spawn_timer >= self.next_obstacle_spawn:
                    random.choice([cactus_small.CactusSmall(), cactus_small.CactusSmall(), bird.Bird(),
                                   cactus_large.CactusLarge()]).add_to_game()
                    self.obstacle_spawn_timer = 0
                    self.next_obstacle_spawn = 60

    def draw(self):
        self.screen.fill((255, 255, 255))
        for obj in game_object.global_objects:
            obj.draw(self.screen)



        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {int(self.score)}", True, (0, 0, 0))
        self.screen.blit(score_text, (1000, 20))

        # Hiển thị high score nếu muốn
        if self.game_over:
            if self.score > GameController.high_score:
                GameController.high_score = self.score

            hs_text = font.render(f"High Score: {int(GameController.high_score)}", True, (128, 128, 128))
            self.screen.blit(hs_text, (1000, 50))

        pygame.display.flip()

    def restart_game(self):
        game_object.global_objects.clear()
        self.__init__()