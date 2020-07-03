import sys
import pygame


from Snake import Snake
from FoodSpawner import FoodSpawner
from settings import SCREEN_SIZE, BLOCK_SIZE, FPS


CONTROLS = [
    pygame.K_RIGHT,
    pygame.K_LEFT,
    pygame.K_UP,
    pygame.K_DOWN,
    pygame.K_d,
    pygame.K_a,
    pygame.K_w,
    pygame.K_s
]


pygame.init()
fps = pygame.time.Clock()
pygame.display.set_caption('Snake')
window = pygame.display.set_mode(SCREEN_SIZE)

score = 0
snake = Snake()
isStarted = False
isOver = False
foodSpawner = FoodSpawner()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key != pygame.K_SPACE and event.key in CONTROLS:
                snake.changeDirTo(event.key)
            elif event.key == pygame.K_SPACE and not isStarted:
                score = 0
                snake = Snake()
                foodSpawner = FoodSpawner()
                isStarted = True
                isOver = False

    window.fill((225, 225, 225))

    if isStarted:
        foodPos = foodSpawner.spawnFood()

        if snake.move(foodPos):
            score += 1
            foodSpawner.setFoodOnScreen(False)

        for pos in snake.getBody():
            pygame.draw.rect(
                window,
                (0, 225, 0),
                [pos.x, pos.y, BLOCK_SIZE, BLOCK_SIZE]
            )

        pygame.draw.rect(
            window,
            (225, 0, 0),
            [foodPos.x, foodPos.y, BLOCK_SIZE, BLOCK_SIZE]
        )

        if snake.checkCollision():
            isStarted = False
            isOver = True



    else:
        font = pygame.font.Font(None, 36)

        if isOver:
            string = ["Вы проиграли.", "Счет: {}, чтобы начать заново нажмите ПРОБЕЛ".format(score)]
            text = font.render(string[0], 1, (0, 0, 0))
            window.blit(text, (int(SCREEN_SIZE[0] / 2.5), int(SCREEN_SIZE[1] / 2.2)))
            text = font.render(string[1], 1, (0, 0, 0))
            window.blit(text, (int(SCREEN_SIZE[0] / 5), int(SCREEN_SIZE[1] / 2)))
        else:
            string = "Нажмите ПРОБЕЛ для начала игры!"
            text = font.render(string, 1, (0, 0, 0))
            window.blit(text, (int(SCREEN_SIZE[0] / 5), int(SCREEN_SIZE[1] / 2.2)))

    pygame.display.flip()

    pygame.display.set_caption('Snake | Score: {}'.format(score))

    fps.tick(FPS)
