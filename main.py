# allows using code from open source pygame lib
import pygame 
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()



# ensures main() is only called when this file is run directly# wont run if imported as a module
# "pythonic" way to structure an executable program in python
# just calling main() will work but it's not "proper"
if __name__ == "__main__":
    main()
