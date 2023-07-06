import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the game window
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("3D Game")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Player position and rotation
player_x = width // 2
player_y = height // 2
player_angle = 0

# Define the map
map_width = 10
map_height = 10
tile_size = 50
map_data = [
    '1111111111',
    '1........1',
    '1........1',
    '1...111..1',
    '1........1',
    '1...111..1',
    '1........1',
    '1........1',
    '1........1',
    '1111111111',
]

# Set up the game clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_angle -= 0.05
    if keys[pygame.K_RIGHT]:
        player_angle += 0.05
    if keys[pygame.K_UP]:
        player_x += math.cos(player_angle) * 5
        player_y += math.sin(player_angle) * 5
    if keys[pygame.K_DOWN]:
        player_x -= math.cos(player_angle) * 5
        player_y -= math.sin(player_angle) * 5

    # Clear the screen
    window.fill(black)

    # Render the 3D view
    for x in range(width):
        # Calculate the distance from the player to the wall
        ray_angle = (player_angle - math.pi / 4) + (x / width) * (math.pi / 2)
        distance_to_wall = 0
        hit_wall = False

        # Ray casting
        while not hit_wall and distance_to_wall < 20:
            test_x = int(player_x + math.cos(ray_angle) * distance_to_wall)
            test_y = int(player_y + math.sin(ray_angle) * distance_to_wall)

            if (
                test_x < 0
                or test_x >= map_width * tile_size
                or test_y < 0
                or test_y >= map_height * tile_size
                or map_data[test_y // tile_size][test_x // tile_size] == '1'
            ):
                hit_wall = True
            else:
                distance_to_wall += 0.1

        # Calculate the ceiling and floor heights
        ceiling = int(height / 2 - height / distance_to_wall)
        floor = height - ceiling

        # Draw the wall slice
        pygame.draw.line(window, white, (x, 0), (x, ceiling), 2)
        pygame.draw.line(window, white, (x, floor), (x, height), 2)

    # Draw the player
    pygame.draw.circle(window, white, (int(player_x), int(player_y)), 5)

    # Update the game display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
