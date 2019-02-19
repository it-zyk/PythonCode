

import random


def main():

    while True:
    # 1. 从控制台输入命令
        player = int(input("请输入您要出的拳头 石头（1）/剪刀（2） /布（3) /退出（4）;"))
        
        
        if player == 4:
            break
        #电脑 随机出拳
        computer = random.randint(1, 3)
        
        print("玩家选择的拳头是 %d - 电脑出的 拳是 %d " % (player, computer))

        # 3. 比较胜负
        # 1.石头 胜 剪刀
        # 2.剪刀 胜 布
        # 3.布 胜 石头
        
        if ((player == 1 and computer == 2 )
                or (player == 2 and computer == 3 ) 
                or (player ==3 and  computer == 1 )):

            print("欧耶，电脑输了！")

        elif player == computer:
            print("心有灵犀啊，再来一盘。")
        else:
            print("不服气，我们决战到天明。")
        # 电脑获胜平局

        



if __name__ == "__main__":
    main()
