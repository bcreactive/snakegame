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
        self.width = 40
        self.height = 40
        self.x = 380
        self.y = 260
        # choice = ["n", "s", "e", "w"]
        # self.direction = random.choice(choice)
        self.direction = "n"
        self.speed = 40
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

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.update_seg_rects(self.rect)

        self.wall_collision = self.check_border()
        if self.wall_collision:
            self.teleport_body()
        self.check_body()
        
        # print(self.seg_rects)
        # print(self.seg_amount)

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


    def drawme(self):
        l = len(self.seg_rects)
        # for i in  range(l*(-1), -1):
        #     self.player_img = pygame.draw.rect(self.screen, (100,100,100), (self.seg_rects[i]))
        self.head = pygame.draw.rect(self.screen, (100,100,100), (self.seg_rects[0]))
        self.draw_eyes()  
        for i in  range(1, l-1):
            self.player_img = pygame.draw.rect(self.screen, (100,100,100), (self.seg_rects[i]))
        # self.head = pygame.draw.rect(self.screen, (100,100,100), (self.seg_rects[0]))
        # self.draw_eyes()

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

    