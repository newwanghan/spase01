import pygame  # 将pygame库导入到python程序中
from pygame.locals import *  # 导入pygame中的常量
import sys  # 导入系统模块

SCREENWIDTH = 822
SCREENHEIGHT = 199
FPS = 30


class MyMap():
    def __init__(self, x, y):
        self.bg = pygame.image.load('image/bg.png')
        self.x = x
        self.y = y

    def map_rolling(self):
        if self.x < -790:
            self.x = 800
        else:
            self.x -= 5

    def map_update(self):
        SCREEN.blit(self.bg, (self.x, self.y))


class Music_Button():
    is_open = True

    def __init__(self):
        self.open_img = pygame.image.load('image/btn_open.png').convert_alpha()
        self.close_img = pygame.image.load('image/btn_close.png').convert_alpha()
        self.bg_music = pygame.mixer.Sound('audio/bg_music.wav')

    def is_select(self):
        point_x, point_y = pygame.mouse.get_pos()
        w, h = self.open_img.get_size()
        in_x = point_x > 20 and point_x < 20 + w
        in_y = point_y > 20 and point_y < 20 + h
        return in_x and in_y


from itertools import cycle


class Marie():
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.jumpState = False
        self.jumpHeight = 130
        self.lowest_y = 140
        self.jumpValue = 0
        self.marieIndex = 0
        self.marieIndexGen = cycle([0, 1, 2])

        self.adventure_img = (
            pygame.image.load("image/adventure1.png").convert_alpha(),
            pygame.image.load("image/adventure2.png").convert_alpha(),
            pygame.image.load("image/adventure3.png").convert_alpha()
        )
        self.jump_audio = pygame.mixer.Sound('audio/jump.wav')
        self.rect.size = self.adventure_img[0].get_size()
        self.x = 50
        self.y = self.lowest_y
        self.rect.topleft = (self.x, self.y)

    def jump(self):
        self.jumpState = True

    def move(self):
        if self.jumpState:
            if self.rect.y >= self.lowest_y:
                self.jumpValue = -5
            if self.rect.y <= self.lowest_y - self.jumpHeight:
                self.jumpValue = 5
            self.rect.y += self.jumpValue
            if self.rect.y >= self.lowest_y:
                self.jumpState = False

    def draw_marie(self):
        marieIndex = next(self.marieIndexGen)
        SCREEN.blit(self.adventure_img[marieIndex], (self.x, self.rect.y))


import random


class Obstacle():
    score = 1
    move = 5
    obstacle_y = 150

    def __init__(self):
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.missile = pygame.image.load("image/missile.png").convert_alpha()
        self.pipe = pygame.image.load("image/pipe.png").convert_alpha()
        self.numbers = (pygame.image.load('image/0.png').convert_alpha(),
                        pygame.image.load('image/1.png').convert_alpha(),
                        pygame.image.load('image/2.png').convert_alpha(),
                        pygame.image.load('image/3.png').convert_alpha(),
                        pygame.image.load('image/4.png').convert_alpha(),
                        pygame.image.load('image/5.png').convert_alpha(),
                        pygame.image.load('image/6.png').convert_alpha(),
                        pygame.image.load('image/7.png').convert_alpha(),
                        pygame.image.load('image/8.png').convert_alpha(),
                        pygame.image.load('image/9.png').convert_alpha())
        self.score_audio = pygame.mixer.Sound('audio/score.wav')

        r = random.randint(0, 1)
        if r == 0:
            self.image = self.missile
            self.move = 15
            self.obstacle_y = 100
        else:
            self.image = self.pipe
        self.rect.size = self.image.get_size()
        self.width, self.height = self.rect.size

        self.x = 800
        self.y = self.obstacle_y
        self.rect.center = (self.x, self.y)

    def obstacle_move(self):
        self.rect.x -= self.move

    def draw_obstacle(self):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))

    def getScore(self):
        # self.score
        tmp = self.score
        if tmp == 1:
            self.score_audio.play()
        self.score = 0
        return tmp

    def showScore(self, score):
        self.scoreDigits = [int(x) for x in list(str(score))]
        totalWidth = 0
        for digit in self.scoreDigits:
            totalWidth += self.numbers[digit].get_width()
        Xoffset = (SCREENWIDTH - (totalWidth + 30))
        for digit in self.scoreDigits:
            SCREEN.blit(self.numbers[digit], (Xoffset, SCREENHEIGHT * 0.1))
            Xoffset += self.numbers[digit].get_width()


def game_over():
    bump_audio = pygame.mixer.Sound('audio/bump.wav')
    bump_audio.play()
    screen_w = pygame.display.Info().current_w
    screen_h = pygame.display.Info().current_h
    over_img = pygame.image.load('image/gameover.png').convert_alpha()
    SCREEN.blit(over_img, ((screen_w - over_img.get_width()) / 2, (screen_h - over_img.get_height()) / 2))


def mainGame():
    score = 0
    over = False
    global SCREEN, FPSCLOCK
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption('玛丽冒险')
    bg1 = MyMap(0, 0)
    bg2 = MyMap(800, 0)
    marie = Marie()

    addObstacleTimer = 0
    li = []

    music_button = Music_Button()
    btn_img = music_button.open_img
    music_button.bg_music.play(-1)

    while True:
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONUP:
                if music_button.is_select():
                    if music_button.is_open:
                        btn_img = music_button.close_img
                        music_button.is_open = False
                        music_button.bg_music.stop()
                    else:
                        btn_img = music_button.open_img
                        music_button.is_open = True
                        music_button.bg_music.play(-1)

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN and event.key == K_SPACE:
                if marie.rect.y >= marie.lowest_y:
                    marie.jump_audio.play()
                    marie.jump()
                if over == True:
                    mainGame()

        if over == False:
            bg1.map_update()
            bg1.map_rolling()
            bg2.map_update()
            bg2.map_rolling()

            marie.move()
            marie.draw_marie()

            if addObstacleTimer >= 1300:
                r = random.randint(0, 100)
                if r > 40:
                    obstacle = Obstacle()
                    li.append(obstacle)
                addObstacleTimer = 0

            for i in range(len(li)):
                li[i].obstacle_move()
                li[i].draw_obstacle()

                if pygame.sprite.collide_rect(marie, li[i]):
                    over = True
                    game_over()
                    music_button.bg_music.stop()
                else:
                    if (li[i].rect.x + li[i].rect.width) < marie.rect.x:
                        score += li[i].getScore()
                li[i].showScore(score)

        addObstacleTimer += 20
        SCREEN.blit(btn_img, (20, 20))
        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    mainGame()
