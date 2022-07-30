import pygame

BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

SNAKE_SPEED = 30
SNAKE_BLOCK = 10

# FONT_STYLE = pygame.font.SysFont(None, 50)


class Snake:
    def __init__(self, head_x, head_y):
        self.head_x = head_x
        self.head_y = head_y

    def move_head(self, x, y):
        self.head_x += x
        self.head_y += y


# def message(board, msg, color):
#     rendered_msg = FONT_STYLE.render(msg, True, color)
#     board.blit(rendered_msg, [DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2])


def main():
    pygame.init()
    board = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption('PySnake game by GGRS')

    snake = Snake(DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)
    clock = pygame.time.Clock()

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            print(event)  # prints out all the actions that take place on the screen
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.move_head(-SNAKE_BLOCK, 0)
                elif event.key == pygame.K_RIGHT:
                    snake.move_head(SNAKE_BLOCK, 0)
                elif event.key == pygame.K_UP:
                    snake.move_head(0, -SNAKE_BLOCK)
                elif event.key == pygame.K_DOWN:
                    snake.move_head(0, SNAKE_BLOCK)

            board.fill(WHITE)
            pygame.draw.rect(board, BLACK, [snake.head_x, snake.head_y, SNAKE_BLOCK, SNAKE_BLOCK])
            pygame.display.update()

            clock.tick(30)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
