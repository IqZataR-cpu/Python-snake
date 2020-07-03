from random import randrange

from SnakeBlock import SnakeBlock
from settings import SCREEN_SIZE, BLOCK_SIZE


class FoodSpawner:
    def __init__(self):
        self.position = SnakeBlock(
            randrange(1, SCREEN_SIZE[0] / BLOCK_SIZE) * BLOCK_SIZE,
            randrange(1, SCREEN_SIZE[1] / BLOCK_SIZE) * BLOCK_SIZE
        )
        self.isFoodOnScreen = True

    def spawnFood(self):
        if not self.isFoodOnScreen:
            self.position = SnakeBlock(
                randrange(1, SCREEN_SIZE[0] / BLOCK_SIZE) * BLOCK_SIZE,
                randrange(1, SCREEN_SIZE[1] / BLOCK_SIZE) * BLOCK_SIZE
            )
            self.isFoodOnScreen = True

        return self.position

    def setFoodOnScreen(self, bool):
        self.isFoodOnScreen = bool
