import pygame
from fruit import Fruit
from random import randint


class BonusFruit(Fruit):
    """Class to build a bonus fruit."""

    def __init__(self, game, player):
        self.game = game
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.player = player    
        self.width = 80
        self.height = 80
        self.width = 40
        self.height = 40
        self.x = self.get_rnd_x()
        self.y = self.get_rnd_y()
        self.rect = (self.x, self.y, self.width, self.height)
        
    def check_spawn(self):
        chance = 5
        rand_number = randint(1, 100)
        if rand_number <= chance:
            self.get_new_fruit()

    def check_fruit_place(self, x, y, rects):
        self.rects = rects
        self.fruit_rect = pygame.Rect(x, y, 39, 39)
        for i in self.rects:
            if not self.fruit_rect.colliderect(i):
                return True
    
    def get_bonus_fruit(self):
        self.fruit_color = (randint(1, 255), randint(0, 255), randint(1, 255))
        self.x = self.get_rnd_x()
        self.y = self.get_rnd_y()
        place = self.check_fruit_place(self.x, self.y)

        if place:
            self.rect = (self.x, self.y, 80, 80)
            self.draw_bonus_fruit()
            self.game.fruit_visible = True
            return
        else:
            self.get_bonus_fruit()
        
    def draw_fruit(self):
        self.bonus_fruit_img = pygame.draw.rect(self.screen, self.fruit_color, (self.rect))