import pygame
import numpy as np

# Initialize game window and setup objects
pygame.init()
screen = pygame.display.set_mode((800, 600))

red_triangle = np.array([[400.0, 550.0], [450.0, 550.0], [425.0, 500.0]])
blue_triangle = np.array([[400.0, 150.0], [450.0, 150.0], [425.0, 100.0]])
center = np.mean(red_triangle, axis=0)

# Main game loop
running = True
while running:
    # Input handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        angle = np.radians(-0.1)
        red_triangle -= center
        red_triangle = np.dot(red_triangle, [[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        red_triangle += center
    if keys[pygame.K_RIGHT]:
        angle = np.radians(0.1)
        red_triangle -= center
        red_triangle = np.dot(red_triangle, [[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        red_triangle += center
    if keys[pygame.K_UP]:
        angle = np.arctan2(red_triangle[0][1] - red_triangle[2][1], red_triangle[0][0] - red_triangle[2][0])
        red_triangle[:, 0] += 0.5 * np.cos(angle)
        red_triangle[:, 1] += 0.5 * np.sin(angle)
    if keys[pygame.K_DOWN]:
        angle = np.arctan2(red_triangle[0][1] - red_triangle[2][1], red_triangle[0][0] - red_triangle[2][0])
        red_triangle[:, 0] -= 0.5 * np.cos(angle)
        red_triangle[:, 1] -= 0.5 * np.sin(angle)

    # Render objects
    screen.fill((0, 0, 0))
    pygame.draw.polygon(screen, (255, 0, 0), red_triangle.astype(int), 0)
    pygame.draw.polygon(screen, (0, 0, 255), blue_triangle.astype(int), 0)

    # Update game window
    pygame.display.flip()

# Close game window and de-initialize resources
pygame.quit()
