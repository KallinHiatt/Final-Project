import pygame
import sys
from game import Game
pygame.init()
screen = pygame.display.set_mode((400, 720))
clock = pygame.time.Clock()
game = Game('bird.webp')
game.resize_images()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game.active:
                game.flap()        
    if game.active:
        game.show_bird(screen)
        game.update_bird()
    clock.tick(120)
     
