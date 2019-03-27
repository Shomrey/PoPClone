import sys, pygame
pygame.init()

size = width, height = 760, 520
speed = [2, 2]
bg = pygame.transform.scale(pygame.image.load("bg.jpg"), [760, 520])
black = 0, 0, 0

edgeh = 315
edgew = 500


def collide(herorect):
    if herorect.top < edgeh < herorect.bottom and herorect.left < edgew:
        return True
    if herorect.bottom > edgeh > herorect.top and herorect.left < edgew:
        return True
    return False

screen = pygame.display.set_mode(size)

hero = pygame.transform.scale(pygame.image.load("player.jpg"), [50, 70])
herorect = hero.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    herorect = herorect.move(speed)
    if herorect.left < 0 or herorect.right > width:
        speed[0] = -speed[0]
    if herorect.top < 0 or herorect.bottom > height:
        speed[1] = -speed[1]
    if collide(herorect):
        speed[1] = -speed[1]
    screen.fill(black)
    screen.blit(bg,(0, 0))
    screen.blit(hero, herorect)
    pygame.display.flip()