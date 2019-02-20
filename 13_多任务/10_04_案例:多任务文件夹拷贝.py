import os
import sys
import multiprocessing


gl_file_path ="/home/zyk/code/"

def copy_file(q, file_name, old_folder_name, new_folder_name):
    """完成文件的copy"""
   # print("========模拟copy 【%s】 文件从 【%s】 到 【%s】" % (file_name, old_folder_name, new_folder_name))
   
    # 读取文件
    old_file_path = gl_file_path + old_folder_name + "/" + file_name 
    old_f = open(old_file_path, "rb")
    content = old_f.read()
    old_f.close()


    # 写入新文件夹
    new_file_path = gl_file_path + new_folder_name + "/" + file_name 
    new_f = open(new_file_path, "wb")
    new_f.write(content)
    new_f.close()
    
    # 如果拷贝完成了文件夹，那么就向队列中写入一个消息 表示已经完成

    q.put(file_name)

def main():
    # 1. 获取要copy的文件夹的名字
    old_folder_name = input("请输入要copy的文件夹的名字")
    
    # 2. 创建一个新的文件夹
    try:
        new_folder_name = old_folder_name + "[复件]"
        os.mkdir(gl_file_path + new_folder_name)

    except:
        pass

    # 3 获取文件夹中所有待copy 的文件名字 listdir()
    
    file_names = os.listdir(gl_file_path + old_folder_name)
    
    # 4 创建进程池
    po = multiprocessing.Pool(5)

    
    # 创建队列
    q = multiprocessing.Manager().Queue()


    # 复制原文件中的文件，到新文件中的文件去
    
    for file_name in  file_names:
        po.apply_async(copy_file, args=(q, file_name, old_folder_name, new_folder_name))
    po.close()
    # po.join()
    all_file_num = len(file_names)
    copy_ok_num = 0
    while True:
        file_name = q.get()
        copy_ok_num += 1
        # print("已经完成copy: %s" % file_name)
        print("\r拷贝的进度为：%.2f %%" % (copy_ok_num * 100 / all_file_num), end="")
        if copy_ok_num >= all_file_num:
            break
    # 另起一行
    print("")



if __name__ == "__main__":
    main()
