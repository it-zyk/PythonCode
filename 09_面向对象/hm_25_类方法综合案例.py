

class Game(object):
    
    #类属性
    top_score = 0

    def __init__(self, player_name):
        
        self.player_name = player_name
    
    
    # 静态方法

    @staticmethod
    def show_help():
        print("帮助信息")


    
    # 类方法

    @classmethod
    def show_top_score(cls):
        print("历史最高分 %.2f" % cls.top_score)


    def start_game(self):
        print("%s开始游戏" % self.player_name)




def main():
    
    # 1. 创建类属性
    gm = Game("小明")


    # 2. 访问实例方法
    gm.start_game()

    Game.show_top_score()
    
    # 3 访问静态方法
    Game.show_help()



if __name__ == "__main__":
    main()
