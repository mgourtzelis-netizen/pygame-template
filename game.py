import pygame
pygame.init() #initialization of pygame
screen = pygame.display.set_mode((800, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 0, 0))  # Fill the window with red
    pygame.display.flip()  # Update the display
