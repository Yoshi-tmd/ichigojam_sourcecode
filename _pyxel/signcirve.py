import pyxel
import math

class App:
    BASE_X = 80     # 基準座標（X)
    BASE_Y = 60     # 基準座標（Y)
    def __init__(self):
        pyxel.init(160, 120, fps=60)

        self.x = self.BASE_X
        self.y = self.BASE_Y
        self.timer = 0
        self.speed = 0.05   # 速度
        self.intensity = 40     # 揺れ幅
        pyxel.run(self.update, self.draw)
    
    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.speed -= 0.001     # 速度ダウン
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.speed += 0.001     # 速度アップ
        if pyxel.btn(pyxel.KEY_UP):
            self.intensity += 0.4   # 振れ幅アップ
        if pyxel.btn(pyxel.KEY_DOWN):
            self.intensity -= 0.4   # 振れ幅ダウン

        self.timer += self.speed
        self.y = self.BASE_Y + self.intensity * math.sin(self.timer)
    
    def draw(self):
        pyxel.cls(0)
        # 円の描画
        pyxel.circ(self.x, self.y, 8, 9)

        # テキスト描画
        pyxel.text(0, 0, "SPEED: %f"%self.speed, 7)
        pyxel.text(0, 8, "INTENSITY: %f"%self.intensity, 7)

App()
