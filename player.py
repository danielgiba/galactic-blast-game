import pygame
import config

class Player():
    def __init__(self, screen):
        self.screen = screen
        self.position = round(config.SCREEN_WIDTH / 2)
        self.image = pygame.image.load("imgs/player.png")
        self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))
        self.lives = 3  
        self.drawn_lives = 3 

    def render(self):
        self.rect = pygame.Rect(self.position, config.SCREEN_HEIGHT - config.SCALE, config.SCALE, config.SCALE)
        self.screen.blit(self.image, self.rect)

    def decrease_lives(self):
        self.lives -= 1  

    def draw_lives(self):
        heart_image = pygame.image.load("imgs/heart.png")
        heart_image = pygame.transform.scale(heart_image, (30, 30))
        for i in range(self.lives):
            self.screen.blit(heart_image, (10 + i * 35, 10))


    def collide(self, x, y):
        return self.rect.collidepoint(x, y)
