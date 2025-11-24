import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal
from alien_fleet import AlienFleet
from game_stats import GameStats
from time import sleep

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.game_stats = GameStats(self.settings.starting_ship_count)

        self.screen = pygame.display.set_mode((self.settings.screen_w,self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        self.running = True
        self.clock = pygame.time.Clock()
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_w, self.settings.screen_h))

        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)
        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(0.3)

        self.game_active = True

    def run_game(self):
        while(self.running):
            self._check_events()
            if(self.game_active):
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self):
        if(self.ship.check_collisions(self.alien_fleet.fleet)):
            self._check_game_status()
        
        if(self.alien_fleet.check_fleet_bottom()):
            self._check_game_status()

        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if(collisions):
            self.impact_sound.play()

        if self.alien_fleet.check_destroyed_status():
            self._check_game_status()

    def _check_game_status(self):
        if(self.game_stats.ships_left > 0):
            self.game_stats.ships_left -= 1
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False
        print(self.game_stats.ships_left)

    def _reset_level(self):
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

    def _update_screen(self):
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        self.alien_fleet.draw()
        pygame.display.flip()
        self.ship.update()

    def _check_events(self):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                self.running = False
                pygame.quit()
                sys.exit()
            elif(event.type == pygame.KEYDOWN):
                self._check_keydown_event(event)
            elif(event.type == pygame.KEYUP):
                self._check_keyup_event(event)
    
    def _check_keydown_event(self, event):
        if(event.key == pygame.K_RIGHT):
            self.ship.moving_right = True
        elif(event.key == pygame.K_LEFT):
            self.ship.moving_left = True
        elif(event.key == pygame.K_SPACE):
            if(self.ship.fire()):
                self.laser_sound.play()
        elif(event.key == pygame.K_q):
            self.running = False
            pygame.quit()
            sys.exit()

    def _check_keyup_event(self, event):
        if(event.key == pygame.K_RIGHT):
            self.ship.moving_right = False
        elif(event.key == pygame.K_LEFT):
            self.ship.moving_left = False

    def create():
        pass

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
