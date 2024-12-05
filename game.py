import pygame
import random
class Game:
    def __init__(self, bird_img):
        self.bird = pygame.image.load(bird_img).convert_alpha()
        self.active = True
        self.gravity = 0.07
        self.bird_movement = 0
        self.rotated_bird = pygame.Surface((0,0))


    def resize_images(self):
        self.bird = pygame.transform.scale(self.bird, (51, 34))
        self.bird_rect = self.bird.get_rect(center = (70, 180))
    """def show_background(self, screen):
        screen.blit(self.background, (0,0))
    def show_ground(self, screen):
        screen.blit(self.ground, (self.ground_position, 650))
    def move_ground(self):
        self.ground_position -= 2
        self.ground_position %= 45
        self.ground_position -= 45"""
    def show_bird(self, screen):
        screen.blit(self.rotated_bird, self.bird_rect)
    def update_bird(self):
        self.bird_movement += self.gravity
        self.rotated_bird = self.rotate_bird()
        self.bird_rect.centery += self.bird_movement   
    def rotate_bird(self):
        new_bird = pygame.transform.rotozoom(self.bird, -self.bird_movement * 3, 1)
        return new_bird
    def flap(self):
        self.bird_movement = 0
        self.bird_movement -= 4.0 
"""def check_collision(self):
        for pipe in self.pipes:
            if self.bird_rect.colliderect(pipe):
                self.active = False
        if self.bird_rect.top <= -100 or self.bird_rect.bottom >= 650:
            self.active = False
    def update_score(self):
        self.score += 0.01
    def show_score(self, game_state, screen, color):
        score_surface = self.font.render(str(int(self.score)), True, color)
        score_rect = score_surface.get_rect(center = (202, 75))
        screen.blit(score_surface, score_rect)
        if game_state == "Game_Over":
            restart_text1 = self.font.render("Press Space Bar", True, color)
            restart_rect1 = restart_text1.get_rect(center=(200, 280))
            screen.blit(restart_text1, restart_rect1)
            restart_text2 = self.font.render("To Play Again", True, color)
            restart_rect2 = restart_text2.get_rect(center=(200, 340))
            screen.blit(restart_text2, restart_rect2)
            high_score_surface = self.font.render("High Score: {:d}".format(int(self.high_score)), True, color)
            high_score_rect = high_score_surface.get_rect(center = (200, 610))
            screen.blit(high_score_surface, high_score_rect)
    def game_over(self, screen, color):
        self.update_high_score()
        self.show_score("Game_Over", screen, color) 
    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score 
    def restart(self):
        self.active = True
        del self.pipes[:]
        del self.bills[:]
        self.bird_rect.center = (70, 180)
        self.bird_movement = 0
        self.score = 0"""



