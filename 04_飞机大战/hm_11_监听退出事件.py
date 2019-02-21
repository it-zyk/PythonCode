import pygame
from plane_sprites import *


def main():
    # 游戏的初始化
    pygame.init()
    # 创建游戏的窗口
    screen = pygame.display.set_mode((480, 700))

    # 绘制背景图像
    bg = pygame.image.load("./images/background.png")
    screen.blit(bg, (0, 0))

    # 绘制英雄飞机
    hero = pygame.image.load("./images/me1.png")
    screen.blit(hero, (150, 300))

    # 可以在所有绘制工作完成之后，统一调用update()
    pygame.display.update()

    # 创建时钟
    clock = pygame.time.Clock()

    # 1. 定义rect记录飞机的初始化位置
    hero_rect = pygame.Rect(150, 300, 102, 126)

    # 创建敌机的精灵
    enemy = GameSprite("./images/enemy1.png")
    enemy = GameSprite("./images/enemy1.png")

    # 创建敌机精灵组
    enemy_group = pygame.sprite.Group(enemy)

    while True:

        clock.tick(60)

        for event in pygame.event.get():

            # 判断事件类型是否是退出
            if event.type == pygame.QUIT:
                print("游戏退出...")

                # quit 卸载所有模块
                pygame.quit()

                # exit() 直接退出当前正在执行的程序
                exit()

        # 修改飞机的位置
        hero_rect.y -= 1

        # 判断飞机的位置
        if hero_rect.y <= 0:
            hero_rect.y = 700

            # 3.调用blit方法绘制退休
        screen.blit(bg, (0, 0))
        screen.blit(hero, hero_rect)

        # 4 让精灵组调用两个方法
        enemy_group.update()

        enemy_group.draw(screen)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
