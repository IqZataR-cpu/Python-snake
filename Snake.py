import pygame

from SnakeBlock import SnakeBlock
from settings import BLOCK_SIZE, SCREEN_SIZE, START_POSITION


class Snake:
    def __init__(self):
        self.position = SnakeBlock(START_POSITION[0], START_POSITION[1])
        self.body = [
            SnakeBlock(START_POSITION[0], START_POSITION[1]),
            SnakeBlock(START_POSITION[0] - BLOCK_SIZE, START_POSITION[1]),
            SnakeBlock(START_POSITION[0] - BLOCK_SIZE * 2, START_POSITION[1])
        ]
        self.direction = "RIGHT"

    def changeDirTo(self, dir):
        if (dir == pygame.K_RIGHT or dir == pygame.K_d) and self.direction != "LEFT":
            self.direction = "RIGHT"
        elif (dir == pygame.K_LEFT or dir == pygame.K_a) and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif (dir == pygame.K_UP or dir == pygame.K_w) and self.direction != "DOWN":
            self.direction = "UP"
        elif (dir == pygame.K_DOWN or dir == pygame.K_s) and self.direction != "UP":
            self.direction = "DOWN"

    def move(self, foodPos):
        if self.direction == "RIGHT":
            self.position.x += BLOCK_SIZE
        if self.direction == "LEFT":
            self.position.x -= BLOCK_SIZE
        if self.direction == "UP":
            self.position.y -= BLOCK_SIZE
        if self.direction == "DOWN":
            self.position.y += BLOCK_SIZE

        self.body.insert(0, SnakeBlock(self.position.x, self.position.y))

        if self.position.equalsTo(foodPos):
            return 1
        else:
            self.body.pop()
            return 0

    def checkCollision(self):
        if self.position.x > SCREEN_SIZE[0] - BLOCK_SIZE or self.position.x < 0:
            return 1
        elif self.position.y > SCREEN_SIZE[1] - BLOCK_SIZE or self.position.y < 0:
            return 1

        for bodyPart in self.body[1:]:
            if self.position.equalsTo(bodyPart):
                return 1

        return 0

    def getHeadPos(self):
        return self.position

    def getBody(self):
        return self.body

