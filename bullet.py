import pygame
import config

class Bullet():
    def __init__(self, screen, x_position, y_position, speed):
        self.screen = screen
        self.position = [x_position, y_position]
        self.image = pygame.image.load("imgs/bullet.png")
        self.image = pygame.transform.scale(self.image, (config.SCALE // 2, config.SCALE // 2))
        self.speed = speed
        self.killed = False

    def render(self):
        self.rect = pygame.Rect(self.position[0], self.position[1], round(config.SCALE // 2), round(config.SCALE // 2))
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.position[1] = self.position[1] + self.speed
