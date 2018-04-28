class Gato:
    def __init__(self, canvas, x,y):
        self.ref = canvas.create_rectangle(
            x,y,x+10, y+10, fill="#66FF66")
        self.x = x
        self.y = y
        self.velX = 1;
        self.velY = 1;
    def update(self, canvas, diffTime):
        if self.x > 800 or self.x < 0:
            self.velX *= -1
        if self.y > 800 or self.y < 0:
            self.velY *= -1

        canvas.move(self.ref, self.velX*diffTime, self.velY*diffTime)
        self.x += self.velX * diffTime
        self.y += self.velY * diffTime