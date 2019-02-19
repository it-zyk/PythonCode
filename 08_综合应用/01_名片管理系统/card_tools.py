

# 所有名片的列表
card_list = list()


def show_menu():
    
    """显示菜单"""

    print("*" * 60)

    print("""欢迎使用【名片管理系统】 V 1.0
        
        1. 新建名片
        2. 显示全部
        3. 查询名片

        0. 是退出
    """)
    print("*" * 60)


def new_card():
    
    # 新增名片

    print("-" * 60)
    print("新增名片")

    # 1.提示用户输入信息
    name_str = input("请输入姓名：")
    phone_str =input("请输入电话：")
    qq_str = input("请输入电话：")
    email_str= input("请输入邮箱：")
    card_dict = { "name": name_str, 
            "phone": phone_str, 
            "qq": qq_str, 
            "email": email_str}
    card_list.append(card_dict)
    
    print(card_list)

    print("添加 %s 名片成功！" % name_str)



def show_all():
    
    # 显示全部
    print("-" * 60)
    if len(card_list) == 0:
       print("当前没有任何名片记录，请使用新增功能添加名片!")
       return
    for name in ["姓名", "电话", "qq", "邮箱"]:
        print(name, end="\t\t")
    print("")
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["phone"],card_dict["qq"], card_dict["email"]))
    

def search_card():

    # 搜索名片
    
    print("-" * 60)
    print("搜索名片")
    

    # 1. 提示用户输入要搜索的姓名
    find_name = input("请输入要搜素的姓名：")



    # 2.通过遍历名片列表，查询要搜素的姓名，如果没有找到，需要提示用户
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 60)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["phone"],card_dict["qq"], card_dict["email"]))
            deal_card(card_dict)
            break
    else:
        print("抱歉，没有找到。")


def deal_card(find_dict):
    
    print(find_dict)

    action_str = input("请选择要执行的操作 1 修改 2 删除 0 返回上级菜单")

    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "输入姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "输入电话：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "输入QQ：")
        find_dict["email"] = input_card_info(find_dict["email"], "输入邮箱：")
        print("修改名片成功！")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除名片成功！")
    else:
        return


def input_card_info(dict_value, tip_message):

    # 提示输入信息
    result_str = input(tip_message)

    # 针对用户输入进行判断， 如果用户输入内容，直接返回
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value

    # 如果没有输入内容，返回原有的值

