import pygame
import random

def redraw_screen(mole_image,screen,color,mole_x,mole_y):
    screen.fill("light blue")
    for i in range(1, 21):
        pygame.draw.line(screen, color, (i * 32, 0), (i * 32, 512))
    for i in range(1, 17):
        pygame.draw.line(screen, color, (0, i * 32), (640, i * 32))
    screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))


def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        color = "black"
        mole_x = 0
        mole_y = 0
        while running:
            redraw_screen(mole_image,screen,color,mole_x,mole_y)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (x,y) = event.pos
                    if mole_x < x< mole_x+32:
                        if mole_y <y < mole_y+32:
                            mole_x, mole_y = random.randint(0, 19)*32, random.randint(0, 15)*32
                            redraw_screen(mole_image, screen, color, mole_x, mole_y)

                pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
