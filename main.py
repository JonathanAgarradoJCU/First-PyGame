import pygame
import time
import random
import pygame.font

WIDTH, HEIGHT = 1200, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Untitled Python Game")

BACKGROUND = pygame.transform.scale(pygame.image.load('windows-xp-bg.png'), (WIDTH, HEIGHT))
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VELOCITY = 8
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VELOCITY = 3
FONT = None


def initialize_fonts():
    global FONT
    pygame.font.init()
    FONT = pygame.font.SysFont('comicsans', 30)


def draw(player, elapsed_time, stars):
    WIN.blit(BACKGROUND, (0, 0))

    time_text = FONT.render(f"{round(elapsed_time)}s", 1, (0, 0, 0))
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, (255, 255, 0), player)

    for star in stars:
        pygame.draw.rect(WIN, (255, 0, 0), star)

    pygame.display.update()

initialize_fonts()


def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []
    hit = False

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT,
                                   STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

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

        for star in stars[:]:
            star.y += STAR_VELOCITY
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
            
        if hit:
            lost_text = FONT.render("LOL YOU SUCK NOOB", 1, (0, 0, 0))
            lost_text = pygame.transform.scale(lost_text, (270, 90))
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, stars)

    pygame.quit()


if __name__ == "__main__":
    main()
