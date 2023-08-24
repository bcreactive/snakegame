import pygame
import sys
from time import sleep

from button import Button
from player import Player
from fruit import Fruit
from scorelabel import Scorelabel


class Game:
    """Main gameclass."""

    def __init__(self):
        """Initialize game attributes."""
        pygame.init()
        self.clock = pygame.time.Clock()   
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Testgame")
        
        self.play_button = Button(self, "Snake!")
        self.player = Player(self)
        self.player_rect = pygame.Rect(self.player.x, self.player.y, self.player.width, self.player.height)
        self.fruit = Fruit(self, self.player)
        self.scorelabel = Scorelabel(self)
        self.points = 0
        self.fps = 3

        self.game_active = False
        self.fruit_visible = True
        
    def run_game(self):      
        while True:
            self._check_events()
            if self.game_active:
                self.player.update()
                self.scorelabel.prep_score()
                self.check_fruit()
            self._update_screen()  
            self.clock.tick(self.fps)
            
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
                if self.game_active:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            self.player.direction = "n"
                        if event.key == pygame.K_DOWN:
                            self.player.direction = "s"
                        if event.key == pygame.K_LEFT:
                            self.player.direction = "w"
                        if event.key == pygame.K_RIGHT:
                            self.player.direction = "e"
                            
    def _check_play_button(self, mouse_pos):
        """Start a new game if the player clicks Play."""
        if not self.game_active:
            if self.play_button.rect.collidepoint(mouse_pos):
                pygame.mixer.Channel(2).play(pygame.mixer.Sound('sound\\button.mp3'))
                sleep(1)
                pygame.mixer.Channel(0).play(pygame.mixer.Sound('sound\playing.mp3'))
                self.game_active = True
                pygame.mouse.set_visible(False)

    def hit(self):
        pygame.mixer.Channel(0).stop()
        pygame.mixer.Channel(2).play(pygame.mixer.Sound('sound\end.mp3'))
        sleep(0.2)
        pygame.mixer.Channel(3).play(pygame.mixer.Sound('sound\end_2.mp3'))
        sleep(1)
        sys.exit()

    def check_points(self):
        if self.points % 6 == 0:
            self.fps += 0.5

    def check_fruit(self):
        if self.game_active:
            self.fruit_rect = pygame.Rect(self.fruit.x, self.fruit.y, self.fruit.width, self.fruit.height)
            self.player_rect = pygame.Rect(self.player.x, self.player.y, self.player.width, self.player.height)
            if self.player_rect.colliderect(self.fruit_rect):
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('sound\pickup_1.mp3'))
                self.fruit_visible = False
                self.fruit.get_new_fruit()
                self.player.add_segment()
                self.points += 1
                self.check_points()

    def _update_screen(self):
        self.screen.fill((0, 0, 0))
        if not self.game_active:      
            self.play_button.draw_button()
        if self.game_active:
            self.player.drawme()
            if self.fruit_visible:
                self.fruit.draw_fruit()
            self.scorelabel.draw_score()        
        pygame.display.flip()

pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run_game()

