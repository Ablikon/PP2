import pygame
import random
import time

pygame.init()

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLOCK_SIZE = 20

INITIAL_SPEED = 10
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

FONT_STYLE = 'freesansbold.ttf'
FONT_SIZE = 30

clock = pygame.time.Clock()

font = pygame.font.Font(FONT_STYLE, FONT_SIZE)
def display_text(text, color, x, y):
    rendered_text = font.render(text, True, color)
    gameDisplay.blit(rendered_text, (x, y))

def draw_snake(snake_list):
    for segment in snake_list:
        pygame.draw.rect(gameDisplay, GREEN, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])

def generate_food():
    weights = [YELLOW] * 3 + [RED] * 7 
    food_color = random.choice(weights)
    food_x = random.randrange(0, DISPLAY_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    food_y = random.randrange(0, DISPLAY_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
    return food_x, food_y, food_color

def display_stats(score, level):
    display_text(f"Score: {score}", (255, 255, 255), 10, 10)
    display_text(f"Level: {level}", (255, 255, 255), 10, 40)

def game_over():
    gameDisplay.fill(RED)
    display_text("Game Over!", BLACK, DISPLAY_WIDTH // 2 - 100, DISPLAY_HEIGHT // 2 - 50)
    display_text("Press Q to Quit or C to Play Again", BLACK, DISPLAY_WIDTH // 2 - 200, DISPLAY_HEIGHT // 2 + 20)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_c:
                    game_loop()

def check_border_collision(x, y):
    if x >= DISPLAY_WIDTH or x < 0 or y >= DISPLAY_HEIGHT or y < 0:
        return True
    return False

def check_self_collision(new_head, snake_list):
    for segment in snake_list[:-1]:
        if new_head == segment:
            return True
    return False

def game_loop():
    game_over_flag = False
    game_exit = False
    score = 0
    level = 1
    speed = INITIAL_SPEED

    snake_list = []
    snake_length = 1
    snake_x = DISPLAY_WIDTH / 2
    snake_y = DISPLAY_HEIGHT / 2
    snake_x_change = 0
    snake_y_change = 0

    food_x, food_y, food_color = generate_food()
    food_timer = time.time() + 10 

    while not game_exit:
        while game_over_flag:
            game_over()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -BLOCK_SIZE
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = BLOCK_SIZE
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -BLOCK_SIZE
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = BLOCK_SIZE
                    snake_x_change = 0

        snake_x += snake_x_change
        snake_y += snake_y_change
        if check_border_collision(snake_x, snake_y) or check_self_collision([snake_x, snake_y], snake_list):
            game_over_flag = True

        if snake_x == food_x and snake_y == food_y:
            score += 1
            snake_length += 1
            food_x, food_y, food_color = generate_food()
            food_timer = time.time() + 10 

            if score % 3 == 0:
                level += 1
                speed += 2 

        if time.time() > food_timer:
            food_x, food_y, food_color = generate_food()
            food_timer = time.time() + 10

        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        gameDisplay.fill(BLACK)
        pygame.draw.rect(gameDisplay, food_color, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        draw_snake(snake_list)
        display_stats(score, level)
        pygame.display.update()

        clock.tick(speed)

    pygame.quit()
    quit()

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Snake Game')

game_loop()