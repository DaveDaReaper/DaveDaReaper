# 1. Imports
import sys
import pygame


# 2. General setup
pygame.init()
clock = pygame.time.Clock()
game_font = pygame.font.Font("Cow-Mix.ttf", 100)
light_grey = (215, 215, 215)
x_speed, y_speed = (5, 5)
score_left, score_right = 0, 0


# 3. Window setup
screen_width, screen_height = 1280, 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")


# 4. Creating the shapes
pingpong = pygame.Rect(screen_width / 2, screen_height / 2 - 15, 30, 30)
player1 = pygame.Rect(10, screen_height / 2 - 70, 10, 140)
player2 = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
goal_left = pygame.Rect(0, 0, 10, screen_height)
goal_right = pygame.Rect(screen_width - 10, 0, 10, screen_height)
box = pygame.Rect(0, 0, screen_width, screen_height)


class MAIN:
    def __init__(self):
        return

    # 7. Drawing
    @staticmethod
    def draw():
        global pingpong
        pygame.draw.ellipse(screen, light_grey, pingpong)
        pygame.draw.rect(screen, light_grey, player1)
        pygame.draw.rect(screen, light_grey, player2)
        pygame.draw.rect(screen, (120, 20, 20), goal_left)
        pygame.draw.rect(screen, (120, 20, 20), goal_right)
        pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))
        pygame.draw.rect(screen, light_grey, box, 5)

    @staticmethod
    def score_boxes():
        global score_left, score_right
        score_r = str(score_right)
        score_l = str(score_left)
        score_r_surface = game_font.render(score_r, True, light_grey)
        score_l_surface = game_font.render(score_l, True, light_grey)

        score_r_pos = score_r_surface.get_rect(center=(screen_width * 3 / 4, 100))
        score_l_pos = score_l_surface.get_rect(center=(screen_width * 1 / 4, 100))

        screen.blit(score_r_surface, score_r_pos)
        screen.blit(score_l_surface, score_l_pos)

    # 6. Ball
    @staticmethod
    def collisions():
        global x_speed, y_speed, score_right, score_left
        pygame.draw.ellipse(screen, light_grey, pingpong)
        pingpong.x += x_speed
        pingpong.y += y_speed

        if pingpong.right >= screen_width - 5 or pingpong.left <= 5:
            x_speed *= -1
        if pingpong.top >= screen_height - 30 or pingpong.bottom <= 30:
            y_speed *= -1

        if pingpong.colliderect(player1) or pingpong.colliderect(player2):
            x_speed *= -1

        if pingpong.colliderect(goal_left):
            score_right += 1
        if pingpong.colliderect(goal_right):
            score_left += 1

    # Left Player
    @staticmethod
    def player1_movement():
        global player1
        player_speed = 6
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player1.top -= player_speed
            if event.key == pygame.K_DOWN:
                player1.top += player_speed

        if player1.top <= 5:
            player1.top = 5
        if player1.bottom >= screen_height - 5:
            player1.bottom = screen_height - 5

    # Right Player
    @staticmethod
    def player2_movement():
        player_speed = 6

        # uncomment this half for single player
        if player2.top < pingpong.y:
            player2.top += player_speed
        if player2.bottom > pingpong.x:
            player2.bottom -= player_speed

        if player2.top <= 5:
            player2.top = 5
        if player2.bottom >= screen_height - 5:
            player2.bottom = screen_height - 5

        # uncomment this half for 2 player
        # PageUp & PageDown due to alphabet keys not working
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_PAGEUP:
        #         player2.top -= player_speed
        #     if event.key == pygame.K_PAGEDOWN:
        #         player2.top += player_speed
        #
        # if player2.top <= 5:
        #     player2.top = 5
        # if player2.bottom >= screen_height - 5:
        #     player2.bottom = screen_height - 5


main = MAIN()

# 5. Event
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(0)
    main.draw()
    main.collisions()
    main.score_boxes()
    main.player1_movement()
    main.player2_movement()

    # Updating
    pygame.display.flip()
    clock.tick(60)
