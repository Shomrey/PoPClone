import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    clock = pygame.time.Clock()
    done = False

    position = [30, 30]

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] : position[1] -= 3
        if pressed[pygame.K_DOWN] : position[1] += 3
        if pressed[pygame.K_LEFT] : position[0] -= 3
        if pressed[pygame.K_RIGHT] : position[0] += 3

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(position[0], position[1], 60, 60))
        pygame.display.flip()   # this call is required to perform updates to the game screen

        clock.tick(60)  # slows the execution to 60 fps


if __name__ == '__main__':
    main()

