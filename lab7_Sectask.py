import pygame
from pygame.locals import *

pygame.init()

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 200
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Music Player')

font = pygame.font.SysFont(None, 24)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.mixer.init()

playlist = ['/Users/ablik/Desktop/PP2/sounds/Mnogotocie_Semit_v_duse_toska.mp3', '/Users/ablik/Desktop/PP2/sounds/Sergey_Shnurov_-_Mobilnik_(ringon.site).mp3']
current_track = 0
playing = False

def draw_text(text, font, surface, x, y, color):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def play_music(track):
    pygame.mixer.music.load(track)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_music(playlist[current_track])

def previous_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_music(playlist[current_track])

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                if playing:
                    stop_music()
                    playing = False
                else:
                    play_music(playlist[current_track])
                    playing = True
            elif event.key == K_n:
                next_track()
            elif event.key == K_p:
                previous_track()

    window_surface.fill(WHITE)

    status_text = "Playing" if playing else "Paused"
    draw_text(status_text, font, window_surface, 10, 10, BLACK)
    draw_text("Press SPACE to play/pause", font, window_surface, 10, 40, BLACK)
    draw_text("Press N for next track", font, window_surface, 10, 70, BLACK)
    draw_text("Press P for previous track", font, window_surface, 10, 100, BLACK)

    pygame.display.update()