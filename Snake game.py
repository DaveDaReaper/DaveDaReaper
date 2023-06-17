# 1 Imports
import random
import pygame
from pygame.math import Vector2
import sys


# 5 sssss
class SNAKE:
    def __init__(self):
        self.head = None
        self.tail = None
        self.body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False

        # 9 Graphics for snake
        self.hu = pygame.image.load("Imports/head_up.png").convert_alpha()
        self.hd = pygame.image.load("Imports/head_down.png").convert_alpha()
        self.hr = pygame.image.load("Imports/head_right.png").convert_alpha()
        self.hl = pygame.image.load("Imports/head_left.png").convert_alpha()

        self.tu = pygame.image.load("Imports/tail_up.png").convert_alpha()
        self.td = pygame.image.load("Imports/tail_down.png").convert_alpha()
        self.tr = pygame.image.load("Imports/tail_right.png").convert_alpha()
        self.tl = pygame.image.load("Imports/tail_left.png").convert_alpha()

        self.body_v = pygame.image.load("Imports/body_vertical.png").convert_alpha()
        self.body_h = pygame.image.load("Imports/body_horizontal.png").convert_alpha()

        self.body_tr = pygame.image.load("Imports/body_tr.png").convert_alpha()
        self.body_tl = pygame.image.load("Imports/body_tl.png").convert_alpha()
        self.body_br = pygame.image.load("Imports/body_br.png").convert_alpha()
        self.body_bl = pygame.image.load("Imports/body_bl.png").convert_alpha()

        self.nom_sound = pygame.mixer.Sound("Imports/crunch.wav")

    # Blocky snake body
    # def draw_snake(self):
    #     for block in self.body:
    #         x_pos = int(block.x * cell_size)
    #         y_pos = int(block.y * cell_size)
    #         body_shape = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
    #         pygame.draw.rect(screen, (0, 0, 80), body_shape)

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            body_shape = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, body_shape)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, body_shape)

            else:
                prev_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                # Head & Tail
                if prev_block.x == next_block.x:
                    screen.blit(self.body_v, body_shape)
                elif prev_block.y == next_block.y:
                    screen.blit(self.body_h, body_shape)
                else:
                    # Turns
                    if prev_block.x == -1 and next_block.y == -1 or prev_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, body_shape)
                    elif prev_block.x == -1 and next_block.y == 1 or prev_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, body_shape)
                    elif prev_block.x == 1 and next_block.y == -1 or prev_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, body_shape)
                    elif prev_block.x == 1 and next_block.y == 1 or prev_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, body_shape)

    def update_head_graphics(self):
        head_pos = self.body[1] - self.body[0]
        if head_pos == Vector2(1, 0):
            self.head = self.hl
        elif head_pos == Vector2(-1, 0):
            self.head = self.hr
        elif head_pos == Vector2(0, 1):
            self.head = self.hu
        elif head_pos == Vector2(0, -1):
            self.head = self.hd

    def update_tail_graphics(self):
        tail_pos = self.body[-2] - self.body[-1]
        if tail_pos == Vector2(1, 0):
            self.tail = self.tl
        elif tail_pos == Vector2(-1, 0):
            self.tail = self.tr
        elif tail_pos == Vector2(0, 1):
            self.tail = self.tu
        elif tail_pos == Vector2(0, -1):
            self.tail = self.td

    def move_snake(self):
        if self.new_block is True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False

        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def nom(self):
        self.nom_sound.play()

    def reset(self):
        self.body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)]
        self.direction = Vector2(0, 0)


# 4 nom nom nom
class FRUIT:
    def __init__(self):
        self.x = None
        self.y = None
        self.pos = None
        self.randomise()

    # Creating fruit
    def draw_apple(self):
        # (fruit x, fruit y, x size, y size)
        apple_shape = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, apple_shape)
        # pygame.draw.rect(screen, (200, 50, 50), apple_shape)

    def randomise(self):
        self.x = random.randint(0, (cell_number - 1))
        self.y = random.randint(0, (cell_number - 1))
        self.pos = Vector2(self.x, self.y)


# 7 game system
class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.contact()
        self.check_fail()

    def draw(self):
        self.grass()
        self.snake.draw_snake()
        self.fruit.draw_apple()
        self.score()

    def contact(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomise()
            self.snake.add_block()
            self.snake.nom()
            print("nom")

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomise()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.gameover()
        if self.snake.body[0] in self.snake.body[1:]:
            self.gameover()

    def gameover(self):
        self.snake.reset()

    @staticmethod
    def grass():
        # Colours
        grass1 = (100, 160, 70)
        grass2 = (110, 170, 80)

        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_square = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass1, grass_square)
                    else:
                        grass_square = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass2, grass_square)

            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_square = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass1, grass_square)
                    else:
                        grass_square = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass2, grass_square)

    def score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (25, 25, 25))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)

        score_pos = score_surface.get_rect(center=(score_x, score_y))
        apple_pos = apple.get_rect(midright=(score_pos.right + 50, score_pos.centery))
        box_pos = pygame.Rect(apple_pos.left - 45, apple_pos.top - 3, apple_pos.width + apple_pos.width, apple_pos.height)


        screen.blit(score_surface, score_pos)
        screen.blit(smol_apple, apple_pos)
        pygame.draw.rect(screen, (25, 25, 25), box_pos, 2)


# 2 Screen
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

# 8 Import font and apple
apple = pygame.image.load("Imports/snake_apple.png").convert_alpha()
apple = pygame.transform.scale(apple, (40, 40))
smol_apple = pygame.transform.scale(apple, (30, 30))
game_font = pygame.font.Font("Imports/Cow-Mix.ttf", 25)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

# 3 What appears
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()

        # 6 Key inputs
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)

    screen.fill((0, 0, 0))
    main_game.draw()
    pygame.display.update()
    clock.tick(60)
