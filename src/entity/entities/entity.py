class Entity():
    def __init__(self, game):
        self.game=game
        self.team="baddie"#TODO: default should probably be "neutral" or similar.  should have a Baddie class that all baddies inherit from.  it can have a team of "baddie"