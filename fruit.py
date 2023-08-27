import pygame
from random import randint


class Fruit:
    """This class generates the randomly spawned collectible."""
    def __init__(self, game, player):
        """Initialize fruit attributes."""
        
        self.game = game
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.player = player    
        self.width = 40
        self.height = 40
        self.x = self.get_rnd_x()
        self.y = self.get_rnd_y()
        self.fruit_color = (randint(1, 255), randint(0, 255), randint(1, 255))

    def get_rnd_x(self):
            x = randint(0, self.screen_rect.right - 40)
            return x
    
    def get_rnd_y(self):
            y = randint(0, self.screen_rect.bottom - 40)
            return y
    
    def get_new_fruit(self):
        self.fruit_color = (randint(1, 255), randint(0, 255), randint(1, 255))
        # self.player.body_color = self.fruit_color
        self.x = self.get_rnd_x()
        self.y = self.get_rnd_y()
        place = self.check_space(self.x, self.y)
        if place:
            self.draw_fruit()
            self.game.fruit_visible = True
            return
        else:
            self.get_new_fruit()
            return
        
    def check_space(self, x, y):
        self.fruit_rect = pygame.Rect(x, y, 39, 39)
        for i in self.game.player.seg_rects:
            if not self.fruit_rect.colliderect(i):
                return True
    
    def draw_fruit(self):
        self.fruit_img = pygame.draw.rect(self.screen, self.fruit_color, (self.x, self.y, self.width, self.height))
         