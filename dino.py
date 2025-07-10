from game_object import GameObject
import pygame

class Dino(GameObject):
    def __init__(self):
        animations = {
            "stand": [
                GameObject.sprite_sheet.subsurface(pygame.Rect(848, 2, 44, 47)),
                GameObject.sprite_sheet.subsurface(pygame.Rect(892, 2, 44, 47)),
            ],
            "run": [
                GameObject.sprite_sheet.subsurface(pygame.Rect(936, 2, 44, 47)),
                GameObject.sprite_sheet.subsurface(pygame.Rect(980, 2, 44, 47)),
            ],
            "jump": [
                GameObject.sprite_sheet.subsurface(pygame.Rect(1024, 2, 44, 47)),
            ],
            "duck": [
                GameObject.sprite_sheet.subsurface(pygame.Rect(1112, 2, 59, 47)),
                GameObject.sprite_sheet.subsurface(pygame.Rect(1171, 2, 59, 47)),
            ],
            "dead": [
                GameObject.sprite_sheet.subsurface(pygame.Rect(980, 0, 44, 47)),
            ],
        }

        super().__init__(x=80, y=280, animations=animations, state="run", layer=3)

        self.velocity_y = 0
        self.gravity = 1
        self.jump_force = -20
        self.is_jumping = False
        self.ground_y = self.y

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
