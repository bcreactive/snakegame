import pygame
import random


class Player:
    """This class generates the player with update and drawme methods."""
    def __init__(self, game):
        """Initialize player attributes"""
    
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.screen_width = self.screen_rect.width
        self.screen_height = self.screen_rect.height
        self.game = game
        self.width = 39
        self.height = 39
        self.x = 240
        self.y = 200
        self.head_color = (110, 110, 210)
        self.body_color = (30, 250, 170)
        choice = ["n", "s", "e", "w"]
        self.direction = random.choice(choice)
        self.speed = 39
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.seg_amount = 1
        self.seg_rects = []
        self.seg_rects.append(self.rect)

        self.wall_collision = False

    def update(self):       
        if self.direction == "e":
            self.x += self.speed   
        if self.direction == "w":
            self.x -= self.speed
        if self.direction == "n":
            self.y -= self.speed
        if self.direction == "s":
            self.y += self.speed
        self.wall_collision = self.check_border()
        if self.wall_collision:
            self.teleport_body()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.update_seg_rects(self.rect)
        self.check_body()
        
    def check_border(self):
        if self.x >= self.screen_rect.right - self.width:
            return True
        if self.x <= self.screen_rect.left:
            return True
        if self.y >= self.screen_rect.bottom - self.height:
            return True
        if self.y <= self.screen_rect.top:
            return True

    def update_seg_rects(self, master):
        self.seg_rects.insert(0, master)
        self.seg_rects.pop()

    def check_body(self):
        l = len(self.seg_rects)
        if l > 3:
            for i in range(1, l):               
                if self.rect.colliderect(self.seg_rects[i]):
                    self.game.hit()

    def add_segment(self):
        self.seg_rects.insert(0, self.rect)
        self.seg_amount += 1

    def teleport_body(self):
        for seg in self.seg_rects:
            if self.x >= self.screen_width - self.width:
                self.x -= self.screen_rect.width
            if self.x <= self.screen_rect.left:
                self.x += self.screen_rect.width
            if self.y >= self.screen_rect.bottom - self.height:
                self.y -= self.screen_rect.height
            if self.y <= self.screen_rect.top:
                self.y += self.screen_rect.height
    
    def reset_stats(self):
        self.seg_amount = 1
        self.game.fps = 3
        self.game.points = 0
        self.game.scorelabel.score = 0
        self.game.timer.stored_values = []
        self.game.timer.temp_seconds = []
        self.game.timer.temp_value = 0
        self.game.timer.seconds = 0
        self.get_new_snakehead()

    def get_new_snakehead(self):
        choice = ["n", "s", "e", "w"]
        self.direction = random.choice(choice)
        self.x = 240
        self.y = 200
        self.head_color = (110, 110, 210)
        self.body_color = (30, 250, 170)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.seg_rects = []
        self.seg_rects.append(self.rect)

    def drawme(self):
        l = len(self.seg_rects)
        if l == 1:
            self.head = pygame.draw.rect(self.screen, (255, 255, 255), (self.seg_rects[0]), 2)
        if l > 1:
            self.head = pygame.draw.rect(self.screen, (self.head_color), (self.seg_rects[0]))
        self.draw_eyes() 
         
        # changes color for every frame
        # self.body_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        for i in  range(1, l-1):
            self.player_img = pygame.draw.rect(self.screen, (self.body_color), (self.seg_rects[i]))

    def draw_eyes(self):
        if self.direction == "e":
            pygame.draw.circle(self.screen, (200,200,200), (self.x + 40, self.y + 10), 5)
            pygame.draw.circle(self.screen, (200,200,200), (self.x + 40, self.y + 30), 5)
        if self.direction == "w":
            pygame.draw.circle(self.screen, (200,200,200), (self.x , self.y + 10), 5)
            pygame.draw.circle(self.screen, (200,200,200), (self.x , self.y + 30), 5)
        if self.direction == "n":
            pygame.draw.circle(self.screen, (200,200,200), (self.x + 10, self.y ), 5)
            pygame.draw.circle(self.screen, (200,200,200), (self.x + 30, self.y ), 5)
        if self.direction == "s":
            pygame.draw.circle(self.screen, (200,200,200), (self.x + 10, self.y + 40), 5)
            pygame.draw.circle(self.screen, (200,200,200), (self.x + 30, self.y + 40), 5)

    