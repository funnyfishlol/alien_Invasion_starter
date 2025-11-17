from pathlib import Path
class Settings:
    def __init__(self):
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'alien_Invasion_starter' / 'Assets' / 'images' / 'Starbasesnow.png'
        self.ship_file = Path.cwd() / 'alien_Invasion_starter' / 'Assets' / 'images' / 'pngtree-x-wing-starfigher-star-wars-ija-collection-png-image_8656566.png'
        self.ship_w = 60
        self.ship_h = 90