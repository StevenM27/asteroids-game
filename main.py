import pygame
from constants import *
from player import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Checking to see that the constants were imported
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Restrict to 60 FPS
    clock = pygame.time.Clock()
    dt = 0

    # Create groups for managing our game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    # Create Player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0, 0, 0))

        # 60 FPS
        dt = clock.tick(60) / 1000

        # Update all objects
        updatable.update(dt)

        # Draw all objects
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()