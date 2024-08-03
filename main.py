import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from ailens import Ailen


class AilenInvasion:
    def __init__(self):
        pygame.init()
        self.setting = Settings()
        self.screen = pygame.display.set_mode((self.setting.width,self.setting.height))
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.ailens = pygame.sprite.Group()
        self._create_fleet()
        self.bg_color = self.setting.bg_color
        pygame.display.set_caption('Ailen Invasion')
    
    def run_game(self):
        while True:
           self._check_events()
           self.ship.update()
           self.bullets.update()
           self._update_screen()
           for bullet in self.bullets.copy():
                if bullet.rect.bottom:
                     if bullet.rect.bottom <= 0:
                          self.bullets.remove(bullet)
                print(len(self.bullets))

    def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                     self._check_Keydown(event)
                elif event.type == pygame.KEYUP:
                     self._check_keyup(event)
                     
        
    def _check_Keydown(self,event):
         if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
         elif event.key == pygame.K_LEFT:
            self.ship.move_left = True
         elif event.key == pygame.K_q:
              sys.exit()
         elif event.key == pygame.K_SPACE:
              self._fire_bullets()
    
    def _check_keyup(self,event):
         if event.key == pygame.K_RIGHT:
              self.ship.move_right = False
         elif event.key == pygame.K_LEFT:
              self.ship.move_left = False
    
    def _fire_bullets(self):
         if len(self.bullets) < self.setting .bullets_allowed:
          new_bullet = Bullet(self)
          self.bullets.add(new_bullet)
     
    def _create_fleet(self):
         ailen = Ailen(self)
         ailen_width = ailen.rect.width
         available_space_x = self.setting.width - (2*ailen_width)
         number_ailens_x = available_space_x // (2*ailen_width)
         for ailen_number in range(number_ailens_x):
              self._create_ailen(ailen_number)
             


    def _create_ailen(self,ailen_number):
          ailen = Ailen(self)
          ailen_width,ailen_height = ailen.rect.size
          ailen.x = ailen_width + 2 * ailen_width * ailen_number
          ailen.rect.x  = ailen.x
          self.ailens.add(ailen)
          ship_height = self.ship.rect.height
          available_space_y = (self.setting.height - (3*ailen_height) - ship_height)
          number_rows = available_space_y//(2*ailen_height)
          for  row_number in range(number_rows):
               
         
         
         
                          
                     
    
    def _update_screen(self):
          self.image = pygame.image.load('ship.jpg')
          self.screen.fill(self.bg_color)
          self.ship.blitme()
          for bullet in self.bullets.sprites():
               bullet.draw_bullet()
          self.ailens.draw(self.screen)
          pygame.display.flip()
         



if __name__ == '__main__':
    ai = AilenInvasion()
    ai.run_game()
        