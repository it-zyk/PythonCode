class MinOS(object):
    """MinOS 操作系统"""

    def __init__(self, name):
        # 初始化系统名字
        self.name = name
        self.apps = list()  # 安装程序列表

    def __str__(self):
        return "%s 安装的软件列表为 %s" % (self.name, str(self.apps))


    def install_app(self, app):
        # 安装软件
        if app.name in self.apps:
            print("此系统已经安装了%s, 无需再此安装" % app.name)
        else:
            app.install()
            self.apps.append(app.name)



class App(object):
    def __init__(self, name, version, desc):
        self.name = name
        self.version = version
        self.desc = desc

    def __str__(self):
        return "%s 的当前版本是 --%s ----%s" % (self.name, self.version, self.desc)

    def install(self):
        print("将 %s [%s]的执行程序复制到目录..." % (self.name,self.version))


    
class Pycharm(App):
    pass


class Chrome(App):
    def install(self):
        print("正在解压要安装的程序文件....")
        super().install()




def main():
    linux = MinOS("Linux")
    print(linux)

    pycharm = Pycharm("Pycharm", "1.0", "python 开发的 IDE 环境")
    chrome = Chrome("Chrome", "2.0", "谷歌浏览器")

    linux.install_app(pycharm)
    linux.install_app(chrome)

    print(linux)


if __name__ == "__main__":
    main()
