import pygame
pygame.init()

screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Squarey")

done = False
og_color = True

x= 30
y= 30
x2= 100
y2 =30

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            og_color = not og_color


    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y-=3
    if pressed[pygame.K_DOWN]: y+=3
    if pressed[pygame.K_RIGHT]: x+=3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_w]: y2 -= 3
    if pressed[pygame.K_s]: y2 += 3
    if pressed[pygame.K_a]: x2 -= 3
    if pressed[pygame.K_d]: x2 += 3



    screen.fill((0,0,0))
    if og_color: color= (255, 0, 0)
    else: color= (114, 67, 100)
    if og_color: color2= (89, 255, 56)
    else: color2 = (254,130,140)
    rect1 = pygame.draw.rect(screen, color, pygame.Rect(x,y,60,60))
    rect2 = pygame.draw.rect(screen, color2, pygame.Rect(x2, y2, 60, 60))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
  