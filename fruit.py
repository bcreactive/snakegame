import pygame
from random import randint


class Fruit:
    """This class generates the randomly spawned collectible."""

    def __init__(self, game):
        """Initialize fruit attributes."""
        
        self.game = game
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.player = game.player
        self.scorelabel = game.scorelabel
        self.score_rect = self.scorelabel.score_rect
        self.width = 20
        self.height = 20
        self.fruit_rect = pygame.rect.Rect(0, 0, 20, 20)
        self.snake_rects = game.player.seg_rects
        self.x = self.get_rnd_x()
        self.y = self.get_rnd_y()
        self.fruit_color = (randint(1, 255), randint(1, 255), randint(1, 255))
        self.bonus_fruit = False

    def get_rnd_x(self):
            x = randint(0, self.screen_rect.right - 20)
            return x
    
    def get_rnd_y(self):
            y = randint(0, self.screen_rect.bottom - 20)
            return y

    def get_new_fruit(self):
        if not self.bonus_fruit:
            self.fruit_color = (randint(1, 255), randint(0, 255), randint(1, 255))
            self.width = 20
            self.height = 20
            self.x = self.get_rnd_x()
            self.y = self.get_rnd_y()
            place = self.check_space(self.fruit_rect, self.snake_rects) and self.check_scorelabel(self.score_rect, self.fruit_rect)
            if not place:
                self.get_new_fruit()
                if place: 
                    return True

            self.draw_fruit()
            self.game.fruit_visible = True

    def check_scorelabel(self, labelrect, fruitrect):
        self.labelrect = labelrect
        self.fruitrect = fruitrect
        if not self.fruitrect.colliderect(self.labelrect):
            return True

    def check_space(self, fruitrect, rects):
        snake_rects = rects
        fruit_rect = fruitrect
        for rect in snake_rects:
            if not fruit_rect.colliderect(rect):
                return True
              
    def draw_fruit(self):
        if not self.bonus_fruit:
            pygame.draw.rect(self.screen, self.fruit_color, (self.x, self.y, self.width, self.height))
       