import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Brush properties
BRUSH_SIZE = 10
brush_color = BLACK
drawing = False
erasing = False

# Current shape to draw
current_shape = None

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                drawing = True
                pos = pygame.mouse.get_pos()
                if current_shape == 'circle':
                    pygame.draw.circle(SCREEN, brush_color, pos, BRUSH_SIZE)
                elif current_shape == 'triangle':
                    # Draw a triangle with the first point as the mouse position
                    pygame.draw.polygon(SCREEN, brush_color, [(pos[0], pos[1] - BRUSH_SIZE),
                                                               (pos[0] + BRUSH_SIZE, pos[1] + BRUSH_SIZE),
                                                               (pos[0] - BRUSH_SIZE, pos[1] + BRUSH_SIZE)])
                # Add conditions for other shapes here

        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Clear screen
                SCREEN.fill(WHITE)
            elif event.key == pygame.K_c:  # Set current shape to circle
                current_shape = 'circle'
            elif event.key == pygame.K_t:  # Set current shape to triangle
                current_shape = 'triangle'
            elif event.key == pygame.K_r:  # Set brush color to red
                brush_color = (255, 0, 0)
            elif event.key == pygame.K_g:  # Set brush color to green
                brush_color = (0, 255, 0)
            elif event.key == pygame.K_b:  # Set brush color to blue
                brush_color = (0, 0, 255)
            # Add conditions for other colors here

    pygame.display.flip()

pygame.quit()
sys.exit()
