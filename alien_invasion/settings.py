class Settings():
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1024
        self.screen_height = 640
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 5.0
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 8
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (218, 165, 32)
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed_factor = 2
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

