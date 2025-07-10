import pygame

class GameObject:
    def __init__(self, x, y, animations: dict[str, list[pygame.Surface]], state: str = "idle"):
        self.x = x
        self.y = y
        self.animations = animations
        self.state = state
        self.frame_index = 0
        self.image = self.animations[self.state][self.frame_index]
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.animation_speed = 0.2  # tốc độ chuyển frame
        self.frame_timer = 0

    def update(self):
        frames = self.animations[self.state]
        self.frame_timer += self.animation_speed
        if self.frame_timer >= 1:
            self.frame_index = (self.frame_index + 1) % len(frames)
            self.frame_timer = 0
        self.image = frames[self.frame_index]
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.handle_events()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def change_state(self, new_state: str):
        if new_state != self.state:
            self.state = new_state
            self.frame_index = 0
            self.frame_timer = 0

    def handle_events(self):
        pass