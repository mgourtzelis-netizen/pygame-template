import pygame
pygame.init() #initialization of pygame
screen = pygame.display.set_mode((800, 600)) # creates a window of 800x600 pixels

running = True # variable to control the main loop
while running: # runs if running is true
    for event in pygame.event.get(): # constantly checking for events
        if event.type == pygame.QUIT: # checks if the user has clicked the close button
            running = False # changes running to false and breaks the running loop

    screen.fill((255, 0, 0))  # Fill the window with red
    pygame.display.flip()  # Update the display
