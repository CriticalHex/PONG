import pygame
pygame.init()

screen = pygame.display.set_mode((700,500))

font = pygame.font.Font(None, 74)

pygame.display.set_caption("Pong")

StopGame = False
doExit = False

clock = pygame.time.Clock()

p1x = 20
p1y = 200
p2x = 660
p2y = 200
bx = 350
by = 250
b2x = 345
b2y = 245
b3x = 340
b3y = 240
bVx = 5
bVy = 5
p1Score = 0
p2Score = 0

def bx(ball):
    #do ball movement here with the input being which ball it is.
    print(p1x)

while not StopGame:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            StopGame = True
    
    #logic----------------------------------------------------------------

    #Cheat Code
    keys = pygame.key.get_pressed()
    if keys[pygame.K_t]:
        p1Score = 10

    #Player 1 Movement Limiter
    if p1y == 400:
        down = 0
    else:
        down = 5
    if p1y == 0:
        up = 0
    else:
        up = 5

    #Player 1 Up and Down
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        p1y-=up
    if keys[pygame.K_s]:
        p1y+=down

    #Player 2 Movement Limiter
    if p2y == 400:
        down = 0
    else:
        down = 5
    if p2y == 0:
        up = 0
    else:
        up = 5

    #Player 2 Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_i]:
        p2y-=up
    if keys[pygame.K_k]:
        p2y+=down
    
    #Move the Ball
    bx += bVx
    by += bVy

    #Ball Reflections
    if bx < 0 or bx + 20 > 700:
        bVx *= -1
    if by < 0 or by + 20 > 500:
        bVy *= -1
    if bx < p1x + 25 and by + 20 > p1y and by < p1y + 100:
        bVx *= -1
    if bx > p2x - 10 and by + 20 > p2y and by < p2y + 100:
        bVx *= -1

    #Add Score
    if bx < 0:
        p2Score += 1
    if bx > 680:
        p1Score += 1

    #AI
    p2y = by - 50

    #You Lose Sucka
    if p1Score == 10:
        StopGame = True
        screen.fill((0,0,0))
    if p2Score == 10:
        StopGame = True
        
        
    #render--------------------------------------------------------------------------------------------

    #Make Screen Black
    screen.fill((0,0,0))

    #Write the Scores
    text = font.render(str(p1Score), 1, (255 ,255 ,255))
    screen.blit(text, (250,10))
    text = font.render(str(p2Score), 1, (255 ,255 ,255))
    screen.blit(text, (450,10))

    #Draw Everything
    pygame.draw.line(screen, (255,255,255), [349, 0], [349, 500], 1) #Middle Line

    pygame.draw.rect(screen, (255,255,255), (p1x, p1y, 20, 100), 1) #Player 1 Paddle

    pygame.draw.rect(screen, (255,255,255), (p2x, p2y, 20, 100), 1) #Player 2 Paddle

    pygame.draw.rect(screen, (255,255,255), (bx, by, 5, 5), 5) #Ball

    pygame.draw.rect(screen, (240,240,240), (bx, by, 5, 5), 5) #Ball Shadow

    pygame.draw.rect(screen, (200,200,200), (bx, by, 5, 5), 5) #Ball Super Shadow

    pygame.display.flip()
while not doExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
    screen.fill((0,0,0))
    if p1Score == 10:
        text = font.render(str("Player 1 Wins!"), 1, (255 ,255 ,255))
        screen.blit(text, (170,200))
    if p2Score == 10:
        text = font.render(str("Player 2 Wins!"), 1, (255 ,255 ,255))
        screen.blit(text, (170,200))
    if p1Score < 10 and p2Score < 10:
        text = font.render(str("You Quit!"), 1, (255 ,255 ,255))
        screen.blit(text, (225,200))
    pygame.display.flip()

pygame.quit()
