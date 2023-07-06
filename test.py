import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("2D Game")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Define the player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height-50)

    def update(self):
        # Handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

# Define the obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((random.randint(20, 50), random.randint(20, 50)))
        self.image.fill((random.randint(50, 200), random.randint(50, 200), random.randint(50, 200)))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width)
        self.rect.y = random.randint(0, height)

    def update(self):
        # Move the obstacle
        self.rect.y += 3
        if self.rect.y > height:
            self.rect.y = 0
            self.rect.x = random.randint(0, width)

# Create player object
player = Player()

# Create obstacle group
obstacles = pygame.sprite.Group()

# Add obstacles to the group
for _ in range(1):
    obstacle = Obstacle()
    obstacles.add(obstacle)

# Set up the game clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    player.update()
    obstacles.update()

    # Check for collisions
    if pygame.sprite.spritecollide(player, obstacles, False):
        running = False

    # Draw
    window.fill(black)
    window.blit(player.image, player.rect)
    obstacles.draw(window)

    # Update the game display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
