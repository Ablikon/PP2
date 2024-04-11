import pygame 
import datetime 
 
pygame.init() 
screen = pygame.display.set_mode((500, 400)) 
running = True 
 
clock = pygame.time.Clock() 
main_clock = pygame.image.load((r"C:\Users\zhylk\OneDrive\Рабочий стол\PP2\mainclock.png")) 
minute_hand = pygame.image.load((r"C:\Users\zhylk\OneDrive\Рабочий стол\PP2\rightarm.png")) 
second_hand = pygame.image.load((r"C:\Users\zhylk\OneDrive\Рабочий стол\PP2\leftarm.png")) 
main_clock = pygame.transform.scale(main_clock, (500, 400)) 
minute_hand = pygame.transform.scale(minute_hand, (500, 450)) 
second_hand = pygame.transform.scale(second_hand, (50, 480)) 
 
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
 
    screen.fill((255, 255, 255)) 
    current_time = datetime.datetime.now() 
 
    minute_angle = current_time.minute * 6 * -1 
    second_angle = current_time.second * 6 * -1 
 
    rotated_minute_hand = pygame.transform.rotate(minute_hand, minute_angle) 
    rotated_second_hand = pygame.transform.rotate(second_hand, second_angle) 
 
    screen.blit(main_clock, main_clock.get_rect(center=screen.get_rect().center)) 
    screen.blit(rotated_minute_hand, rotated_minute_hand.get_rect(center=screen.get_rect().center)) 
    screen.blit(rotated_second_hand, rotated_second_hand.get_rect(center=screen.get_rect().center)) 
    pygame.display.flip() 
    clock.tick(50) 
 
pygame.quit()




import pygame
import sys
from datetime import datetime
import math

RES= WIDTH, HEIGHT = 1200, 800
H_WIDTH, H_HEIGHT = WIDTH//2, HEIGHT//2
RADIUS= H_HEIGHT-50

pygame.init()
surface=pygame.display.set_mode(RES)
clock=pygame.time.Clock()
font=pygame.font.SysFont('Verdana',60)

clock60= dict(zip(range(60), range(0,360,6)))

def get_clock_pos(clock_dict, clock_hand):
    x = H_WIDTH+RADIUS*math.cos(math.radians(clock_dict[clock_hand])-math.pi/2)
    y = H_WIDTH+RADIUS*math.sin(math.radians(clock_dict[clock_hand])-math.pi/2)
    return x,y

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    surface.fill(pygame.Color('black'))
    t=datetime.now()
    minute,second=t.minute, t.sec
    time_render= font.render(f'{t:%M:%S}', True, pygame.Color('green'), pygame.Color('Yellow'))
    surface.blit(time_render, (120,150))

    pygame.display.flip()
    clock.tick(20)
