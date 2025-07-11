import pygame
import os, sys

global_objects = []

class GameObject:

    sprite_sheet = pygame.image.load("Assets/x1.png")
    scale = 2

    def __init__(self, x, y, animations: dict[str, list[pygame.Surface]], state: str = "idle", layer: int = 1):
        self.x = x
        self.y = y
        self.animations = animations
        self.state = state
        self.frame_index = 0
        self.image = self.animations[self.state][self.frame_index]
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.image)

        self.animation_speed = 0.2
        self.frame_timer = 0
        self.layer = layer
        self.scale_frames()

    def scale_frames(self):
        for state in self.animations:
            self.animations[state] = [
                pygame.transform.scale(frame, (frame.get_width() * self.scale, frame.get_height() * self.scale))
                for frame in self.animations[state]
            ]

    def update(self):
        frames = self.animations[self.state]
        self.frame_timer += self.animation_speed
        if self.frame_timer >= 1:
            self.frame_index = (self.frame_index + 1) % len(frames)
            self.frame_timer = 0
        self.image = frames[self.frame_index]

        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.image)


        self.handle_events()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y - self.image.get_height()))

    def change_state(self, new_state: str):
        if new_state != self.state:
            self.state = new_state
            self.frame_index = 0
            self.frame_timer = 0

    def handle_events(self):
        pass

    def destroy(self):
        if self in global_objects:
            global_objects.remove(self)

    def add_to_game(self):
        global_objects.append(self)
        global_objects.sort(key=lambda obj: obj.layer)
        return self

    def is_colliding_with(self, other):
        offset = (other.rect.x - self.rect.x, other.rect.y - self.rect.y)
        return self.mask.overlap(other.mask, offset) is not None