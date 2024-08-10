class Settings():
    def __init__(self) -> None:
        self.width = 600
        self.height = 600
        self.bg_color = (230,230,230)
        self.ship_speed = 0.3
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = (60,60,60)
        self.bullet_speed = 1.5
        self.bullets_allowed = 6
        self.ailen_speed = 0.2
        self.fleet_drop_speed = 10
        self.fleet_direction  = 1
        self.ship_limit = 1
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        self.ship_speed = 0.3
        self.bullet_speed = 3
        self.ailen_speed = 0.2
        self.fleet_direction = 1
        self.ailen_points = 50
    
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.ailen_speed *= self.speedup_scale
        self.ailen_points = int(self.ailen_points*self.score_scale)
