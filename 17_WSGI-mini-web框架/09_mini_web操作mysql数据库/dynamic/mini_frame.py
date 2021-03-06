import re
import time
import os
import pymysql
import urllib.parse
import logging


URL_FUNC_DICT = dict()


def route(url):
    def set_func(func):
        # URL_FUNC_DICT["/index.py"] = index
        URL_FUNC_DICT[url] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func


@route("/index.html")
def index(ret):
    with open("./templates/index.html") as f:
        content = f.read()

    # my_stock_info = "哈哈哈哈 这是你的本月名称....."

    # content = re.sub(r"\{%content%\}", my_stock_info, content)
    db = pymysql.connect(host='localhost', port=3306, user='root',
                         password='root', database='stock_db', charset='utf8')
    cursor = db.cursor()
    sql = """select * from info;"""
    cursor.execute(sql)
    stock_infos = cursor.fetchall()
    cursor.close()
    db.close()

    tr_tempt = """
    <tr>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>
        <input type="button" value="添加" id="toAdd" name="toAdd" systemIdValue="%s">
    </td>
    </tr>
    """
    html = ""

    for line_info in stock_infos:
        html += tr_tempt % (line_info[0], line_info[1], line_info[2], line_info[3],
                            line_info[4], line_info[5], line_info[6], line_info[7], line_info[1])
    content = re.sub(r"\{%content%\}", html, content)
    return content


@route("/center.html")
def center(ret):
    with open("./templates/center.html") as f:
        content = f.read()

    db = pymysql.connect(host='localhost', port=3306, user='root',
                         password='root', database='stock_db', charset='utf8')
    cursor = db.cursor()
    sql = """select a.code,a.short,a.chg,a.turnover,a.price,a.highs, b.note_info from info as a inner join focus as b on a.id = b.info_id; """
    cursor.execute(sql)
    stock_infos = cursor.fetchall()
    cursor.close()
    db.close()

    tr_tempt = """
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>
            <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
        </td>
        <td>
            <input type="button" value="删除" id="toDel" name="toDel" systemIdValue=%s>
        </td>
    </tr>
    """
    html = ""

    for line_info in stock_infos:
        html += tr_tempt % (line_info[0], line_info[1], line_info[2],
                            line_info[3], line_info[4], line_info[5], line_info[6], line_info[0], line_info[0])
    content = re.sub(r"\{%content%\}", html, content)
    return content

 #
 # URL_FUNC_DICT = {
 #        "/index.py": index,
 #       "/center.py": center
 #        }
 #


@route(r"/add/(\d+)\.html")
def add_focus(ret):
    # 1.获取股票代码
    # 2. 判断试下是否有这个股票代码，防止恶意添加
    # 3. 判断以下是否已经关注过
    stock_code = ret.group(1)

    db = pymysql.connect(host='localhost', port=3306, user='root',
                         password='root', database='stock_db', charset='utf8')
    cursor = db.cursor()
    sql = """select * from info where code=%s; """
    cursor.execute(sql, (stock_code,))
    if not cursor.fetchone():
        cursor.close()
        db.close()
        return "没有这只股票"

    cursor.execute(sql, (stock_code,))
    sql = """select * from info as i  inner join focus as f on i.id=f.info_id where i.code=%s; """
    cursor.execute(sql, (stock_code,))

    # 如果要是没有这个股票代码，那么认为是非法的请求
    if cursor.fetchone():
        cursor.close()
        db.close()
        return "已经关注了，请勿重复关注..."

    # 4. 添加关注
    sql = """insert into focus (info_id) select id from info where code=%s; """
    cursor.execute(sql, (stock_code,))
    db.commit()
    cursor.close()
    db.close()
    return "add %s OK " % str(stock_code)


@route(r"/del/(\d+)\.html")
def del_focus(ret):
    # 1.获取股票代码
    # 2. 判断试下是否有这个股票代码，防止恶意添加
    # 3. 判断以下是否已经关注过
    stock_code = ret.group(1)

    db = pymysql.connect(host='localhost', port=3306, user='root',
                         password='root', database='stock_db', charset='utf8')
    cursor = db.cursor()
    sql = """select * from info where code=%s; """
    cursor.execute(sql, (stock_code,))
    # 如果要是没有这个股票代码，那么认为是非法的请求
    if not cursor.fetchone():
        cursor.close()
        db.close()
        return "没有这只股票"

    cursor.execute(sql, (stock_code,))
    sql = """select * from info as i  inner join focus as f on i.id=f.info_id where i.code=%s; """
    cursor.execute(sql, (stock_code,))

    # 判断是否关注过
    if not cursor.fetchone():
        cursor.close()
        db.close()
        return "%s 之前未关注，请勿取消关注..." % stock_code

    # 4. 取消关注
    sql = """delete from focus where info_id = (select id from info where code=%s); """
    cursor.execute(sql, (stock_code,))
    db.commit()
    cursor.close()
    db.close()
    return "取消关注成功"


@route(r"/update/(\d+)\.html")
def show_update_page(ret):
    """显示修改的那个页面"""
    # 1. 获取股票代码
    stock_code = ret.group(1)

    # 2. 打开模板
    with open("./templates/update.html") as f:
        content = f.read()

    # 3. 根据股票代码查询相关的备注信息
    db = pymysql.connect(host='localhost', port=3306, user='root',
                         password='root', database='stock_db', charset='utf8')
    cs = db.cursor()
    sql = """select f.note_info from focus as f inner join info as i on i.id=f.info_id where i.code=%s;"""
    cs.execute(sql, (stock_code,))
    stock_infos = cs.fetchone()
    note_info = stock_infos[0]  # 获取这个股票对应的备注信息
    cs.close()
    db.close()

    content = re.sub(r"\{%note_info%\}", note_info, content)
    content = re.sub(r"\{%code%\}", stock_code, content)

    return content


@route(r"/update/(\d+)/(.*)\.html")
def save_update_page(ret):
    """"保存修改的信息"""
    stock_code = ret.group(1)
    comment = ret.group(2)
    # URL 解码
    comment = urllib.parse.unquote(comment)
    db = pymysql.connect(host='localhost', port=3306, user='root',
                         password='root', database='stock_db', charset='utf8')
    cs = db.cursor()
    sql = """update focus set note_info=%s where info_id = (select id from info where code=%s);"""
    cs.execute(sql, (comment, stock_code))
    db.commit()
    cs.close()
    db.close()

    return "修改成功..."


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])

    file_name = env['PATH_INFO']
    # file_name = "/index.py"

    # return URL_FUNC_DICT[file_name]()

    logging.basicConfig(level=logging.INFO,
                        filename='./log.txt',
                        filemode='a',
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

    logging.info("访问的是，%s" % file_name)
    try:
        for url, func in URL_FUNC_DICT.items():
            ret = re.match(url, file_name)
            if ret:
                return func(ret)
            else:
                 logging.warning("没有对应的函数....")
                 return "请求的url(%s)没有对应的函数...." % file_name

        # func = URL_FUNC_DICT[file_name]
        # return func()
    except Exception as ret:
        return "产生了异常 %s" % str(ret)
