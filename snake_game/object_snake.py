class  Snake:
    def __init__(self, head, fragments):
        self.head = head
        self.fragments = fragments
    
    def directions_head(self, left, right, up, down):
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        
    def snake_speed(self, speed):
        self.speed = speed
        
    def snake_curves(self, curves):
        pass
        
    def coordinates(self, x, y):
        self.x = x
        self.y = y
        
    def actions(self):
        pass
        
    def game_over(self):
        pass