import pygame
from fruit import Fruit
from random import randint


class BonusFruit:
    """Class to build a bonus fruit."""

    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.player = game.player   
        self.scorelabel = game.scorelabel
        self.width = 50
        self.height = 50
        self.x = randint(0, self.screen_rect.right - 50)
        self.y = randint(0, self.screen_rect.bottom - 50)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.bonus_fruit_color = (randint(20, 255), randint(20, 255), randint(20, 255))
        self.ticks = 20
        self.bonus_fruit = False
        
    def check_bonus_spawn(self):
        if not self.game.bonus_fruit_visible:
            chance = 100
            rand_number = randint(1, 1000)
            if rand_number <= chance and self.game.points > 1:
                self.bonus_fruit = True
                self.get_bonus_fruit()              
            
    def get_bonus_fruit(self):
        self.bonus_fruit_color = (randint(1, 255), randint(0, 255), randint(1, 255))
        self.x = randint(0, self.screen_rect.right - self.width)
        self.y = randint(0, self.screen_rect.bottom - self.height)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
        place = self.check_space() and self.check_scorelabel() and self.check_pickup()
        if place:
            self.draw_bonus_fruit()
            pygame.mixer.Channel(3).play(pygame.mixer.Sound('sound\pickup_bonus_2.mp3'))
            self.game.bonus_fruit_visible = True
            self.bonus_fruit = False
        else:
            self.get_bonus_fruit()

    def check_space(self):
        l = len(self.game.player.seg_rects)
        for i in range(0, l):               
            if self.rect.colliderect(self.game.player.seg_rects[i]):
                return False
        return True
        
    def check_scorelabel(self):
        labelrect = self.scorelabel.score_rect
        if not self.rect.colliderect(labelrect):
            return True
    
    def check_pickup(self):
        if not self.rect.colliderect(self.game.fruit.fruit_rect):
            return True
   
    def check_bonus_fruit(self):
        if self.game.game_active:
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
            self.player_rect = pygame.Rect(self.player.x, self.player.y, self.player.width, self.player.height)

            if self.player_rect.colliderect(self.rect) and self.game.bonus_fruit_visible == True:
                self.game.bonus_fruit_visible = False    
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('sound\pickup_bonus.mp3'))  

                if len(self.player.seg_rects) > 2:
                    self.player.seg_rects.pop()
                self.game.score += 1000 
                self.ticks = 20
                return
            
    def bonus_timer(self):
        if self.ticks == 0:
            self.game.bonus_fruit_visible = False
            self.ticks = 20

    def bonus_click(self):
        if self.ticks > 10:
            if self.ticks % 3 == 0:
                pygame.mixer.Channel(4).play(pygame.mixer.Sound('sound\\bonus_timer.mp3'))
        elif self.ticks <= 9:
            if self.ticks % 2 == 1:
                pygame.mixer.Channel(4).play(pygame.mixer.Sound('sound\\bonus_timer.mp3'))

    def draw_bonus_fruit(self):
        pygame.draw.rect(self.screen, self.bonus_fruit_color, (self.x, self.y, self.width, self.height))