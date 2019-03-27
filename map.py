import sys, pygame
pygame.init()

size = width, height = 760, 520
speed = [0, 0]
bg = pygame.transform.scale(pygame.image.load("bg.jpg"), [760, 520])
black = 0, 0, 0

edgeh = 315
edgew = 500

def collide(herorect):
    #if ballrect.left < 0 or ballrect.right > width or ballrect.top < 0 or ballrect.bottom > height:
     #   return True
    if herorect.top < edgeh < herorect.bottom and herorect.left < edgew:
        return True
    if herorect.bottom > edgeh > herorect.top and herorect.left < edgew:
        return True
    return False

screen = pygame.display.set_mode(size)

hero = pygame.transform.scale(pygame.image.load("player.jpg"), [50, 70])
herorect = hero.get_rect()
herorect.y = 245
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == 26:
            speed[1] = 1
            pygame.time.set_timer(26, 0)
    key=pygame.key.get_pressed()
    if key[pygame.K_RIGHT]: speed[0] = 1
    if key[pygame.K_LEFT]: speed[0] = -1
    if key[pygame.K_UP]:
        speed[1] = -1
        pygame.time.set_timer(26, 1000)
    if key[pygame.K_DOWN]: speed[1] = 1
    herorect = herorect.move(speed)
    if herorect.left < 0 or herorect.right > width:
        speed[0] = 0
    if herorect.top < 0 or herorect.bottom > height:
        speed[1] = 0
    if collide(herorect):
        speed[1] = 0
    screen.fill(black)
    screen.blit(bg,(0, 0))
    screen.blit(hero, herorect)
    pygame.display.flip()