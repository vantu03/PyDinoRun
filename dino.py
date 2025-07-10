from game_object import GameObject
import pygame

class Dino(GameObject):
    def __init__(self):
        animations = {
            "run": [pygame.image.load("Assets/Dino/DinoRun1.png"), pygame.image.load("Assets/Dino/DinoRun2.png")],
            "jump": [pygame.image.load("Assets/Dino/DinoJump.png")],
            "duck": [pygame.image.load("Assets/Dino/DinoDuck1.png"), pygame.image.load("Assets/Dino/DinoDuck2.png")],
            "dead": [pygame.image.load("Assets/Dino/DinoDead.png")],
        }

        super().__init__(x=80, y=310, animations=animations, state="run")

        # Thuộc tính nhảy
        self.velocity_y = 0
        self.gravity = 1
        self.jump_force = -20
        self.is_jumping = False
        self.ground_y = self.y  # mốc sàn để biết khi nào chạm đất

    def update(self):
        # Nếu đang nhảy thì áp dụng vật lý
        if self.is_jumping:
            self.velocity_y += self.gravity
            self.y += self.velocity_y

            # Chạm đất
            if self.y >= self.ground_y:
                self.y = self.ground_y
                self.velocity_y = 0
                self.is_jumping = False
                self.change_state("run")

        super().update()

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.velocity_y = self.jump_force
            self.change_state("jump")

    def handle_events(self):

        # Điều khiển chuyển trạng thái
        if not self.is_jumping:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                self.jump()
            elif keys[pygame.K_DOWN]:
                self.change_state("duck")
            else:
                self.change_state("run")