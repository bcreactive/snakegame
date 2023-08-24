import pygame


class Player:
    """This class generates the player with update and drawme methods."""
    def __init__(self, game):
        """Initialize player attributes"""
    
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.game = game
        self.width = 40
        self.height = 40
        self.x = 100
        self.y = 100
        self.direction = "s"
        self.speed = 40
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.seg_amount = 1
        self.seg_rects = []
        self.seg_rects.append(self.rect)

    def update(self):
        if self.direction == "e" and (self.x + self.width) < self.screen_rect.right:
            self.x += self.speed       
        if self.direction == "w" and self.x > self.screen_rect.left:
            self.x -= self.speed
        if self.direction == "n" and self.y > self.screen_rect.top:
            self.y -= self.speed
        if self.direction == "s" and (self.y + self.height) < self.screen_rect.bottom:
            self.y += self.speed

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.update_seg_rects(self.rect)

        # print(self.seg_rects)
        # print(self.seg_amount)
        
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
        pass
        self.seg_rects.insert(0, self.rect)
        self.seg_amount += 1

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

    