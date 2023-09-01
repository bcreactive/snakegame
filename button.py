import pygame.font


class Button:
    """A class to build buttons for the game."""

    def __init__(self, game, msg):
        """Initialize button attributes."""

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        if msg == "Snake!":
            self.width, self.height = 160, 80
            self.button_color = (96, 21, 95)
        elif msg == "Snake again?":
            self.width, self.height = 300, 80
            self.button_color = (55, 23, 100)
        self.text_color = (255, 55, 255)
        self.font = pygame.font.SysFont(None, 60)

        # Build the button's rect object and set position.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        if msg == "Snake!":
            self.rect.center = self.screen_rect.center
            # self.rect.x = 250
            # self.rect.y = 400
        elif msg == "Snake again?":
            self.rect.x = 20
            self.rect.y = 300
        
        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        # self.mouse_pos = pygame.mouse.get_pos()
        # if self.rect.collidepoint(pygame.mouse.get_pos()):
        #     self.button_color = (255, 223, 200)
        self.msg_image = self.font.render(msg, True, self.text_color,
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw massage."""
        self.screen.fill(self.button_color, self.rect)
        self.border = pygame.draw.rect(self.screen, (255, 255, 255), (self.rect), 2)
        self.screen.blit(self.msg_image, self.msg_image_rect)