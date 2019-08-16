import pyxel
import random

class App:
    def __init__(self):
        pyxel.init(160, 120, fps=30, caption='Random Walk')
        self.init()
        pyxel.run(self.update, self.draw)
    
    def init(self):
        # X座標とY座標の初期化
        self.x = pyxel.width / 2 - 1
        self.y = pyxel.height / 2 - 1
        # 体のX座標とY座標を入れるリストを初期化
        self.body_list = []

    def update(self):
        # 最新のX座標とY座標を一時的に入れておくリストを初期化
        # フレーム毎で初期化
        temp_list = []
        # X座標とY座標に乱数（－2, -1, 0, 1, 2）を足す
        self.x += random.randint(-1 ,1)
        self.y += random.randint(-1 ,1)
        # 画面内に制限
        if self.x < 0:
            self.x = 0
        if self.x > pyxel.width - 1:
            self.x = pyxel.width - 1
        if self.y < 0:
            self.y = 0
        if self.y > pyxel.width - 1:
            self.y = pyxel.width - 1
        # 一時的リストに追加
        temp_list.append(self.x)
        temp_list.append(self.y)
        # 一時的リストの要素を体の座標リストに追加
        self.body_list.append(temp_list)
        # 要素の数が30を超えたら、一番古い要素を削除
        if len(self.body_list) > 30:
            del self.body_list[0]


    def draw(self):
        pyxel.cls(0)
        # 体の座標リストからループ処理で描画
        for i in range(len(self.body_list)):
            pyxel.rect(self.body_list[i][0], self.body_list[i][1], self.body_list[i][0] + 1, self.body_list[i][1] + 1, 11)
        # 先頭を赤色にするために別で描画
        pyxel.rect(self.x, self.y, self.x + 1, self.y + 1, 8)
            
        # 先頭のX座標とY座標を表示
        pyxel.text(0, 0, "X:%f"%self.x, 7)
        pyxel.text(0, 6, "Y:%f"%self.y, 7)

App()