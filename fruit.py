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

    def draw_fruit(self):
        self.fruit_img = pygame.draw.rect(self.screen, (230,135,20), (self.x, self.y, self.width, self.height))

    def get_rnd_x(self):
            x = randint(10, self.screen_rect.right - 50)
            return x
    
    def get_rnd_y(self):
            y = randint(10, self.screen_rect.bottom - 50)
            return y
    
    def get_new_fruit(self):
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
        self.fruit_rect = f"<(rect({x}, {y}, 40, 40)>"
        if not self.fruit_rect in self.player.seg_rects:
            return True