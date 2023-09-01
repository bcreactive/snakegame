import pygame
from fruit import Fruit
from random import randint


class BonusFruit(Fruit):
    """Class to build a bonus fruit."""

    def __init__(self, game, player):
        self.game = game
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.player = game.player    
        self.width = 80
        self.height = 80
        self.x = self.get_rnd_x()
        self.y = self.get_rnd_y()
        self.rect = (self.x, self.y, self.width, self.height)
        self.bonus_fruit_color = (randint(20, 255), randint(20, 255), randint(20, 255))
        
    def check_bonus_spawn(self):
        if not self.game.bonus_fruit_visible:
            chance = 2
            rand_number = randint(1, 100)
            if rand_number <= chance and self.game.points >= 3:
                self.bonus_fruit = True
                self.get_bonus_fruit()

    def check_fruit_place(self, x, y, rects):
        self.rects = rects
        self.fruit_rect = pygame.Rect(x, y, 39, 39)
        for i in self.rects:
            if not self.fruit_rect.colliderect(i):
                return True
    
    def get_bonus_fruit(self):
        # self.bonus_fruit_color = (randint(1, 255), randint(0, 255), randint(1, 255))
        self.x = self.get_rnd_x()
        self.y = self.get_rnd_y()
        self.width = 80
        self.height = 80
        place = self.check_space(self.x, self.y, self.game.player.seg_rects[:])

        while not place:
            self.get_new_fruit()
            if place: 
                break   

        self.draw_fruit()
        self.game.bonus_fruit_visible = True
        self.bonus_fruit = False

    def check_bonus_fruit(self):
        if self.game.game_active:
            self.bonus_fruit_rect = pygame.Rect(self.x, self.y, self.width, self.height)
            self.player_rect = pygame.Rect(self.player.x, self.player.y, self.player.width, self.player.height)
            if self.player_rect.colliderect(self.bonus_fruit_rect) and self.game.bonus_fruit_visible == True:
                self.game.bonus_fruit_visible = False    
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('sound\pickup_1.mp3'))
               
                if len(self.player.seg_rects) > 2:
                    self.player.seg_rects.pop()
                self.game.score += 1000 
                return

    def draw_bonus_fruit(self):
        pygame.draw.rect(self.screen, self.bonus_fruit_color, (self.x, self.y, self.width, self.height))