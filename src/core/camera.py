class Camera:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.scale = 1

    @property
    def centerx(self):
        return self.w / 2 - self.x
    
    @property
    def centery(self):
        return self.h / 2 - self.y
    
    @property
    def left(self):
        return int(self.x - self.w / 2)

    @property
    def top(self):
        return int(self.y - self.h / 2)
    
    @property
    def right(self):
        return int(self.x + self.w / 2)

    @property
    def bottom(self):
        return int(self.y + self.h / 2)

    @property
    def zoom(self):
        return self.scale

    @zoom.setter
    def zoom(self, value):
        self.scale = value

    def to_home(self):
        self.zoom = 1
        self.x = 0
        self.y = 0
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def collide(self, obj):
        x, y = obj.position * self.scale
        return self.left <= x <= self.right and self.top <= y <= self.bottom
