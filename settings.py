from pathlib import Path
class Settings:
    def __init__(self):
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60

        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'nebula.png'
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'pngtree-x-wing-starfigher-star-wars-ija-collection-png-image_8656566.png'
        self.ship_w = 60
        self.ship_h = 90

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'orangelaser.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'newlaser.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'Alien-Transparent-Images.png'
        self.fleet_speed = 4
        self.fleet_direction = 1
        self.fleet_drop_speed = 40
        self.alien_w = 60
        self.alien_h = 40