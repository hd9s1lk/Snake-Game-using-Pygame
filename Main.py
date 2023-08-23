import pygame
from pygame.locals import *
from consts import *
import random

pygame.init()


screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake Game by Henrique!")

snake_pos = [[int(screen_width / 2), int(screen_height/2)]]
snake_pos.append([int(screen_width / 2), int(screen_height/2 ) + cell_size])
snake_pos.append([int(screen_width / 2), int(screen_height/2 ) + cell_size *2])
snake_pos.append([int(screen_width / 2), int(screen_height/2 ) + cell_size *3])
snake_pos.append([int(screen_width / 2), int(screen_height/2 ) + cell_size *4])

font = pygame.font.SysFont(None,40)
again_rect = Rect(screen_width // 2 -80 , screen_height // 2, 160, 50)

def draw_screen():
    screen.fill(bg)

def draw_score():
    score_text = "Score: " + str(score)
    score_img = font.render(score_text, True, blue)
    screen.blit(score_img, (0,0))

def check_gameover(game_over):
    head_count = 0
    for segment in snake_pos:
        if snake_pos[0] == segment and head_count >0:
            game_over = True
        head_count += 1

    if snake_pos[0][0] < 0 or snake_pos[0][0] > screen_width or snake_pos[0][1] < 0 or snake_pos[0][1] > screen_height:
        game_over = True

    return game_over

def draw_gameover():
    game_over_text = "Game Over"
    game_over_text_img = font.render(game_over_text, True, blue)
    pygame.draw.rect(screen, red, (screen_width//2 -80, screen_height//2 - 60, 160, 50))
    screen.blit(game_over_text_img, (screen_width // 2-80, screen_height// 2- 50))

    again_text = "Play Again?"
    again_text_img = font.render(again_text, True, blue)
    pygame.draw.rect(screen, red, again_rect)
    screen.blit(again_text_img, (screen_width// 2 -80, screen_height // 2  +10))


while running:

    draw_screen()
    draw_score()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 3:
                direction = 1
            if event.key == pygame.K_RIGHT and direction != 4:
                direction = 2
            if event.key == pygame.K_DOWN and direction != 1:
                direction = 3
            if event.key == pygame.K_LEFT and direction != 2:
                direction = 4

    if new_food == True:
        new_food = False
        food[0] = cell_size * random.randint(0, (screen_width / cell_size) -1)
        food[1] = cell_size * random.randint(0, (screen_height / cell_size) -1)

    pygame.draw.rect(screen, food_colour, (food[0], food[1], cell_size,cell_size))

    if snake_pos[0] == food:
        new_food = True
        new_piece = list(snake_pos[-1])
        if direction == 1:
            new_piece[1] += cell_size
        if direction == 3:
            new_piece[1] -= cell_size
        if direction == 2:
            new_piece[0] -= cell_size
        if direction == 4:
            new_piece[0] += cell_size

        snake_pos.append(new_piece)
        score += 1

    if game_over == False:
        if update_snake > 99:
            update_snake = 0
            snake_pos = snake_pos[-1:] + snake_pos[:-1]

            if direction == 1:
                snake_pos[0][0] = snake_pos[1][0]
                snake_pos[0][1] = snake_pos[1][1] - cell_size
            if direction == 3:
                snake_pos[0][0] = snake_pos[1][0]
                snake_pos[0][1] = snake_pos[1][1] + cell_size
            if direction == 2:
                snake_pos[0][1] = snake_pos[1][1]
                snake_pos[0][0] = snake_pos[1][0] + cell_size
            if direction == 4:
                snake_pos[0][1] = snake_pos[1][1]
                snake_pos[0][0] = snake_pos[1][0] - cell_size

            game_over = check_gameover(game_over)
    if game_over == True:
        draw_gameover()
        if event.type  == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type  == pygame.MOUSEBUTTONDOWN and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                game_over = False
                direction = 1 #1 cima , 2 direira, 3 baixo, 4 esquerda
                update_snake = 0
                food = [0,0]
                new_food = True
                new_piece = [0,0]
                score = 0

                snake_pos = [[int(screen_width / 2), int(screen_height/2)]]
                snake_pos.append([int(screen_width / 2), int(screen_height/2 ) + cell_size])
                snake_pos.append([int(screen_width / 2), int(screen_height/2 ) + cell_size *2])
                snake_pos.append([int(screen_width / 2), int(screen_height/2 ) + cell_size *3])
                snake_pos.append([int(screen_width / 2), int(screen_height/2 ) + cell_size *4])

    head = 1
    for x in snake_pos:
        if head == 0:
            pygame.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
            pygame.draw.rect(screen, body_inner, (x[0] + 1, x[1] + 1, cell_size -2, cell_size -2))
        if head == 1:
            pygame.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
            pygame.draw.rect(screen, red, (x[0] + 1, x[1] + 1, cell_size -2, cell_size -2))
            head = 0


    pygame.display.update()

    update_snake += 1


pygame.quit()