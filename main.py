import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basit Pong Oyunu")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (50, 150, 255)
DARK_BLUE = (20, 60, 120)

FPS = 60
clock = pygame.time.Clock()

PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
PADDLE_SPEED = 6

BALL_RADIUS = 10
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

SCORE_FONT = pygame.font.SysFont("comicsans", 40)

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = PADDLE_SPEED

    def draw(self):
        pygame.draw.rect(SCREEN, LIGHT_BLUE, self.rect)

    def move(self, up=True):
        if up:
            self.rect.y -= self.speed
            if self.rect.top < 0:
                self.rect.top = 0
        else:
            self.rect.y += self.speed
            if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = BALL_RADIUS
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def draw(self):
        pygame.draw.circle(SCREEN, WHITE, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
            self.speed_y *= -1

    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed_x *= -1
        self.speed_y *= -1

def draw_center_line():
    for i in range(10, HEIGHT, 40):
        pygame.draw.rect(SCREEN, WHITE, (WIDTH//2 - 5, i, 10, 20))

def draw_score(player1_score, player2_score):
    score1 = SCORE_FONT.render(str(player1_score), True, WHITE)
    score2 = SCORE_FONT.render(str(player2_score), True, WHITE)
    SCREEN.blit(score1, (WIDTH//4, 20))
    SCREEN.blit(score2, (WIDTH*3//4, 20))

def main():
    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2)
    ball = Ball(WIDTH // 2, HEIGHT // 2)

    player1_score = 0
    player2_score = 0

    running = True
    while running:
        clock.tick(FPS)
        SCREEN.fill(DARK_BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            left_paddle.move(up=True)
        if keys[pygame.K_s]:
            left_paddle.move(up=False)
        if keys[pygame.K_UP]:
            right_paddle.move(up=True)
        if keys[pygame.K_DOWN]:
            right_paddle.move(up=False)

        ball.move()

        if ball.x - ball.radius <= left_paddle.rect.right and \
           left_paddle.rect.top < ball.y < left_paddle.rect.bottom:
            ball.speed_x *= -1
        if ball.x + ball.radius >= right_paddle.rect.left and \
           right_paddle.rect.top < ball.y < right_paddle.rect.bottom:
            ball.speed_x *= -1

        if ball.x < 0:
            player2_score += 1
            ball.reset()
        if ball.x > WIDTH:
            player1_score += 1
            ball.reset()
        
        draw_center_line()
        left_paddle.draw()
        right_paddle.draw()
        ball.draw()
        draw_score(player1_score, player2_score)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
