import re
import time
import os
import pymysql

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
    sql = """select a.code,a.short,a.chg,a.turnover,a.price,a.highs, b.note_info from info as a inner join focus as b on a.id = b.id; """
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
        <input type="button" value="删除" id="toDel" name="toDel" systemIdValue="00007">
    </td>
    </tr>
    """
    html = ""

    for line_info in stock_infos:
        html += tr_tempt % (line_info[0], line_info[1], line_info[2],
                            line_info[3], line_info[4], line_info[5], line_info[6])
    content = re.sub(r"\{%content%\}", html, content)
    return content

 #
 # URL_FUNC_DICT = {
 #        "/index.py": index,
 #        "/center.py": center
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
    sql = """selct * from info as i  inner join focus as f on i.id=f.info_id where i.code = %s; """
    cursor.execute(sql, (stock_code,))
    # 如果要是没有这个股票代码，那么认为是非法的请求
    if not cursor.fetchone():
        cursor.close()
        db.close()
        return "已经关注了，请勿重复关注..."
    # 4. 添加关注
    sql ="""insert into focus (info_id) select id from info where code = %s """
    cursor.execute(sql, stock_code)
    db.commit()
    cursor.close()
    db.close()
    return "add %s OK "  % str(stock_code)


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])

    file_name = env['PATH_INFO']
    # file_name = "/index.py"

    # return URL_FUNC_DICT[file_name]()
    try:
        for url, func in URL_FUNC_DICT.items():
            ret = re.match(url, file_name)
            if ret:
                return func(ret)

        # func = URL_FUNC_DICT[file_name]
        # return func()
    except Exception as ret:
        return "产生了异常 %s" % str(ret)
