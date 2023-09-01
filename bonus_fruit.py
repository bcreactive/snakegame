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
        self.width = 60
        self.height = 60
        self.x = self.get_rnd_x()
        self.y = self.get_rnd_y()
        self.rect = (self.x, self.y, self.width, self.height)
        self.bonus_fruit_color = (randint(20, 255), randint(20, 255), randint(20, 255))
        self.ticks = 21
        
    def check_bonus_spawn(self):
        if not self.game.bonus_fruit_visible:
            chance = 10
            rand_number = randint(1, 100)
            if rand_number <= chance and self.game.points >= 1:
                self.bonus_fruit = True
                self.get_bonus_fruit()
                
    def get_rnd_x(self):
            x = randint(0, self.screen_rect.right - self.width)
            return x
    
    def get_rnd_y(self):
            y = randint(0, self.screen_rect.bottom - self.height)
            return y

    def check_fruit_place(self, x, y, rects):
        self.rects = rects
        self.fruit_rect = pygame.Rect(x, y, self.width, self.height)
        for i in self.rects:
            if not self.fruit_rect.colliderect(i):
                return True
    
    def get_bonus_fruit(self):
        self.bonus_fruit_color = (randint(1, 255), randint(0, 255), randint(1, 255))
        self.x = self.get_rnd_x()
        self.y = self.get_rnd_y()
        self.width = 60
        self.height = 60
        place = self.check_space(self.x, self.y, self.game.player.seg_rects[:])

        while not place:
            self.get_new_fruit()
            if place: 
                break   

        self.draw_fruit()
        pygame.mixer.Channel(3).play(pygame.mixer.Sound('sound\pickup_bonus_2.mp3'))
        self.game.bonus_fruit_visible = True
        self.bonus_fruit = False

    def check_bonus_fruit(self):
        if self.game.game_active:
            self.bonus_fruit_rect = pygame.Rect(self.x, self.y, self.width, self.height)
            self.player_rect = pygame.Rect(self.player.x, self.player.y, self.player.width, self.player.height)

            if self.player_rect.colliderect(self.bonus_fruit_rect) and self.game.bonus_fruit_visible == True:
                self.game.bonus_fruit_visible = False    
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('sound\pickup_bonus.mp3'))      

                if len(self.player.seg_rects) > 2:
                    self.player.seg_rects.pop()
                self.game.score += 1000 
                self.ticks = 21
                return
            
    def bonus_timer(self):
        if self.ticks == 0:
            self.game.bonus_fruit_visible = False
            self.ticks = 21

    def bonus_click(self):
        if self.ticks > 10:
            if self.ticks % 3 == 0:
                pygame.mixer.Channel(4).play(pygame.mixer.Sound('sound\\bonus_timer.mp3'))
        elif self.ticks <= 9:
            if self.ticks % 2 == 1:
                pygame.mixer.Channel(4).play(pygame.mixer.Sound('sound\\bonus_timer.mp3'))
        # elif self.ticks < 2:
        #     pygame.mixer.Channel(4).play(pygame.mixer.Sound('sound\\bonus_timer.mp3'))

    def draw_bonus_fruit(self):
        pygame.draw.rect(self.screen, self.bonus_fruit_color, (self.x, self.y, self.width, self.height))