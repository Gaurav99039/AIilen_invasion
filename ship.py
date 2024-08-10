import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.setting = ai_game.setting

        self.image = pygame.image.load('ship.jpg')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.move_right = False
        self.move_left = False

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        if self.move_left and self.rect.left > 0:
            self.x -= self.setting.ship_speed
        self.rect.x = self.x

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        