import pygame
from game import GameController

def main():
    pygame.init()
    game = GameController()
    game.run()

if __name__ == "__main__":
    main()
