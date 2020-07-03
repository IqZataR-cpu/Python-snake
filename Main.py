import sys
import pygame


from Snake import Snake
from FoodSpawner import FoodSpawner
from settings import SCREEN_SIZE, BLOCK_SIZE, FPS


def gameOver():
    pygame.quit()
    sys.exit()


fps = pygame.time.Clock()
pygame.display.set_caption('Snake')
window = pygame.display.set_mode(SCREEN_SIZE)

score = 0
snake = Snake()
foodSpawner = FoodSpawner()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver()
        elif event.type == pygame.KEYDOWN:
            snake.changeDirTo(event.key)

    foodPos = foodSpawner.spawnFood()

    if snake.move(foodPos):
        score += 1
        foodSpawner.setFoodOnScreen(False)

    window.fill((225, 225, 225))

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
        gameOver()

    pygame.display.set_caption('Snake | Score: {}'.format(score))
    pygame.display.flip()

    fps.tick(FPS)
