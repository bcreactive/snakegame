import pygame.font


class Scorelabel:
    """This class gets the score and prepares the image to blit."""

    def __init__(self, game):
        """Initialize scorekeeping attributes."""
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        
        # Font settings for scoring information
        self.label_color = (150, 135, 100)   
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image
        self.prep_score()
       
    def prep_score(self):
        """Turn the score into a rendered image."""
        self.score = (self.game.player.seg_amount -1) * 100
        score_str = f"Score: {self.score}"
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.label_color)
        
        # Display the score on the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def draw_score(self):
        """Draw score, level and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
       

