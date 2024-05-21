import pygame
import config
from alien import Alien, attack_random_alien
from bullet import Bullet
from player import Player
import datetime
import random

pygame.init()
pygame.font.init()

def load_scores():
    scores = []
    try:
        with open("scores.txt", "r") as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    try:
                        scores.append((parts[0], int(parts[1]), parts[2]))
                    except ValueError:
                        pass
    except FileNotFoundError:
        pass
    return scores

def save_scores(scores):
    with open("scores.txt", "w") as file:
        for score in scores:
            file.write(f"{score[0]},{score[1]},{score[2]}\n")

def main_menu(screen):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos):
                    load_game(screen)
                elif scoreboard_rect.collidepoint(event.pos):
                    scores = load_scores()
                    draw_scoreboard(screen, scores)
                    pygame.time.wait(3000)
                    draw_menu(screen)

        start_rect, scoreboard_rect = draw_menu(screen)

def draw_menu(screen):
    font = pygame.font.Font("fontgame.ttf", 24)
    screen.fill((0, 0, 0))
    start_text = font.render("START GAME", True, (255, 255, 255))
    scoreboard_text = font.render("SCOREBOARD", True, (255, 255, 255))
    start_rect = start_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 - 50))
    scoreboard_rect = scoreboard_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 + 50))
    screen.blit(start_text, start_rect)
    screen.blit(scoreboard_text, scoreboard_rect)
    pygame.display.flip()
    return start_rect, scoreboard_rect

def draw_scoreboard(screen, scores):
    font = pygame.font.Font("fontgame.ttf", 10)
    screen.fill((0, 0, 0))
    title_text = font.render("SCOREBOARD", True, (255, 255, 255))
    screen.blit(title_text, (10, 10))
    y_offset = 50
    for i, score in enumerate(scores):
        score_text = font.render(f"{i+1}. {score[0]} - {score[1]} - {score[2]}", True, (255, 255, 255))
        screen.blit(score_text, (10, y_offset + i * 25))
    pygame.display.flip()

def enter_player_name(screen):
    font = pygame.font.Font("fontgame.ttf", 12)
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    player_text = font.render("NUME PLAYER", True, (255, 255, 255))
    screen.blit(player_text, (input_box.x, input_box.y - 30))
    pygame.display.flip()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()

    return text

def game_over_screen(screen, score):
    font = pygame.font.Font("fontgame.ttf", 24)
    player_name = ""
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    scores = load_scores()
                    scores.append((player_name, score, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                    scores.sort(key=lambda x: x[1], reverse=True)
                    save_scores(scores)
                    done = True
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                elif event.unicode.isalnum():
                    player_name += event.unicode

        screen.fill((0, 0, 0))
        game_over_text = font.render("GAME OVER", True, (255, 255, 255))
        score_text = font.render(f"Scor: {score}", True, (255, 255, 255))
        name_prompt_text = font.render("Introduceți numele:", True, (255, 255, 255))
        player_name_text = font.render(player_name, True, (255, 255, 255))

        game_over_rect = game_over_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 - 50))
        score_rect = score_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2))
        name_prompt_rect = name_prompt_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 + 50))
        player_name_rect = player_name_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 + 100))

        screen.blit(game_over_text, game_over_rect)
        screen.blit(score_text, score_rect)
        screen.blit(name_prompt_text, name_prompt_rect)
        screen.blit(player_name_text, player_name_rect)

        pygame.display.flip()

        if done:
            pygame.quit()


def load_game(screen):
    game_running = True
    player = Player(screen)
    bullets = []
    aliens = []
    level = 0
    score = 0
    timer = 90 * 24
    clock = pygame.time.Clock()
    frames_per_second = 24
    bullet_timer = 0

    heart_image = pygame.image.load("imgs/heart.png")
    heart_image = pygame.transform.scale(heart_image, (30, 30))

    player_lives = 3

    while game_running:
        drop_aliens = False
        clock.tick(frames_per_second)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                if event.key == pygame.K_LEFT:
                    player.position -= config.SCALE
                if event.key == pygame.K_RIGHT:
                    player.position += config.SCALE
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(screen, player.position, config.SCREEN_HEIGHT - config.SCALE, -10)
                    bullets.append(bullet)

        for i in range(player_lives):
            screen.blit(heart_image, (10 + i * 35, 10))

        for bullet in bullets:
            if bullet.speed < 0:
                for alien in aliens:
                    if alien.collide(bullet.position[0], bullet.position[1]):
                        alien.killed = True
                        bullet.killed = True
                        score += 10

            bullet.update()

        for alien in aliens:
            if alien.killed:
                aliens.remove(alien)
                continue

        for bullet in bullets:
            if bullet.speed > 0:
                for i in range(player_lives):
                    if player.collide(bullet.rect.x, bullet.rect.y):
                        bullets.remove(bullet)
                        player_lives -= 1
                        break

        if player_lives <= 0:
            game_running = False

        screen.fill((0, 0, 0))
        for i in range(player_lives):
            screen.blit(heart_image, (10 + i * 35, 10))

        for alien in aliens:
            if alien.killed:
                aliens.remove(alien)
                continue

            alien.update()

            if alien.position[0] >= (config.SCREEN_WIDTH - 5) or alien.position[0] < 0:
                drop_aliens = True

        if drop_aliens:
            for alien in aliens:
                alien.drop()

        if bullet_timer >= 5 * frames_per_second:
            attack_random_alien(aliens, player, bullets)
            bullet_timer = 0

        if len(aliens) == 0:
            level += 1
            line = 1
            x_position = 0

            for _ in range(config.NUMBER_OF_ALIENS):
                if x_position * config.SCALE * 2 + 100 > config.SCREEN_WIDTH:
                    line += 1
                    x_position = 0

                alien = Alien(screen, x_position * config.SCALE * 2, line * config.SCALE, level)
                x_position += 1
                aliens.append(alien)

        for star in config.STARS:
            pygame.draw.circle(screen, config.WHITE, star, 1)
        player.render()

        for bullet in bullets:
            bullet.render()

        for alien in aliens:
            alien.render()

        font = pygame.font.Font("fontgame.ttf", 12)
        score_text = font.render(f"Scor: {score}", True, (255, 255, 255))
        timer_text = font.render(f"Timp: {timer//frames_per_second} sec", True, (255, 255, 255))
        screen.blit(score_text, (config.SCREEN_WIDTH - 250, 10))
        screen.blit(timer_text, (config.SCREEN_WIDTH - 250, 40))
        pygame.display.flip()

        timer -= 1
        bullet_timer += 1
        if timer <= 0:
            game_running = False

    font = pygame.font.Font("fontgame.ttf", 24)
    screen.fill((0, 0, 0))
    game_over_text = font.render("GAME OVER", True, (255, 255, 255))
    score_text = font.render(f"Scor: {score}", True, (255, 255, 255))
    screen.blit(game_over_text, (config.SCREEN_WIDTH // 2 - 100, config.SCREEN_HEIGHT // 2 - 50))
    screen.blit(score_text, (config.SCREEN_WIDTH // 2 - 50, config.SCREEN_HEIGHT // 2))
    pygame.display.flip()

    player_name = enter_player_name(screen)
    scores = load_scores()
    scores.append((player_name, score, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    scores.sort(key=lambda x: int(x[1]), reverse=True)
    save_scores(scores)
    pygame.time.wait(3000)
    main_menu(screen)

if __name__ == "__main__":
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    main_menu(screen)
    pygame.quit()
