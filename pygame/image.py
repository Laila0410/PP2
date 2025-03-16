import pygame
class Pic():
    def __init__(self, sceen):
               self.screen = screen
               self.image = pygame.image.load('image.jpeg')
               self.rect = self.image.get_react()
               self.screen_rect = screeen.get_rect()
               self.rect.center = self.screen_rect.center
    def output(self):
        self.screen.blit(self.image, self.rect)