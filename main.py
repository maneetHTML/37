import pygame
import random
import sys
pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blue and Red Sprite Game")
BLUE, RED, BLACK, WHITE = (0, 0, 255), (255, 0, 0), (0, 0, 0), (255, 255, 255)
font = pygame.font.Font(None, 50)
blue_size = 20
blue_pos = [200, 200]
speed = 5
score = 0
red_pos = [random.randint(0, WIDTH - 20), random.randint(0, HEIGHT - 20)]
game_state = "playing"
bg = pygame.Surface((WIDTH, HEIGHT))
bg.fill(WHITE)

clock = pygame.time.Clock()

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    if game_state == "playing":
        if keys[pygame.K_LEFT]:  blue_pos[0] -= speed
        if keys[pygame.K_RIGHT]: blue_pos[0] += speed
        if keys[pygame.K_UP]:    blue_pos[1] -= speed
        if keys[pygame.K_DOWN]:  blue_pos[1] += speed
        blue_rect = pygame.Rect(*blue_pos, 20, 20)
        red_rect = pygame.Rect(*red_pos, 20, 20)
        if blue_rect.colliderect(red_rect):
            score += 1
            blue_size += 20
            red_pos = [random.randint(0, WIDTH - 20), random.randint(0, HEIGHT - 20)]
        if score >= 10:
            game_state = "win"

        if (blue_pos[0] < 0 or blue_pos[0] + 20 > WIDTH or
            blue_pos[1] < 0 or blue_pos[1] + 20 > HEIGHT):
            game_state = "game_over"

        screen.blit(bg, (0, 0))
        pygame.draw.rect(screen, BLUE, blue_rect)
        pygame.draw.rect(screen, RED, red_rect)
        screen.blit(font.render(f"Score: {score}", True, BLACK), (10, 10))

    else:
        screen.fill(BLACK)
        msg = "You Win!" if game_state == "win" else "Game Over"
        msg_text = font.render(msg, True, WHITE)
        screen.blit(msg_text, (WIDTH // 2 - msg_text.get_width() // 2, HEIGHT // 2 - 50))
        screen.blit(font.render(f"Score: {score}", True, WHITE), (WIDTH // 2 - 60, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(30)
