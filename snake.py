import pygame

class Snake:
    def __init__(self, block_size):
        self.block_size = block_size
        self.body = [[400, 300], [390, 300], [380, 300]]
        self.direction = [10, 0]

    def move(self):
        head = [self.body[-1][0] + self.direction[0], self.body[-1][1] + self.direction[1]]
        self.body.append(head)
        self.body.pop(0)

    def grow(self):
        self.body.insert(0, self.body[0])

    def draw(self, screen, color):
        for segment in self.body:
            pygame.draw.rect(screen, color, [segment[0], segment[1], self.block_size, self.block_size])

    def check_collision(self, width, height):
        head = self.body[-1]  # ヘッドの座標

    # 画面外への衝突判定
        if head[0] >= width or head[0] < 0 or head[1] >= height or head[1] < 0:
            return True

    # 自分自身に衝突したかの判定
    # ヘッドが自分の体の他の部分と重なっていないか確認
        #if head in self.body[:-1]:  # ヘッドが体のどこかに重なっていたら衝突
            #return True

        return False


