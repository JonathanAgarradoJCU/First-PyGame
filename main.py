import pygame
import time
import random

WIDTH, HEIGHT = 1200, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Untitled Python Game")

BACKGROUND = pygame.transform.scale(pygame.image.load('Windows-XP-BG.png'), (WIDTH, HEIGHT))

def draw(player, elapsed_time):
    WIN.blit(BACKGROUND, (0, 0))
    pygame.draw.rect(WIN, (255, 0, 0), player)
    pygame.display.update()

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_VELOCITY = 8

def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    while run:
        clock.tick(60)
        elapsed_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] and player.x - PLAYER_VELOCITY >= 0:
            player.x -= PLAYER_VELOCITY
        
        if keys_pressed[pygame.K_d] and player.x + PLAYER_VELOCITY + PLAYER_WIDTH <= WIDTH:
            player.x += PLAYER_VELOCITY

        if keys_pressed[pygame.K_w] and player.y - PLAYER_VELOCITY >= 0:
            player.y -= PLAYER_VELOCITY

        if keys_pressed[pygame.K_s] and player.y + PLAYER_VELOCITY + PLAYER_HEIGHT <= HEIGHT:
            player.y += PLAYER_VELOCITY

                
        draw(player, elapsed_time)
        
    pygame.quit()

if __name__ == "__main__":
    main()
