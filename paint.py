import pygame
import random

pygame.init()

width, height, fps = 1000, 800, 60
clock = pygame.time.Clock()

points = []
lastPosition = (0,0)
w = 3

display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Paint app")

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
colorMode = blue

display.fill(white)

open_text = pygame.font.SysFont('comicsansms', 50)
font = pygame.font.SysFont('comicsansms', 30)

imageRect = pygame.image.load("paint/rectangle.png")
imageRect = pygame.transform.scale(imageRect, (50,50))
buttonRect = imageRect.get_rect(center = (50,50))

imageCircle = pygame.image.load("paint/circle.png")
imageCircle = pygame.transform.scale(imageCircle, (50,50))
buttonCircle = imageCircle.get_rect(center = (150, 50))

imageEraser = pygame.image.load("paint/eraser.png")
imageEraser = pygame.transform.scale(imageEraser, (50,50))
buttonEraser = imageEraser.get_rect(center = (350,50))

imageRed = pygame.image.load("paint/red.png")
imageRed = pygame.transform.scale(imageRed, (50,50))
buttonRed = imageRed.get_rect(center = (450, 50))

imageGreen = pygame.image.load("paint/green.png")
imageGreen = pygame.transform.scale(imageGreen, (50,50))
buttonGreen = imageGreen.get_rect(center = (550, 50))

imageBlue = pygame.image.load("paint/blue.png")
imageBlue = pygame.transform.scale(imageBlue, (50,50))
buttonBlue = imageBlue.get_rect(center = (650, 50))

imagePencil = pygame.image.load("paint/pencil.png")
imagePencil = pygame.transform.scale(imagePencil, (50,50))
buttonPencil = imagePencil.get_rect(center = (750, 50))

imageSquare = pygame.image.load("paint/square.png")
imageSquare = pygame.transform.scale(imageSquare, (50,50))
buttonSquare = imageSquare.get_rect(center = (250, 50))

imageRightTriangle = pygame.image.load("paint/right_triangle.png")
imageRightTriangle = pygame.transform.scale(imageRightTriangle, (50,50))
buttonRightTriangle = imageRightTriangle.get_rect(center = (50, 150))

imageTriangle = pygame.image.load("paint/triangle.png")
imageTriangle = pygame.transform.scale(imageTriangle, (50,50))
buttonTriangle = imageTriangle.get_rect(center = (150, 150))

imageRhombus = pygame.image.load("paint/rhombus.png")
imageRhombus = pygame.transform.scale(imageRhombus, (50,50))
buttonRhombus = imageRhombus.get_rect(center = (250, 150))

line = False
circle = False
rect = False
eraser = False
square = False
right_triangle = False
triangle = False
rhombus = False
drawing = False
removing = False

def drawLine(display, start, end, width, colorMode):

    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(display, colorMode, (x,y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(display, colorMode, (x,y), width)

def drawCircle(display, start, end, size, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    width = abs(x1 - x2)
    height = abs(y1 - y2)

    if x1 <= x2:
        if y1 < y2:
            pygame.draw.ellipse(display, color, (x1, y1, width, height), size)
        else:
            pygame.draw.ellipse(display, color, (x1, y2, width, height), size)
    else:
        if y1 < y2:
            pygame.draw.ellipse(display, color, (x2, y1, width, height), size)
        else:
            pygame.draw.ellipse(display, color, (x2, y2, width, height), size)

def drawRect(screen, start, end, size, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    width = abs(x1-x2)
    height = abs(y1-y2)

    if x1 <= x2:
        if y1 < y2:
            pygame.draw.rect(display, color, (x1, y1, width, height), size)
        else:
            pygame.draw.rect(display, color, (x1, y2, width, height), size)
    else:
        if y1< y2:
            pygame.draw.rect(display, color, (x2, y1, width, height), size)
        else:
            pygame.draw.rect(display, color, (x2, y2, width, height), size)

def drawSquare(display, start, end, size, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    width = abs(x1 - x2)
    height = abs(y1 - y2)

    if x1 <= x2:
        if y1 < y2:
            pygame.draw.rect(display, color, (x1, y1, width, width), size)
        else:
            pygame.draw.rect(display, color, (x1, y2, width, width), size)
    else:
        if y1 < y2:
            pygame.draw.rect(display, color, (x2, y1, width, width), size)
        else:
            pygame.draw.rect(display, color, (x2, y2, width, width), size)

def drawRightTriangle(display, start, end, size, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    width = abs(x1 - x2)
    height = abs(y1 - y2)

    pygame.draw.polygon(display, color, [(x1, y1), (x1, y2), (x2, y2)], size)

def drawEquilateralTriangle(display, start, end, size, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    width = abs(x1 - x2)
    height = abs(y1 - y2)

    x3 = x1 + (x2 - x1) / 2
    y3 = y1 - (y2 - y1) * 3**0.5 / 2

    pygame.draw.polygon(display, color, [(x1, y1), (x2, y2), (x3, y3)], size)

    pygame.draw.polygon(display, color, [(x1, y1), (x2, y2), (x3, y3)], size)

    pygame.draw.polygon(display, color, [(x1, y1), (x2, y2), (x3, y3)], size)

def drawRhombus(display, start, end, size, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    width = abs(x1 - x2)
    height = abs(y1 - y2)

    pygame.draw.polygon(display, color, [(x1, y1 + height // 2), (x1 + width // 2, y1 + height), (x2, y1 + height // 2), (x1 + width // 2, y1)], size)


while True:
    pygame.draw.rect(display, (128, 128, 128), buttonRect)
    display.blit(imageRect, buttonRect.topleft)

    pygame.draw.rect(display, (128, 128, 128), buttonCircle)
    display.blit(imageCircle, buttonCircle.topleft)

    pygame.draw.rect(display, (128, 128, 128), buttonEraser)
    display.blit(imageEraser, buttonEraser.topleft)

    pygame.draw.rect(display, (128, 128, 128), buttonRed)
    display.blit(imageRed, buttonRed.topleft)

    pygame.draw.rect(display, (128, 128, 128), buttonGreen)
    display.blit(imageGreen, buttonGreen.topleft)

    pygame.draw.rect(display, (128, 128, 128), buttonBlue)
    display.blit(imageBlue, buttonBlue.topleft)

    pygame.draw.rect(display, (128, 128, 128), buttonPencil)
    display.blit(imagePencil, buttonPencil.topleft)

    pygame.draw.rect(display, (128, 128, 128), buttonSquare)
    display.blit(imageSquare, buttonSquare.topleft)

    pygame.draw.rect(display, (128, 128, 128), buttonRightTriangle)
    display.blit(imageRightTriangle, buttonRightTriangle.topleft)

    pygame.draw.rect(display, (128, 128, 128), buttonTriangle)
    display.blit(imageTriangle, buttonTriangle.topleft)

    pygame.draw.rect(display, (128, 128, 128), buttonRhombus)
    display.blit(imageRhombus, buttonRhombus.topleft)

    pygame.display.flip()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_r]:
        color_mode = red
    elif pressed_keys[pygame.K_g]:
        color_mode = green
    elif pressed_keys[pygame.K_b]:
        color_mode = blue

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            exit()

        if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
            if buttonRect.collidepoint(event.pos):
                line = False
                rect = True
                circle = False
                eraser = False
                square = False
                right_triangle = False
                triangle = False
                rhombus = False
            if buttonCircle.collidepoint(event.pos):
                line = False
                rect = False
                circle = True
                eraser = False
                square = False
                right_triangle = False
                triangle = False
                rhombus = False
            if buttonEraser.collidepoint(event.pos):
                line = False
                rect = False
                circle = False
                eraser = True
                square = False
                right_triangle = False
                triangle = False
                rhombus = False
            if buttonPencil.collidepoint(event.pos):
                line = True
                rect = False
                circle = False
                eraser = False
                square = False
                right_triangle = False
                triangle = False
                rhombus = False
            if buttonSquare.collidepoint(event.pos):
                line = False
                rect = False
                circle = False
                eraser = False
                square = True
                right_triangle = False
                triangle = False
                rhombus = False
            if buttonRightTriangle.collidepoint(event.pos):
                line = False
                rect = False
                circle = False
                eraser = False
                square = False
                right_triangle = True
                triangle = False
                rhombus = False
            if buttonTriangle.collidepoint(event.pos):
                line = False
                rect = False
                circle = False
                eraser = False
                square = False
                right_triangle = False
                triangle = True
                rhombus = False
            if buttonRhombus.collidepoint(event.pos):
                line = False
                rect = False
                circle = False
                eraser = False
                square = False
                right_triangle = False
                triangle = False
                rhombus = True
            if buttonBlue.collidepoint(event.pos):
                colorMode = blue
            if buttonGreen.collidepoint(event.pos):
                colorMode = green
            if buttonRed.collidepoint(event.pos):
                colorMode = red

        if line:
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                lastPosition = pos
                pygame.draw.circle(display, colorMode, pos, w)
            
            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False
            
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    drawLine(display, lastPosition, pos, w, colorMode)
                lastPosition = pos

        if rect:
            if event.type == pygame.MOUSEBUTTONDOWN:
                lastPosition = pos
            if event.type == pygame.MOUSEBUTTONUP:
                drawRect(display, lastPosition, pos, w, colorMode)

        if circle:
            if event.type == pygame.MOUSEBUTTONDOWN:
                lastPosition = pos
            if event.type == pygame.MOUSEBUTTONUP:
                drawCircle(display, lastPosition, pos, w, colorMode)

        if eraser:
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = pos
                erasing = True
                pygame.draw.rect(display, white, (x, y, 50, 50))
            if event.type == pygame.MOUSEMOTION:
                if erasing:
                    pygame.draw.rect(display, white, (pos[0], pos[1], 50, 50))
            if event.type == pygame.MOUSEBUTTONUP:
                erasing = False

        if square:
            if event.type == pygame.MOUSEBUTTONDOWN:
                lastPosition = pos
            if event.type == pygame.MOUSEBUTTONUP:
                drawSquare(display, lastPosition, pos, w, colorMode)

        if right_triangle:
            if event.type == pygame.MOUSEBUTTONDOWN:
                lastPosition = pos
            if event.type == pygame.MOUSEBUTTONUP:
                drawRightTriangle(display, lastPosition, pos, w, colorMode)

        if triangle:
            if event.type == pygame.MOUSEBUTTONDOWN:
                lastPosition = pos
            if event.type == pygame.MOUSEBUTTONUP:
                drawEquilateralTriangle(display, lastPosition, pos, w, colorMode)

        if rhombus:
            if event.type == pygame.MOUSEBUTTONDOWN:
                lastPosition = pos
            if event.type == pygame.MOUSEBUTTONUP:
                drawRhombus(display, lastPosition, pos, w, colorMode)

    pygame.display.update()
    pygame.display.flip()
    clock.tick(65)
