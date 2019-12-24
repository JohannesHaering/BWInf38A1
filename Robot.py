class Robot:
    def __init__(self, x, y, batteryCharge):
        self.x = x
        self.y = y
        self.batteryCharge = batteryCharge

    def right(self):
        self.x += 1
        self.batteryCharge -= 1

    def left(self):
        self.x -= 1
        self.batteryCharge -= 1

    def up(self):
        self.y -= 1
        self.batteryCharge -= 1

    def down(self):
        self.y += 1
        self.batteryCharge -= 1