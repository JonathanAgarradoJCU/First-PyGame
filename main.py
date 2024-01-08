import pygame
import time
import random

WIDTH, HEIGHT = 1200, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Untitled Python Game")

BACKGROUND = pygame.transform.scale(pygame.image.load('Windows-XP-BG.png'), (WIDTH, HEIGHT))

def draw(player):
    WIN.blit(BACKGROUND, (0, 0))
    pygame.draw.rect(WIN, (255, 0, 0), player)
    pygame.display.update()

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_VELOCITY = 1

def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]:
            player.x -= PLAYER_VELOCITY
        
        if keys_pressed[pygame.K_d]:
            player.x += PLAYER_VELOCITY

        if keys_pressed[pygame.K_w]:
            player.y -= PLAYER_VELOCITY

        if keys_pressed[pygame.K_s]:
            player.y += PLAYER_VELOCITY

                
        draw(player)
        
    pygame.quit()

if __name__ == "__main__":
    main()
