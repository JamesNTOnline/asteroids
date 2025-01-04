# allows using code from open source pygame lib
import pygame 
import sys 

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids")
    
    # game object groups 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable) # static field adding all Players to groups
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # game objects
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()

    while True: # game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for sprite in updatable:
            sprite.update(dt)
        for sprite in asteroids:
            if sprite.collides(player):
                sys.exit("Game over!")
        for sprite in drawable:
            sprite.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000



# ensures main() is only called when this file is run directly# wont run if imported as a module
# "pythonic" way to structure an executable program in python
# just calling main() will work but it's not "proper"
if __name__ == "__main__":
    main()
