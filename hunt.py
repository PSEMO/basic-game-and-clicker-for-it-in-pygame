import pygame
import random
import math
from sys import exit

framerate = 150
width = 1280
height = 720

pygame.init()

clock = pygame.time.Clock()

#region image loading
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Vodka hunt")


bg = pygame.image.load('bg.png')
bg_rect = bg.get_rect()
bg_rect.center = (width / 2, height / 2)

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

ImgBottle = pygame.image.load('bottle.png')
#endregion

MouseClicked = False
GameState = 0
point = 0
MaxPoint = 0
slowestBottle = 25
Bottles = []

#---------------------------------
def degree_to_position(degree):
    """ Convert degree to radian """
    radian = degree * math.pi / 180
    # Calculate x and y coordinates
    x = math.cos (radian)
    y = math.sin (radian)
    # Return coordinates as a tuple
    return (x, y)
def Similarity(n1, n2):
    """ Calculates a similarity score between 2 numbers """
    if n1 + n2 == 0:
        return 1
    else:
        return 1 - abs(n1 - n2) / (n1 + n2)
def draw_text(surface, text, size, color, x, y, relative):
    font = pygame.font.Font(pygame.font.get_default_font(), size)
    text_surf = font.render(str(text), True, color)
    text_rect = text_surf.get_rect()

    if(relative == 'center'):
        text_rect.center = (x, y)
    
    surface.blit(text_surf, text_rect)
def disBetweenPoints(P1, P2):
    dis = (P1[1] - P2[1])**2 + (P1[0] - P2[0])**2
    return dis
def changePoint(_input):
    global point
    global MaxPoint
    point += _input
    if(point > MaxPoint):
        MaxPoint = point
    elif(point < 0):
        global GameState
        GameState = 2
        point = 0
        global Bottles
        for bottle in Bottles:
            Bottle.randomizeBottle(bottle)
def CreateBottles():
    for i in range(20):
        temp = Bottle()
        Bottles.append(temp)
class Bottle:

    def __init__(self):
        # Initialize the attributes of the Bottle
        self.x = 0 # The x coordinate
        self.y = 0 # The y coordinate
        self.speedY = 0 # The falling speed
        self.img = pygame.transform.scale(pygame.image.load('bottle.png'), (ImgBottle.get_width() / 1, ImgBottle.get_height() / 1))
        self.rect = self.img.get_rect()
        Bottle.randomizeBottle(self)

    def update(self, dt):
        # Update the position of the Bottle
        self.y += self.speedY * dt # Move down by the speed
        # Draw self
        self.rect.center = (self.x, self.y)
        screen.blit(self.img, self.rect)
        # If the Bottle reaches the bottom of the screen, reset its position
        if self.y - (ImgBottle.get_height() / 2) > height:
            Bottle.randomizeBottle(self)
            changePoint(-10)
        
    def randomizeBottle(obj):
        obj.x = random.randint(50, width - 50) # Random x coordinate
        obj.y = random.randint(-height, 0) # Random y coordinate
        obj.speedY = random.randint(slowestBottle, 150) # Random speed
#---------------------------------
        
CreateBottles()

#Update()
while 1:

    #count the time frame took and assign it to dt
    _dt = clock.tick(framerate)
    dt = _dt / 1000
    #------------

    #resets screen
    screen.fill((255, 0, 0))
    #------------

    #detect events including inputs
    MousePos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            MouseClicked = True
            for CurrentBottle in Bottles:
                _x, _y = event.pos
                if CurrentBottle.rect.collidepoint(_x, _y):
                    changePoint(1)
                    CurrentBottle.randomizeBottle()

        elif event.type == pygame.MOUSEBUTTONUP:
            MouseClicked = False
    #------------

    if GameState == 0:
        screen.fill((0, 0, 0))

        draw_text(screen, "Press enter key to start",
                  40, (255, 255, 255), width / 2, height / 2, "center")
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                GameState = 1

    elif GameState == 1:
        screen.blit(bg, bg_rect)
        
        for bottle in Bottles:
            bottle.update(dt)
            
        draw_text(screen, str(point) + "(" + str(MaxPoint) + ")",
                  40, (255, 255, 255), width / 2, 40, "center")

    elif GameState == 2:
        screen.fill((0, 0, 0))

        draw_text(screen, "Press enter key to restart",
                  40, (255, 255, 255), width / 2, (height / 2) - 40, "center")
        draw_text(screen, "Your score: " + str(MaxPoint),
                  40, (255, 255, 255), width / 2, (height / 2) + 40, "center")
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                GameState = 1
                MaxPoint = 0
        
    pygame.display.flip()