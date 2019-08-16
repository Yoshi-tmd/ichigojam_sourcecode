import pyxel
import random

WINDOW_W = 160
WINDOW_H = 120

class Ball:
    def __init__(self):
        self.x = random.randint(4,WINDOW_W-4)
        self.y = random.randint(4,WINDOW_H-4)
        self.vec_x = 1
        self.vec_y = 1

    def updata(self):
        self.x += self.vec_x
        self.y += self.vec_y
        
        if self.x < 4:
            self.x = 4
            self.vec_x *= -1
        if self.x > WINDOW_W - 4:
            self.x = WINDOW_W - 4
            self.vec_x *= -1
        if self.y < 4:
            self.y = 4
            self.vec_y *= -1
        if self.y > WINDOW_H - 4:
            self.y = WINDOW_H - 4
            self.vec_y *= -1
    
    def draw(self):
        pyxel.circ(self.x, self.y, 4, 10)


class App:
    def __init__(self):
        pyxel.init(WINDOW_W, WINDOW_H, caption="Bound ball", fps=60)
        
        self.ball_list = []
        for i in range(4):
            ball = Ball()
            ball.x = random.randint(4,WINDOW_W-1)
            ball.y = random.randint(4,WINDOW_H-1)
            ball.vec_x = 1
            ball.vec_y = -1
            self.ball_list.append(ball)

        self.obj_x = WINDOW_W / 2
        self.obj_y = WINDOW_H / 2
        self.obj_w = 10
        self.obj_h = 5

        pyxel.run(self.update, self.draw)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        if pyxel.btn(pyxel.KEY_LEFT):
            self.obj_x -= 1
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.obj_x += 1
        if pyxel.btn(pyxel.KEY_UP):
            self.obj_y -= 1
        if pyxel.btn(pyxel.KEY_DOWN):
            self.obj_y += 1
        
        if self.obj_x < 0:
            self.obj_x = 0
        if self.obj_x + self.obj_w > WINDOW_W:
            self.obj_x = WINDOW_W - self.obj_w
        if self.obj_y < 0:
            self.obj_y = 0
        if self.obj_y + self.obj_h > WINDOW_H:
            self.obj_y = WINDOW_H - self.obj_h

        for ball in self.ball_list:
                ball.updata()

    def draw(self):
        pyxel.cls(0)
        # pyxel.circ(self.x, self.y, 4, 10)
        for ball in self.ball_list:
                ball.draw()
        pyxel.rect(self.obj_x, self.obj_y, self.obj_x + self.obj_w, self.obj_y + self.obj_h, 11)

App()
