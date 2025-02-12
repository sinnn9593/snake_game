import pygame
from snake import Snake
from food import Food
import random


class Game:
    def __init__(self, width, height, block_size, speed):
        #画面
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Snake Game with Teleport Feature")
        self.clock = pygame.time.Clock()
        self.width = width
        self.height = height
        self.block_size = block_size
        self.speed = speed
        #サウンドセットアップ
        pygame.mixer.init()
        pygame.mixer.music.load("music/BGM1.mp3")
        pygame.mixer.music.play(-1)
        self.collision_sound = pygame.mixer.Sound("music/effect2.wav")
        self.collision_sound.set_volume(10.0)  # 最大音量



        self.snake = Snake(block_size)
        self.food = Food(block_size)
        self.food.respawn(width, height)
        self.teleport_count = 3

    def display_score(self, score):
        font = pygame.font.SysFont("comicsansms", 25)
        corrected_score = score - 1  # 初期の長さ1を引く
        score_text = font.render(
            f"Score: {corrected_score} | Teleports: {self.teleport_count}", True, (255, 255, 255))
        self.screen.blit(score_text, [10, 10])

    def teleport_snake(self):
        if self.teleport_count > 0:
            new_x = round(random.randrange(
                0, self.width - self.block_size) / 10.0) * 10.0
            new_y = round(random.randrange(
                0, self.height - self.block_size) / 10.0) * 10.0
            self.snake.body[-1] = [new_x, new_y]
            self.teleport_count -= 1

    def run(self):
        running = True
        print("Game started!")  # デバッグメッセージ

        while running:
            self.screen.fill((50, 153, 213))  # 背景色を設定

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.snake.direction = [-self.block_size, 0]
                        elif event.key == pygame.K_RIGHT:
                            self.snake.direction = [self.block_size, 0]
                        elif event.key == pygame.K_UP:
                            self.snake.direction = [0, -self.block_size]
                        elif event.key == pygame.K_DOWN:
                            self.snake.direction = [0, self.block_size]
                        elif event.key == pygame.K_t:  # "T"キーでテレポート
                            self.teleport_snake()

            self.snake.move()

        # 衝突判定
            if self.snake.check_collision(self.width, self.height):
                print("Game Over")
                running = False

        # 食べ物を食べたかどうかの判定
            if self.snake.body[-1] == self.food.position:
                self.snake.grow()
                self.food.respawn(self.width, self.height)
                self.collision_sound.play()

        # 蛇と食べ物を描画
            self.snake.draw(self.screen, (0, 0, 0))
            self.food.draw(self.screen, (0, 255, 0))

        # スコアを表示
            self.display_score(len(self.snake.body) - 1)

            pygame.display.update()
            self.clock.tick(self.speed)

        pygame.quit()
