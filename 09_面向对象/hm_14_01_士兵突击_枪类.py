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



if __name__ == "__main__":
    
    ak = Gun("AK47")

    ak.add_bullet(50)
    ak.shoot()


        
        


	










