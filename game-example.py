import pygame
import sys
import random

# Initialize pygame modules
pygame.init()

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
BLUE = (50, 150, 255)

# Set up the display window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Block Dodger")
clock = pygame.time.Clock()

# Player Properties
player_width = 50
player_height = 50
player_x = (SCREEN_WIDTH - player_width) // 2
player_y = SCREEN_HEIGHT - player_height - 10
player_speed = 8

# Enemy (Falling Block) Properties
enemy_width = 50
enemy_height = 50
enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)
enemy_y = -enemy_height
enemy_speed = 5

# Score tracking
score = 0
font = pygame.font.SysFont("Arial", 30)

# Main Game Loop
running = True
while running:
    # 1. Handle Input/Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys currently pressed
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player_x > 0:
        player_x -= player_speed
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed

    # 2. Update Game Logic
    # Move enemy down
    enemy_y += enemy_speed

    # Reset enemy when it falls off screen
    if enemy_y > SCREEN_HEIGHT:
        enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)
        enemy_y = -enemy_height
        score += 1
        # Gently increase difficulty
        if score % 5 == 0:
            enemy_speed += 1

    # Define bounding rectangles for collision check
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)

    # Collision check
    if player_rect.colliderect(enemy_rect):
        print(f"Game Over! You Scored: {score}")
        running = False

    # 3. Draw Everything
    screen.fill(BLACK)  # Clear screen with BLACK background

    # Draw Player and Enemy
    pygame.draw.rect(screen, BLUE, player_rect)
    pygame.draw.rect(screen, RED, enemy_rect)

    # Render and display score text
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Refresh screen and maintain frame rate
    pygame.display.update()
    clock.tick(FPS)

# Properly close the window
pygame.quit()
sys.exit()
