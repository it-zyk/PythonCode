# 1.士兵y许三多有一把 AK47
# 2.士兵可以开火
# 3. 枪 能够发射 子弹
# 4. 枪装满子弹--增加子弹数量

#coding=utf-8

class Gun:
    
    def __init__(self, model):
        
        # 1.枪的属性 
        self.model = model

        # 2.子弹的数量
        self.bullet_count = 0


    def add_bullet(self, count):

        self.bullet_count += count


    def shoot(self):

        # 1.判断子弹数量
        if self.bullet_count <= 0:
            print("[%s] 没有子弹了" % self.model)
            return

        # 2.发射子弹
        self.bullet_count -= 1

        # 3.提示发射信息
        print("【%s】 突突突突... 剩余子弹【%d】" % (self.model, self.bullet_count))


    def __str__(self):
        return ("枪型号：【%s】\n 子弹数量:【%d】" % (self.model, self.bullet_count))

class Soldier:

    def __init__(self, name):
        
        # 1.新兵的姓名
        self.name = name

        # 2.枪的属性
        self.gun = None
       


    def fire(self):

        # 1.判断士兵是否有枪
        if self.gun is None:
            print("【%s】 还没有枪" % self.name)
            return

        # 2. 高喊口号
        print("冲啊...【%s】" % self.name)

        # 3 让枪发射子弹
        self.gun.shoot()
        


if __name__ == "__main__":
    
    ak47 = Gun("AK47")
    ak47.add_bullet(50)

#    ak47.shoot()
#
    # 创建y许三多
    xusanduo = Soldier("许三多")

    xusanduo.gun = ak47
    
    xusanduo.fire()

    print(xusanduo.gun)
        
        


	










