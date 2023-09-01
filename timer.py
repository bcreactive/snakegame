import pygame


class Time:
    """This class counts the frames and get fps rate, to calculate runtime in seconds."""
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.fps = 3
        self.stored_values = []
        self.temp_seconds = []
        self.temp_value = 0
        self.seconds = 0
        self.text_color = (130, 230, 230)
        self.font = pygame.font.SysFont(None, 60)
        self.label_color = (30, 30, 30)

    def update_timer(self, fps):
        self.actual_fps = fps
        if self.actual_fps == self.fps:
            self.temp_value += 1
        if self.actual_fps > self.fps:
            self.stored_values.append(self.temp_value)
            self.temp_value = 0
            self.fps = fps
        
    def get_time(self):
        fps = 3
        if not self.stored_values:
            value = self.temp_value / fps
            self.temp_seconds.append(value)
            self.prep_time(self.temp_seconds[0]) 
        elif self.stored_values:
            for i in self.stored_values:
                value = i / fps
                self.temp_seconds.append(value)
                fps += 0.5

            sec = 0
            for i in self.temp_seconds:
                sec = sec + i
                
            self.prep_time(sec)
            
    def prep_time(self, time):
        """Turn the runtime into a rendered image."""

        self.amount = round(time)
        time_str = self.get_time_str(self.amount)
        self.time_image = self.font.render(time_str, True,
                                    self.text_color, self.label_color)
        
        self.time_image_rect = self.time_image.get_rect()  
        self.time_image_rect.x = 20
        self.time_image_rect.y = 400  

    def get_time_str(self, time):
        """Turn the runtime into a rendered image."""

        amount = round(time)
        if amount < 10:
            time_str = f"Time: 0{amount} sec"
            return time_str
        elif amount < 60:
            time_str = f"Time: {amount} sec"
            return time_str
        if amount >= 60:
            minutes = amount / 60
            minutes = round(minutes)
            seconds = amount - (minutes * 60)
            seconds = round(seconds)
            if seconds < 10:
                time_str = f"Time: {minutes}:0{seconds}"
                return time_str
            elif seconds >= 10:
                time_str = f"Time: {minutes}:{seconds}"
                return time_str
    
    def draw_time(self):
        """Draw time."""
        self.screen.blit(self.time_image, self.time_image_rect)
        
            


