#! /usr/bin/python3


import card_tools




def main():
  
    while True:
        
        # 显示功能菜单
        card_tools.show_menu()

        action_str = input("请选择希望执行的操作：")
        
        print("您选择的操作是: 【%s】 " % action_str)
        
        # 1,2,3 针对名片的操作
        if action_str in ["1", "2", "3"]:
            # 新增名片
            if action_str == "1":
                card_tools.new_card()
            elif action_str == "2":
                card_tools.show_all()
            elif action_str == "3":
                card_tools.search_card()
            # 显示全部名片


            # 查询名片  
            pass
        # 输入 0 退出系统 
        elif action_str == "0":
            break
        else:
            print("您输入的不正确，请重新选择")

        # 其它输入错误，需要提示用户
    pass


if __name__ == "__main__":
    main()
