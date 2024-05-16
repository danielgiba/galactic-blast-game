import pygame
import config
from bullet import Bullet
import random

class Alien():
    def __init__(self, screen, x_position, y_position, speed):
        self.screen = screen
        self.position = [x_position, y_position]
        self.image = pygame.image.load("imgs/alien.png")
        self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))
        self.speed = speed
        self.killed = False
        self.last_shot_time = 0

    def render(self):
        self.rect = pygame.Rect(self.position[0], self.position[1], round(config.SCALE), round(config.SCALE))
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.position[0] = self.position[0] + self.speed

    def drop(self):
        self.position[1] = self.position[1] + config.SCALE
        self.speed = -self.speed

    def shoot_bullet(self, player, bullets):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= 5000:
            bullet = Bullet(self.screen, self.position[0] + config.SCALE // 2, self.position[1] + config.SCALE, 5)
            bullets.append(bullet)
            self.last_shot_time = current_time

    def collide(self, x, y):
        if self.killed:
            return False

        if x <= (self.position[0] + config.SCALE) and x > self.position[0] and y <= (self.position[1] + config.SCALE) and y > self.position[1]:
            return True
        return False

def attack_random_alien(aliens, player, bullets):
    alive_aliens = [alien for alien in aliens if not alien.killed]
    if alive_aliens:
        alien = random.choice(alive_aliens)
        alien.shoot_bullet(player, bullets)

