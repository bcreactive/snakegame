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
        self.width = 20
        self.height = 20
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
            self.x = self.get_rnd_x()
            self.y = self.get_rnd_y()
            self.width = 20
            self.height = 20
            place = self.check_space(self.x, self.y, self.game.player.seg_rects[:])
            
            while not place:
                self.get_new_fruit()
                if place: 
                    break                 
            self.draw_fruit()
            self.game.fruit_visible = True

    def check_space(self, x, y, rects):
        self.rects = rects
        self.fruit_rect = pygame.Rect(x, y, 20, 20)
        for i in self.rects:
            if not self.fruit_rect.colliderect(i):
                return True
    
    def draw_fruit(self):
        if not self.bonus_fruit:
            pygame.draw.rect(self.screen, self.fruit_color, (self.x, self.y, self.width, self.height))
       