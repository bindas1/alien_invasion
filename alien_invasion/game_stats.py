class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_sets):
        self.ai_sets = ai_sets
        self.reset_stats()
        # Start game in an inactive state.
        self.game_active = False


    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_sets.ship_limit
