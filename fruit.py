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
        self.width = 40
        self.height = 40
        self.x = self.get_rnd_x()
        self.y = self.get_rnd_y()
        self.fruit_color = (randint(1, 255), randint(1, 255), randint(1, 255))
        self.bonus_fruit = False

    def get_rnd_x(self):
            x = randint(0, self.screen_rect.right - 40)
            return x
    
    def get_rnd_y(self):
            y = randint(0, self.screen_rect.bottom - 40)
            return y
    
    def check_bonus_spawn(self):
        chance = 2
        rand_number = randint(1, 1000)
        if rand_number <= chance and self.game.points >= 6:
            self.bonus_fruit = True
            print("bonus!")

    def get_new_fruit(self):
        if not self.bonus_fruit:
            self.fruit_color = (randint(1, 255), randint(0, 255), randint(1, 255))
            # self.player.body_color = self.fruit_color
            self.x = self.get_rnd_x()
            self.y = self.get_rnd_y()
            place = self.check_space(self.x, self.y, self.game.player.seg_rects[:])

            # while not place:
            #     self.get_new_fruit()
            #     if place: 
            #          break   
            self.draw_fruit()
            self.game.fruit_visible = True
                
            # else:
            #     self.get_new_fruit()
                # return
        if self.bonus_fruit:
            self.bonus_fruit = False
        
    def check_space(self, x, y, rects):
        self.rects = rects
        self.fruit_rect = pygame.Rect(x, y, 40, 40)
        for i in self.rects:
            if not self.fruit_rect.colliderect(i):
                return True
    
    def draw_fruit(self):
        self.fruit_img = pygame.draw.rect(self.screen, self.fruit_color, (self.x, self.y, self.width, self.height))
         